---
title: VSCode编写latex
date: 2020-04-11 21:49:48
categories: 野生技术
tags:
    - latex
    - VSCode
---

# VSCode编写latex
## 0 写在前面


由于latex相关软件的编辑界面不太舒服，加上笔者钟情于VSCode，而网上没有一个简单易用的VSCode搭建教程，故有此书。

编写latex的工具也多种多样，各有所爱，使用latex环境自带的编辑器固然无可厚非，然界面过于鄙陋，且无法实时编译预览，因而需要结合第三方文本编辑器，有结合ctex，有使用notepad++，而笔者更钟情于VSCode。VSCode的美妙无可言语，亦不多言，以下直接切入正题，如何使用VSCode编写latex，或者说搭建latex环境。

<!-- more-->
## 1 安装Latex环境
Latex环境即Tex Live，见[参考链接1.1](https://www.tug.org/texlive/)  
不同系统有不同的版本，并且还有完整版和简化版，这里给出全是不同系统完整版的传送门
[MacTex下载链接](http://www.tug.org/mactex/mactex-download.html)
WIN上texlive可以现在在线安装版，也可以下载离线安装iso版本，由于网速问题，推荐下载离线iso的镜像
[texlive iso清华镜像下载](https://mirrors.tuna.tsinghua.edu.cn/ctan/systems/texlive/Images/)
[texlive iso安装教程](https://jingyan.baidu.com/article/4f34706e6e1c85e387b56dae.html)

## 2 LaTeX Workshop
此乃VSCode插件，搜索安装即可，该插件的作用即将latex环境和第三方编辑器VSCode结合，使得在VSCode中能够调用latex环境。至于VSCode如何安装插件比较简单，可自查。
## 3 设置settings.json(针对中文)
[mac参考链接](https://blog.csdn.net/WinstonLau/article/details/89467446)  
[win参考链接](https://zhuanlan.zhihu.com/p/38178015)  
以上给出两个关于配置VSCode内settings.json的参考链接，实际上不管什么系统，配置都是一样的，如下：
快捷键cmd(ctrl)+shift+p输入setting打开settings.json把以下代码加入，注意在原本内容的最后一行加上英文逗号换行再复制粘贴，不然会报错

此外如果需要支持中文路径下的文件，需要把以下内容中的%DOC%改为%DOCFILE%"，但此处笔者建议涉及代码方面不要用中文路径。

```json
"latex-workshop.view.pdf.viewer": "tab",
    "latex-workshop.latex.tools": [
      {
          "name": "xelatex",
          "command": "xelatex",
          "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "-pdf",
              "%DOC%"
          ]
      },
      {
          "name": "latexmk",
          "command": "latexmk",
          "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "-pdf",
              "%DOC%"
          ]
      },
      {
          "name": "pdflatex",
          "command": "pdflatex",
          "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "%DOC%"
          ]
      },
      {
          "name": "bibtex",
          "command": "bibtex",
          "args": [
              "%DOCFILE%"
          ]
      }
  ],
  "latex-workshop.latex.recipes": [
      {
          "name": "xelatex",
          "tools": [
              "xelatex"
          ]
      },
      {
          "name": "pdflatex -> bibtex -> pdflatex*2",
          "tools": [
              "pdflatex",
              "bibtex",
              "pdflatex",
              "pdflatex"
          ]
      }
  ]
```
# 4 demo
在 __英文__ 路径下新建一个.tex文件，输入代码如下，注意首行\documentclass[UTF8]{ctexart} 用于支持中文
```latex
\documentclass[UTF8]{ctexart} 
\title{你好，world!}
\author{Winston}
\date{\today}
\begin{document}
\maketitle
你好，world！
\end{document}
```
然后cmd(ctrl)+s保存编译，就会生成.aux、.pdf等文件，注意保存的过程同时也是编译的过程，然后打开右上角预览就会看到生成的pdf