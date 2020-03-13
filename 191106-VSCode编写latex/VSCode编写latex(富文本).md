# VSCode编写latex
## 0 写在前面
先谈缘由，为何使用latex书写论文是众所周知之事，此处不多讲。但编写latex的工具也多种多样，各有所爱，使用latex环境自带的编辑器固然无可厚非，然界面过于鄙陋，且无法实时编译预览，因而需要结合第三方文本编辑器，有结合ctex，有使用notepad++，而笔者更钟情于VSCode。VSCode的美妙无可言语，亦不多言，以下直接切入正题，如何使用VSCode编写latex，或者说搭建latex环境。

## 1 安装Latex环境
安装自带的环境自是必要，Latex环境即Tex Live，见一下链接：

<center><font color=blue>https://www.tug.org/texlive/ </font></center>
而不同系统有不同的版本，并且还有完整版和简化版，此处给出全是不同系统完整版的传送门，

MacTex下载链接：
<center><font color=blue>http://www.tug.org/mactex/mactex-download.html</font></center>

WIN上texlive可以下载在线安装版，也可以下载离线安装iso版本，由于网速问题，推荐下载离线iso的镜像


texlive iso清华镜像：
<center><font color=blue>https://mirrors.tuna.tsinghua.edu.cn/ctan/systems/texlive/Images/</font></center>

texlive iso安装教程：
<center><font color=blue>https://jingyan.baidu.com/article/4f34706e6e1c85e387b56dae.html</font></center>

## 2 LaTeX Workshop
此乃VSCode插件，搜索安装即可，该插件的作用即将latex环境和第三方编辑器VSCode结合，使得在VSCode中能够调用latex环境。至于VSCode如何安装插件比较简单，可自查。
## 3 设置settings.json
仅是安装插件仍是不够，还需要配置VSCode的设置，即settings.json。
实际上不管系统几何，配置皆可“一概而论”，如下：
快捷键cmd(ctrl)+shift+p输入setting打开settings.json把以下代码加入，注意需在原本内容的最后一行加上英文逗号换行再复制粘贴，不然会报错。

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
配置既成，则试demo。即在 __英文__ 路径下新建一个.tex文件，输入代码如下，注意首行\documentclass[UTF8]{ctexart} 用于支持中文
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
然后cmd(ctrl)+s保存编译，就会生成.aux、.pdf等文件，注意保存的过程同时也是编译的过程，然后打开右上角预览就会看到生成的pdf，至此大功告成。