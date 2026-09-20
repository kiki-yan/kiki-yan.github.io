
由于我对自己的前端水平十分有数，所以想都没想就立刻放弃了“要不自己写一个网站？”的想法。

后来想起之前逛过的ouuan大佬的博客非常好看，我的收藏夹里甚至还有他搭建博客的指南，就直接拿来用了，采用的是 **hugo + even主题 + github actions**，参考资料如下:
> https://ouuan.gitee.io/post/from-hexo-to-hugo/

## 搭建过程

### Step 1 阅读指南
首先阅读ouuan的指南(上述链接)，然后使用他的[hugo模版](https://github.com/ouuan/hugo-blog-template)，按照模版里指示的进行clone。

### Step 2 Config的修改
还是按照模版里指示的，修改一下配置文件`config.toml`里的相关配置，一些需要更改的内容：
1. 包含`yourname`的部分
2. `newContentEditor = ""`
3. `defaultContentLanguage = "en"`
4. `[[menu.main]]`的相关内容 (视情况进行保留和删除)
5. **不要**更改 `[params]` 中的 `version="4.x"`

### Step 2.5 创建repository
因为我打算部署到github pages上，就在github上创建一个新的repository，叫`kiki-yan.github.io`

### Step 3 本地测试
配置完成后，可以 `hugo new post/test.md` 创建一个新的post(在`hugo-blog/content/post/test.md`), 按照markdown随便写点东西以后保存，然后 `hugo server`，打开localhost看一下效果(也可以边写边看效果，热加载真香)。最后用`hugo`命令生成静态文件，就是`hugo-blog/public/`文件夹，把这个文件夹内的内容push到github上就可以了。

注： blog的源代码和网页内容并不是一个东西!

1. 源代码: 是`hugo-blog/` 下除了`hugo-blog/public/`以外的内容，包含了 `content/`, `config.toml` 之类的文件。
2. 网页内容：只是 `hugo-blog/public/`内的内容，有了源代码就可以用`hugo`生成网页内容，但是反之就不可以！

既然两者有别，就要分开管理，我把它们放在同一个repository里，分成2个branch。源代码就放在了`master`里，网页内容就放在`publish`上了。

### Step 4 Github Settings
这个时候网页上应该是没有内容的，因为github pages需要设置一下指定deploy的branch，在repository的`Settings`里，拉到下面看到`GitHub Pages`，改一下Source branch就可以了：
![image](/images/001/1.png)
