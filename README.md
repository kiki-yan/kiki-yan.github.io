newContentEditor = ""
baseURL = "https://kiki-yan.github.io"
languageCode = "en"
defaultContentLanguage = "en"                             # en / zh-cn / ... (This field determines which i18n file to use)
title = "kiki_yan"
preserveTaxonomyNames = true
enableRobotsTXT = true
enableEmoji = true
theme = ["hugo-video", "even"]
enableGitInfo = true # use git commit log to generate lastmod record # 可根据 Git 中的提交生成最近更新记录。

# Syntax highlighting by Chroma. NOTE: Don't enable `highlightInClient` and `chroma` at the same time!
# pygmentsOptions = "linenos=table"
pygmentsCodefences = false
# pygmentsStyle = "pygments"

hasCJKLanguage = true     # has chinese/japanese/korean ? # 自动检测是否包含 中文/日文/韩文
paginate = 10                                              # 首页每页显示的文章数
DisqusShortname = ""      # disqus_shortname
googleAnalytics = "UA-kiki_yan"      # UA-XXXXXXXX-X
copyright = ""            # default: author.name ↓        # 默认为下面配置的author.name ↓

[author]                  # essential                     # 必需
  name = "kiki_yan"

[sitemap]                 # essential                     # 必需
  changefreq = "weekly"
  priority = 0.5
  filename = "sitemap.xml"

[[menu.main]]             # config your menu              # 配置目录
  name = "Home"
  weight = 10
  identifier = "home"
  url = "/"
[[menu.main]]
  name = "Post"
  weight = 20
  identifier = "archives"
  url = "/post/"
[[menu.main]]
  name = "Tags"
  weight = 30
  identifier = "tags"
  url = "/tags/"
[[menu.main]]
  name = "Categories"
  weight = 40
  identifier = "categories"
  url = "/categories/"
[[menu.main]]
  name = "About"
  weight = 50
  identifier = "about"
  url = "/about/"
[[menu.main]]
  name = "CF-Problems"
  weight = 60
  identifier = "cf-problems"
  url = "/cf-problems/"
[[menu.main]]
  name = "Search"
  weight = 70
  identifier = "search"
  url = "/search/"

[params]
  version = "4.x"           # Used to give a friendly message when you have an incompatible update
  debug = false             # If true, load `eruda.min.js`. See https://github.com/liriliri/eruda

  since = "2021"            # Site creation time          # 站点建立时间
  # use public git repo url to link lastmod git commit, enableGitInfo should be true.
  # 指定 git 仓库地址，可以生成指向最近更新的 git commit 的链接，需要将 enableGitInfo 设置成 true.
  gitRepo = "https://github.com/kiki-yan/kiki-yan.github.io"

  # site info (optional)                                  # 站点信息（可选，不需要的可以直接注释掉）
  # logoTitle = "Even"        # default: the title value    # 默认值: 上面配置的title值
  keywords = ["kiki_yan", "blog", "huzhenwei", "胡振为"]
  description = "kiki_yan的博客"

  # paginate of archives, tags and categories             # 归档、标签、分类每页显示的文章数目，建议修改为一个较大的值
  archivePaginate = 25
  showArchiveCount = true
  dateFormatToUse = "2006-01-02"
  moreMeta = false
  highlightInClient = true
  toc = true
  autoCollapseToc = true
  fancybox = false
  mathjax = true
  mathjaxEnableSingleDollar = true
  mathjaxEnableAutoNumber = false
  mathjaxUseLocalFiles = false
  postMetaInFooter = true
  linkToMarkDown = false
  contentCopyright = '<a rel="license noopener" href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a>'
  baiduPush = true
  baiduAnalytics = ""
  baiduVerification = "kiki_yan"
  googleVerification = "kiki_yan"
  customCSS = []
  customJS = []
  uglyURLs = false

  [params.publicCDN]
    enable = true
    jquery = '<script src="https://cdn.jsdelivr.net/npm/jquery@3.2.1/dist/jquery.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>'
    slideout = '<script src="https://cdn.jsdelivr.net/npm/slideout@1.0.1/dist/slideout.min.js" integrity="sha256-t+zJ/g8/KXIJMjSVQdnibt4dlaDxc9zXr/9oNPeWqdg=" crossorigin="anonymous"></script>'
    fancyboxJS = '<script src="https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.1.20/dist/jquery.fancybox.min.js" integrity="sha256-XVLffZaxoWfGUEbdzuLi7pwaUJv1cecsQJQqGLe7axY=" crossorigin="anonymous"></script>'
    fancyboxCSS = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.1.20/dist/jquery.fancybox.min.css" integrity="sha256-7TyXnr2YU040zfSP+rEcz29ggW4j56/ujTPwjMzyqFY[..."'
    timeagoJS = '<script src="https://cdn.jsdelivr.net/npm/timeago.js@3.0.2/dist/timeago.min.js" integrity="sha256-jwCP0NAdCBloaIWTWHmW4i3snUNMHUNO+jr9rYd2iOI=" crossorigin="anonymous"></script>'
    timeagoLocalesJS = '<script src="https://cdn.jsdelivr.net/npm/timeago.js@3.0.2/dist/timeago.locales.min.js" integrity="sha256-ZwofwC1Lf/faQCzN7nZtfijVV6hSwxjQMwXL4gn9qU8=" crossorigin="anonymous"></script>'
    flowchartDiagramsJS = '<script src="https://cdn.jsdelivr.net/npm/raphael@2.2.7/raphael.min.js" integrity="sha256-67By+NpOtm9ka1R6xpUefeGOY8kWWHHRAKlvaTJ7ONI=" crossorigin="anonymous"></script>'
    sequenceDiagramsCSS = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bramp/js-sequence-diagrams@2.0.1/dist/sequence-diagram-min.css" integrity="sha384-6QbLKJMz5dS3adWSeINZe74uSydBG[..."'
    sequenceDiagramsJS = '<script src="https://cdn.jsdelivr.net/npm/webfontloader@1.6.28/webfontloader.js" integrity="sha256-4O4pS1SH31ZqrSOA/2QJTVjTPqVe+jnYgOWUVr7EEc=" crossorigin="anonymous"></script>'

  [params.outdatedInfoWarning]
    enable = false
    hint = 180
    warn = 720

  [params.gitment]
    owner = ""
    repo = ""
    clientId = ""
    clientSecret = ""

  [params.utterances]
    owner = "kiki-yan"
    repo = "kiki-yan.github.io"

  [params.gitalk]
    owner = ""
    repo = ""
    clientId = ""
    clientSecret = ""

  [params.valine]
    enable = false
    appId = ''
    appKey = ''
    notify = false
    verify = false
    avatar = 'mm'
    placeholder = '说点什么吧...'
    visitor = false

  [params.flowchartDiagrams]
    enable = false
    options = ""

  [params.sequenceDiagrams]
    enable = false
    options = ""

  [params.busuanzi]
    enable = true
    siteUV = true
    sitePV = true
    pagePV = true

  [params.reward]
    enable = false
    wechat = "/path/to/your/wechat-qr-code.png"
    alipay = "/path/to/your/alipay-qr-code.png"

  [params.social]
    a-email = "mailto:huzhenweitom@gmail.com"
    b-github = "https://github.com/kiki-yan"

[privacy]
  [privacy.googleAnalytics]
    anonymizeIP = true
  [privacy.youtube]
    privacyEnhanced = true

[markup.goldmark.renderer]
  unsafe = true

[outputs]
  home = ["HTML", "RSS", "JSON"]

[markup.tableOfContents]
  startLevel = 1
  endLevel = 4

[minify]
  disableHTML = true
