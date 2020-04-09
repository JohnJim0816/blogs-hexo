- [github上如何为markdown文件生成目录](#github%e4%b8%8a%e5%a6%82%e4%bd%95%e4%b8%bamarkdown%e6%96%87%e4%bb%b6%e7%94%9f%e6%88%90%e7%9b%ae%e5%bd%95)
  - [写在前面](#%e5%86%99%e5%9c%a8%e5%89%8d%e9%9d%a2)
  - [网页生成](#%e7%bd%91%e9%a1%b5%e7%94%9f%e6%88%90)
  - [使用toc工具](#%e4%bd%bf%e7%94%a8toc%e5%b7%a5%e5%85%b7)
  - [最简单的markdown插件](#%e6%9c%80%e7%ae%80%e5%8d%95%e7%9a%84markdown%e6%8f%92%e4%bb%b6)
  
# github上如何为markdown文件生成目录
## 写在前面
熟悉markdown都知道可以使用[TOC]自动生成markdown文件的标题目录，比如在typora，vscode(需要插件)等本地编辑器中，或者在CSDN等网页编辑器中，但是github却不支持[TOC]标签，至于为什么不支持感兴趣的可以深入搜索，而相应的解决方法之一就是为md文件自动生成适用于github的目录。
## 网页生成
有没有这样自动生成目录的操作呢？答案是有的，其中之一就是在线的generator，比如[GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/)。但是经本人实测并不好用且麻烦。
## 使用toc工具
网页生成的方法并不好用，使用toc工具，比如gh-md-toc这个神器，如何安装可参考这篇博文[快速生成Github README.md的目录](https://www.jianshu.com/p/302abe331dcb)。安装后在终端输入命令就可以在终端里生成目录，但是也比较麻烦，因为是在终端生成的，复制粘贴到md文件里比较麻烦，还要注意格式对齐的问题。
## 最简单的markdown插件
笔者目前了解到的最最最简单的莫过于VSCode中的Markdown All in One
插件了，安装后点开md文件，然后快捷键```CTRL(CMD)+SHIFT+P```，输入```Markdown All in One: Create Table of Contents```回车即可，如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200406223412339.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5KaW0w,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200406223421963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5KaW0w,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200406223428541.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5KaW0w,size_16,color_FFFFFF,t_70)
