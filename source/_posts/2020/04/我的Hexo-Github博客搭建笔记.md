---
title: 我的Hexo-Github博客搭建笔记
date: 2020-04-10 21:29:41
tags:
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

### 安装hexo

终端运行

```bash
npm install -g hexo-cli
```

然后本地新建一个文件夹如hexo-blogs，并cd到该路径，执行初始化，考虑到每个人命名方式不同，hexo-blogs/这里我称为**主目录**，

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

然后本地主目录hexo-blogs下，终端运行如下命令安装hexo-deployer-git。

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
配置完成之后，使用```hexo n 博客题目``` 新建，```hexo g```生成，然后```hexo d```发布，也可以```hexo g -d```将两步合为一步。然后需要等待一段时间，就可以在```https://johnjim0816.github.io/``看到自己的博客了。

## 安装next主题来装点博客



hexo自带的主题是landscape，对应带主目录`themes`文件夹下，这个主题只能说是平平无奇！！！
因此需要安装一个靓靓的主题来使我们的博客秀色可餐，这里推荐[next主题](https://github.com/theme-next/hexo-theme-next)，截止2020年4月10日该主题已经更新到了v7.8.0，可以直接下载整个仓库并在本地解压，将名字改为next，然后放到主目录下的`themes`文件夹下。

在站点配置文件即`hexo-blogs/_config.yml`中将语言更改为中文，如下，注意冒号之后有一个空格

```
language: zh-CN
```

并且将主题改为next：

```
theme: next
```

保存之后使用hexo g -d可以看到初步效果，不过在类似于这些测试的操作还是建议在本地服务器上进行，github page刷新的速度简直就是谜一样的存在。

### 更多配置
