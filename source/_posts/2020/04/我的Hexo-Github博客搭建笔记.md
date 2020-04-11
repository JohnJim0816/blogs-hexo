---
title: 我的Hexo-Github博客搭建笔记
date: 2020-04-10 21:29:41
categories: 野生技术
tags: 
    - hexo
    - 笔记
---
## 从零开始搭建个人博客

主要参考以下链接

[官方文档](https://hexo.io/zh-cn/docs/)
[知乎](https://zhuanlan.zhihu.com/p/26625249)
[b站视频](https://www.bilibili.com/video/BV1Yb411a7ty)

### 安装依赖包node.js

一种方法直接上[node.js](https://nodejs.org/en/)安装，该安装包包括node.js和npm

由于在国内接下来需要更改npm镜像，如下，更多命令参考[CSDN]()：

```bash
npm config set registry https://registry.npm.taobao.org
```
<!-- more -->

### 安装hexo

终端运行

```bash
npm install -g hexo-cli
```

然后本地新建一个文件夹如blogs，并cd到该路径，执行初始化，考虑到每个人命名方式不同，blogs/这里我称为**主目录**，

```bash
hexo init
```

### 本地服务器网页(可选)

利用PC端生成服务器开启网页，比后面部署到github pages上刷新要快，可用于测试

先新建一个博客文档，即

```bash
hexo n test
```

此时会在主目录```source/_posts```下生成一个test.md文件，就是我们的第一个博客test，编辑完毕后保存，然后

```bash
hexo d
```

生成相应的网页文件，然后

```bash
hexo s
```

就会启动本地服务器，点击[http://localhost:4000](http://localhost:4000)就可以看到博客网页，终端```CTRL+C```则关闭本地服务器。

### 部署到Github Pages

本地服务器生成的网页别人是没法看到的，因此可以选择部署到github pages上。

首先Github网页上新建一个repo，名字严格为```用户民.github.io```，比如我的用户名为```JohnJim0816```，则相应的仓库名为```JohnJim0816.github.io```。

然后本地主目录blogs下，终端运行如下命令安装hexo-deployer-git。

```bash
npm install hexo-deployer-git --save
```

然后在主目录的配置文件```_config.yml```中(这里称之为站点配置文件，后面还有一个同名的主题配置文件)，找到deploy部分，并更改如下，注意repo部分根据个人github用户名而定。

```yml
deploy:
  type: git
  repo: https://github.com/JohnJim0816/JohnJim0816.github.io
  branch: master
```
配置完成之后，使用```hexo n 博客题目``` 新建，```hexo g```生成，然后```hexo d```发布，也可以```hexo g -d```将两步合为一步。然后需要等待一段时间，就可以在```https://johnjim0816.github.io/```看到自己的博客了。

![image1](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/04/我的Hexo-Github博客搭建笔记/1.png)




## 安装next主题来装点博客

hexo自带的主题是landscape，对应带主目录`themes`文件夹下，这个主题只能说是平平无奇！！！
因此需要安装一个靓靓的主题来使我们的博客秀色可餐，这里推荐[next主题](https://github.com/theme-next/hexo-theme-next)，截止2020年4月10日该主题已经更新到了v7.8.0。注意还有一个[iissnan/hexo-theme-next](https://github.com/iissnan/hexo-theme-next)，这个虽然star很多但是已经不维护了，所以推荐前面一个。可以直接下载整个仓库并在本地解压，将名字改为next，然后放到主目录下的`themes`文件夹下。

在站点配置文件即```blogs/_config.yml```中将语言更改为中文，如下，注意冒号之后有一个空格

```
language: zh-CN
```

并且将主题改为next：

```
theme: next
```

保存之后使用hexo g -d可以看到初步效果，不过在类似于这些测试的操作还是建议在本地服务器上进行，github page刷新的速度简直就是谜一样的存在。

## 后续优化

### 给本地文章md文件按年月分类

现在```hexo n 文章名```会在```source/_posts/```下创建文件，但是如果文章太多的话放在同一个目录下不好管理，此时可以更改站点配置文件```blogs/_config.yml```中的```new_post_name```，如下
```yml
new_post_name: :year/:month/:title.md 
```
这样```hexo n 文章名```之后会在```source/_posts/```创建比如2020/04/文章名.md文件，即按年月分类。

### 插入图片

插入图片这个搞了我好久，首先强烈建议使用图床，常见的可以搜索Github+PigGo。然后文章中直接按如下格式即可。
```markdown
![fig1](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/4/10/1.png)
```

插入本地图片的方式参考[CSDN](https://blog.csdn.net/JohnJim0/article/details/105430915)，注意hexo-asset-image模块的安装可能会造成文章目录中文乱码的bug，如下：

![image2](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/04/我的Hexo-Github博客搭建笔记/2.png)


### 添加站内搜索

首先安装
```bash
npm install hexo-generator-search --save
```
然后站点配置文件```blogs/_config.yml```添加
```yml
search:
  path: ./public/search.xml
  field: post
  format: html
  limit: 10000
```
主题配置文件```themes/next/_config.yml```设置
```yml
local_search:
  enable: true
  # If auto, trigger search by changing input.
  # If manual, trigger search by pressing enter key or search button.
  trigger: auto
  # Show top n results per article, show all results by setting to -1
  top_n_per_article: 1
```

### 给网页文章增加分类和标签

首先```hexo n page categories```以及```hexo n page tags```新建目录页和标签页，此时本地```source```文件夹下会生成相应的文件夹，将比如```categories```中的index.md更改如下：
```markdown
---
title: 分类
date: 2020-04-10 21:53:23
type: categories
---
```
关键是type这一项，```tags```也同理，
```markdown
---
title: 标签
date: 2020-04-10 21:53:46
type: tags
---
```
然后在文章开头的Front-matter部分，写上相应分类和标签，如下
```markdown
---
title: 我的Hexo-Github博客搭建笔记
date: 2020-04-10 21:29:41
categories: 野生技术
tags: 
    - hexo
    - 笔记
---
```
再到主题配置文件，即```themes```下的```_config.yml```文件，找到```menu```部分，配置如下：
```yml
menu:
  home: / || home
  categories: /categories/ || th
  tags: /tags/ || tags
  archives: /archives/ || archive
```
其中```||```后面指向图标的链接，如果没有则图标默认是问号。

由此可以类推新建一个类似于标签、分类这样的菜单栏，可参考[这个博客](https://hoxis.github.io/Hexo+Next%20%E6%96%B0%E5%A2%9E%E8%8F%9C%E5%8D%95%E5%88%86%E7%B1%BB%E9%A1%B5%E9%9D%A2.html)

### 增加百度统计

可参考[官方文档](http://theme-next.iissnan.com/getting-started.html#theme-settings)

### 如何开启阅读全文

在文章中加入```<!-- more -->```即可，参考[官方文档](https://theme-next.org/docs/theme-settings/posts)

### 增加阅读时间和字数统计
首先安装hexo-symbols-count-time，
```bash
npm i hexo-symbols-count-time --save
```
如果之前安装了hexo-wordcount就要卸载掉```npm uninstall hexo-wordcount```，因为它只适用于老版本，网页也有教程是这个，
修改站点配置文件```/_config.yml```，没有就添加
```markdown
symbols_count_time: 
  symbols: true
  time: true
  total_symbols: true
  total_time: true
  awl: 2
  wpm: 300
```
其中awl（Average Word Length）的数值是设定多少字符统计为一个字(word)，中文博客需要设置为 2。wpm（Words Per Minute）是你的阅读速度，多少字（word）统计为阅读时长一分钟。以下是官方文档里的一些阅读速度参考数据：
* 慢速：200
* 中速：275（默认）
* 快速：350
  
然后修改主题配置文件```next/_config.yml```，
```
symbols_count_time:
  separated_meta: true
  item_text_post: true
  item_text_total: true
```
最后需要```hexo clean```然后重新生成，否则可能会出现阅读时间NaN字样，参考[官方](https://theme-next.org/docs/theme-settings/posts)

### 增加valine评论系统

[知乎](https://www.zhihu.com/question/267598518)有关于评论系统的讨论，目前我暂时使用valine评论系统。

#### leancloud中进行相关的准备工作
该评论系统依赖于leancloud，所以需要先在leancloud中进行相关的准备工作。
* [登录](https://leancloud.cn/dashboard/login.html#/signin) 或 [注册](https://leancloud.cn/dashboard/login.html#/signup) LeanCloud
* 登录成功后，进入后台点击左上角的创建应用：
  
  ![image3](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/04/我的Hexo-Github博客搭建笔记/3.png)
  
* 创建好应用，进入应用，左边栏找到 **设置** ，然后点击 **应用Key**，此时记录出现的 **App ID** 和 **App Key**，后面配置文件中会用到
* 因为评论和文章阅读数统计依赖于存储，所以还需要建立两个新的存储 `Class`，左边栏找到并点击 **存储**，点击 **创建Class**:
  ![image4](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/04/我的Hexo-Github博客搭建笔记/4.png)

* 创建两个存储Class，分别命名为: `Counter` 和 `Comment`
* 还需要为应用添加安全域名，左边栏点击 **设置**，找到 **安全中心**，点击后会看到 **安全域名** 设置框，输入博客使用的域名，点击保存即可：
  ![image5](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/04/我的Hexo-Github博客搭建笔记/5.png)

#### 修改主题配置文件```next/_config.yml```

找到valine部分，

![image6](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/04/我的Hexo-Github博客搭建笔记/6.png)

上面几项内容的含义，这里简单说明需要修改的部分，具体还是要看 [Valine官网中配置相关的内容](https://valine.js.org/configuration.html)：

| 参数       | 用途                                                         |
| ---------- | ------------------------------------------------------------ |
| enable     | 这是用于主题中配置的，不是官方Valine的参数，**true**时控制开启此评论系统 |
| appId      | 这是在 [leancloud](https://leancloud.cn/) 后台应用中获取的，也就是上面提到的 **App ID** |
| appKey     | 这是在 [leancloud](https://leancloud.cn/) 后台应用中获取的，也就是上面提到的 **App Key** |
| notify     | 用于控制是否开启邮件通知功能，具体参考[邮件提醒配置](https://github.com/xCss/Valine/wiki/Valine-评论系统中的邮件提醒设置) |
| verify     | 用于控制是否开启评论验证码功能                               |
| avatar     | 用于配置评论项中用户头像样式，有多种选择：mm, identicon, monsterid, wavatar, retro, hide。详细参考：[头像配置](https://valine.js.org/avatar.html) |
| placehoder | 评论框的提示符                                               |
| visitor    | 控制是否开启文章阅读数的统计功能i, 详情阅读[文章阅读数统计](https://valine.js.org/visitor.html) |

#### 完善评论通知

**Valine** 评论邮件提醒功能不太健全，通知邮件中没有文章直达链接，**Valine** 官网中提供了评论系统第三方功能扩展[Valine](https://github.com/zhaojun1998/Valine-Admin)链接，按照链接中的说明，非常详细的步骤，一步步很容易实现完备的评论系统后台管理以及邮件提醒功能，部分高级配置[点我](https://github.com/zhaojun1998/Valine-Admin/blob/master/高级配置.md#自定义邮件服务器)了解。

#### 删除评论
直接在leancloud后台的存储中找到之前创建的```Comment```这个`class`找到对应评论删除即可。

![image7](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/04/我的Hexo-Github博客搭建笔记/7.png)