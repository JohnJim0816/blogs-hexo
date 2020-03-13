# VSCode实现文献管理
作者：JJ	日期：191104
## 1 主流文献管理软件
[1.1]:https://www.zhihu.com/question/20761911
[1.2]:https://zhuanlan.zhihu.com/p/30168046
常用的文献管理软件有mendely，zotero，endnote和Papers(需要付费)，具体对比参考链接[1.1]、[1.2]  
笔者只用过Mendely，当时综合考虑挑了Endnote和Mendely，发现Endnote打开很麻烦，需要类似于新建工程的过程就立马放弃了。Mendely对我的好处主要是添加文件简单，只需拖拽文件，另外还云同步也方便(前提是有外网)。尽管这类文献管理软件在添加pdf文献时能够自动生成年份期刊文献等，但是也经常出现乱码的经常，相比于每次下载完还需要拖拽添加而言，这个优点不足为道。
## 2 VSCode的优势
下载即用，直接在VSCode打开相应文件夹，不需要额外的添加工作  
配合markdown在VSCode内分屏方便做笔记  
结合谷歌翻译插件悬停翻译和第三方的屏幕取词(有道、mac的三指取词)更加高效  
配合MEGA等实现本地云同步，多端操作更方便  
## 3 欲要实现，全靠插件
如何在VSCode添加插件请自行百度  
vscode-pdf：能够在VSCode内打开pdf文件  
<div align=center><img width="150" height="150" alt=Fig3.1 src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.1.png"/></div>  
Markdown Preview Github Styling：能够预览markdown
<div align=center><img width="150" height="150" alt=“Fig3.2” src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.2.png"/></div>   
预览markdown点击VSCode右上角，如图  
<div align=center><img width="150" height="150" alt=“Fig3.3” src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.3.png"/></div>   
Markdown PDF：能够将markdown输出为pdf等  
<div align=center><img width="150" height="150" alt=“Fig3.4” src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.4.png"/></div>  
markdown输出方法  
<div align=center><img width="150" height="150" alt=“Fig3.5” src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.5.png"/></div>  
Google Translate：能够对VSCode可编辑的文本进行翻译  
<div align=center><img width="150" height="150" alt=“Fig3.6” src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.6.png"/></div>  
谷歌翻译使用方法  
<div align=center><img width="150" height="150" alt=“Fig3.7” src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.7.png"/></div>    
开启悬停翻译在右下角，如何默认开启自行查阅，笔者觉得默认关闭较好  
<div align=center><img width="150" height="150" alt=“Fig3.8” src="https://github.com/JohnJim0816/notes/blob/master/blogs/VSCode%E5%AE%9E%E7%8E%B0%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86/Fig3.8.png"/></div>


