import argparse
import json
import os
import time

import requests

FILE_PATH = "static/contests.json"
INVALID_ID = {
    1597, 1596, 1595, 1410, 1414, 1412, 1258, 1226, 1224, 1222,
    1094, 1050, 1049, 1048, 905, 885, 874, 857, 826, 728, 726, 693,
    630, 345, 76, 48, 38, 22, 17, 6,
}
ALLOWED_CONTEST_PHASES = {"FINISHED", "SYSTEM_TEST", "CODING"}
contest_id_dict = {}


def process(problem):
    result = {
        key: value
        for key, value in problem.items()
        if key in ("contestId", "index", "name", "rating")
    }
    result.update(solved=0, attempted=0, sub=0)
    return result


def load_contest_json():
    global contest_id_dict
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"Data file does not exist: {FILE_PATH}")
    with open(FILE_PATH, encoding="utf-8") as infile:
        contest_list = json.load(infile)
    contest_id_dict = {
        contest["id"]: contest
        for contest in contest_list
        if contest and "id" in contest
    }
    print(f"Current file size = {os.path.getsize(FILE_PATH)}")


def load_contest_by_id(contest_id):
    url = (
        "https://codeforces.com/api/contest.standings"
        f"?contestId={contest_id}&showUnofficial=false"
    )
    try:
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            print(f"Skipping contest {contest_id}: API returned {response.status_code}")
            return None
        info = response.json()
        if info.get("status") != "OK":
            print(f"Skipping contest {contest_id}: {info.get('comment', 'API error')}")
            return None
    except (requests.RequestException, ValueError) as error:
        print(f"Skipping contest {contest_id}: {error}")
        return None

    result = info["result"]
    name = result["contest"]["name"]
    compact_name = "".join(name.split())
    problems = [process(problem) for problem in result.get("problems", [])]
    if not problems or any("rating" not in problem for problem in problems):
        print(f"Skipping contest {contest_id}: incomplete problem data")
        return None

    unique_indexes = {
        problem["index"][0] if len(problem["index"]) > 1 else problem["index"]
        for problem in problems
    }
    problem_count = len(unique_indexes)

    contest_type = "Others"
    if "Global" in compact_name:
        contest_type = "Global"
    elif "Educational" in compact_name:
        contest_type = "Educational"
    elif problem_count >= 10:
        contest_type = "ICPC"
    elif "Div.1+Div.2" in compact_name:
        contest_type = "Div1 + Div2"
    elif "Div.1" in compact_name and problem_count <= 8:
        contest_type = "Div1"
    elif "Div.2" in compact_name and problem_count <= 8:
        contest_type = "Div2"
    elif "Div.3" in compact_name:
        contest_type = "Div3"
    elif "Div.4" in compact_name:
        contest_type = "Div4"

    for row in result.get("rows", []):
        for index, problem_result in enumerate(row.get("problemResults", [])):
            if index >= len(problems):
                continue
            if problem_result.get("points", 0) > 0:
                problems[index]["attempted"] += 1 + problem_result.get(
                    "rejectedAttemptCount", 0
                )
                problems[index]["solved"] += 1

    return {
        "id": contest_id,
        "type": contest_type,
        "problems": problems,
        "name": name,
        "problem_cnt": problem_count,
        "sub": int(any(len(problem["index"]) > 1 for problem in problems)),
    }


def is_relevant_contest(contest):
    """Include finished and currently active contests so the site always shows newest CF rounds."""
    if contest.get("type") not in {"CF", "ICPC"}:
        return False
    return contest.get("phase") in ALLOWED_CONTEST_PHASES


def load_contest_all(force=False):
    for attempt in range(5):
        try:
            response = requests.get(
                "https://codeforces.com/api/contest.list", timeout=30
            )
            response.raise_for_status()
            contest_info = response.json()
            break
        except (requests.RequestException, ValueError) as error:
            print(f"Contest list attempt {attempt + 1}/5 failed: {error}")
            if attempt == 4:
                raise
            time.sleep(10)

    if contest_info.get("status") != "OK":
        raise RuntimeError("Loading Codeforces contest list failed")

    contests = []
    for contest in filter(is_relevant_contest, contest_info["result"]):
        contest_id = contest["id"]
        if contest_id in INVALID_ID:
            continue

        contest_obj = contest_id_dict.get(contest_id)
        if contest_obj is None or force:
            contest_obj = load_contest_by_id(contest_id)
            if contest_obj:
                contest_id_dict[contest_id] = contest_obj

        if contest_obj:
            contests.append(contest_obj)

    with open(FILE_PATH, "w", encoding="utf-8") as outfile:
        json.dump(contests, outfile, ensure_ascii=False)
    print(f"After update, file size = {os.path.getsize(FILE_PATH)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", "-f", action="store_true")
    args = parser.parse_args()
    load_contest_json()
    load_contest_all(args.force)
