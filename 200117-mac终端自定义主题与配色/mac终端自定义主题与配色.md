## 1 确定脚本环境
主要用的多是两种，一种bash是mac和linux终端默认的脚本环境，网上关于终端配色涉及```source .bash_profile```都是在bash脚本下，另一种是zsh，对应```source .zshrc```，据说挺好用但是配色往往跟item2配合起来，笔者暂时比较菜只考虑bash。

首先查看当前终端脚本环境```echo $SHELL```，返回```/bin/bash```说明是bash环境，默认一般是，怎么更改默认脚本环境参考[简书](https://www.jianshu.com/p/3b0c3cfc4267)。
## 2 更换图式scheme
推荐一个[github](https://github.com/mbadolato/iTerm2-Color-Schemes)上有丰富的主题，各终端主题可在主页预览，打开terminal文件夹选择中意的.terminal文件，怎么下载github的单独文件可以使用chrome浏览器的扩展程序**Octo Mate**。下载好之后之前双击就可以看见改变后的终端，此时在终端的偏好设置-描述文件将添加的terminal主题设置默认即可。注意此时只是更改了终端的背景以及字体统一颜色而已，并不能显示不同颜色。
## 3 主题与配色
这个很多博客上有，笔者也不挑参考了一个[CSDN](https://blog.csdn.net/u011635492/article/details/84374325)，打开终端，然后```open .bash_profile```，将以下内容粘贴：
```bash
# Tell ls to be colourful
export CLICOLOR=1
export LSCOLORS=Exfxcxdxbxegedabagacad
 
# Tell grep to highlight matches
export GREP_OPTIONS='--color=auto'

export TERM="xterm-color"
# 这个比较普通
# PS1='\[\e[0;33m\]\u\[\e[0m\]@\[\e[0;32m\]\h\[\e[0m\]:\[\e[0;34m\]\w\[\e[0m\]\$ '
# 下面加了表情
# PS1='\[\033[01;36m\]\u😎 \[\033[01;33m\]\h \[\033[01;35m\]\t \[\033[01;31m\]\W\$ \[\033[00m\]😛 '
# 去掉时间
# PS1='\[\033[01;36m\]\u😎 \[\033[01;33m\]\h\[\033[01;31m\]\w\\$ \[\033[00m\]😛 '
# 去掉时间和电脑名字，本人采用
PS1='\[\033[01;36m\]\u😎 \[\033[01;31m\]\w\\$ \[\033[00m\]😛 '
```
然后```source .bash_profile```生效，到此完结。
贴上一张效果图XD:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200116155439214.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5KaW0w,size_16,color_FFFFFF,t_70)
## 4 关于zsh终端的配置
最后还是真香了选择zsh终端，另外注意mac catalina默认是zsh而不是bash，首先切换为zsh脚本环境，具体参考第1节，然后参考[简书](https://www.jianshu.com/p/60a11f762f62)安装oh-my-zsh，注意简书说的主题指的这里的配色，简书说的配色是指这里的主题。下面给出最简步骤，不需要下载item2
### 4.1 安装oh-my-zsh
笔者直接用curl安装
```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
安装好之后会自动生成.zshrc文件。
### 4.2 主题与配色
终端```open .zshrc```打开，把默认的```ZSH_THEME="robbyrussell"```更换成别的theme，theme安装在```~/.oh-my-zsh/themes```路径下，笔者自己新建了一个my.zsh-theme文件，然后改成了```ZSH_THEME="my"```，具体配置如下：
```python
## based on murilasso
local return_code="%(?..%{$fg[red]%}%? ↵%{$reset_color%})"
local user_host='%{$terminfo[bold]$fg[green]%}%n@%m%{$reset_color%}'
local current_dir='%{$terminfo[bold]$fg[blue]%}%~%{$reset_color%}'
local rvm_ruby='%{$fg[red]%}$(rvm_prompt_info || rbenv_prompt_info)%{$reset_color%}'
local git_branch='%{$fg[blue]%}$(git_prompt_info)%{$reset_color%}'

# emoj can be found on https://emojipedia.org/grinning-face-with-one-large-and-one-small-eye/
# PROMPT="${user_host}😎 :${current_dir}${rvm_ruby}${git_branch}%b $%b 🤪 "
PROMPT="😎 :${current_dir}${rvm_ruby}${git_branch}%b $%b 🤪 "
RPS1="${return_code}"

ZSH_THEME_GIT_PROMPT_PREFIX=""
ZSH_THEME_GIT_PROMPT_SUFFIX=""
ZSH_THEME_GIT_PROMPT_DIRTY=" %{$fg[red]%}✗%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN=" %{$fg[green]%}✔%{$reset_color%}"
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200116174056317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5KaW0w,size_16,color_FFFFFF,t_70)