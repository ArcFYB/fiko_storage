原文地址 [blog.csdn.net](https://blog.csdn.net/Hacker_MAI/article/details/130334821)

#### Ubuntu 20.04 安装 [Latex](https://so.csdn.net/so/search?q=Latex&spm=1001.2101.3001.7020) 并使用 vscode 作为文本编辑器

*   [1 Texlive 下载与安装](#1_Texlive___22)
*   *   [1.1 镜像文件下载](#11__24)
    *   [1.2 安装步骤](#12__28)
    *   [1.3 查看是否安装成功](#13__80)
    *   [1.4 相关依赖安装](#14__104)
*   [2 安装 windows 字体](#2__windows__116)
*   [3 vscode 编辑与编译环境配置](#3_vscode__150)
*   *   [3.1 vscode 安装](#31_vscode__152)
    *   [3.2 编辑相关插件安装](#32__162)
    *   [3.3 编译环境配置](#33__169)
    *   [附录：](#_277)

* * *

因为笔者有在 Ubuntu 下进行 Latex 编写的需求，因此在安装完成后以此为作为笔记，方便各位以及笔者后续作为参考。本文主要解决的问题如下：

1.  Ubuntu 下进行 Latex 的安装
2.  Ubuntu 下安装 Windows 下的字体以提供更加丰富的字体支持
3.  配置 vscode 的编辑与编译环境

* * *

测试时间：2023年4月24日

测试系统：Ubuntu 20.04

安装版本：texlive2023

1 [Texlive](https://so.csdn.net/so/search?q=Texlive&spm=1001.2101.3001.7020) 下载与安装
----------------------------------------------------------------------------------

### 1.1 镜像文件下载

进入 Texlive [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)，下载 texlive2023.iso；

### 1.2 安装步骤

下载完成后双击 .iso 镜像文件进行挂载，挂载后终端进入 .iso 目录执行如下命令进行安装
```
sudo perl ./install-tl --no-interaction
```

等待安装完成，相关安装路径为

```
/usr/local/texlive/YYYY/bin/PLATFORM
e.g., /usr/local/texlive/2024/bin/x86_64-linux
```

在安装命令的终端输出结尾会输出如下路径

```
Add /usr/local/texlive/2024/texmf-dist/doc/man to MANPATH.
Add /usr/local/texlive/2024/texmf-dist/doc/info to INFOPATH.
Most importantly, add /usr/local/texlive/2024/bin/x86_64-linux
to your PATH for current and future sessions.
```

进一步将 texlive 添加到环境变量中

```
sudo gedit ~/.bashrc
```

在 .bashrc 文件的末尾添加如下代码

```
export PATH=/usr/local/texlive/2023/bin/x86_64-linux:$PATH
export MANPATH=/usr/local/texlive/2023/texmf-dist/doc/man:$PATH
export INFOPATH=/usr/local/texlive/2023/texmf-dist/doc/info:$PATH
```

完成环境变量的添加后重新加载 .bashrc 文件

```
source ~/.bashrc
```

完成上述步骤后，进行设备重启

```
sudo reboot
```

### 1.3 查看是否安装成功

打开终端命令行键入如下命令

```
tex --version
```

终端返回输出：

```
TeX 3.141592653 (TeX Live 2023)
kpathsea version 6.3.5
Copyright 2023 D.E. Knuth.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the TeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the TeX source.
Primary author of TeX: D.E. Knuth.
```

至此， texlive 的安装完成。

### 1.4 相关依赖安装

打开新的终端，键入如下命令下载相关依赖支持

```
sudo apt-get install texlive-latex-extra
sudo apt-get install texlive-latex-recommended
sudo apt-get install texlive-science
```

2 安装 windows 字体
---------------

首先在 windows 下进入 C 盘下的 C:/windows/Fonts 下将需要的字体拷贝出来，放到新建的文件夹中

下一步将拷贝出来的字体文件通过 U 盘拷贝至 Ubuntu 下

在 Ubuntu 的计算机存储下新建目录用于存储字体

```
sudo mkdir /usr/share/fonts/winfonts
```
将 windows 系统下的字体拷贝到刚刚创建的 winfonts 目录下
```
sudo chmod 644 /usr/share/fonts/winfonts/*
```

刷新缓存字体

```
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fsv
```

查看系统中安装的中文字体

```
fc-list :lang=zh | sort
```

3 vscode 编辑与编译环境配置
------------------

### 3.1 vscode 安装

vscode 进入对应官网下载 deb 包进行安装即可，[点击](https://code.visualstudio.com/)访问官网

完成 vscode 的安装后，可在终端中键入如下命令启动 vscode

```
code
```

### 3.2 编辑相关插件安装

进入 vscode， 通过快捷键 ctrl+shift+x 打开插件面板，搜索关键词 latex，安装

![在这里插入图片描述](https://img-blog.csdnimg.cn/4277cf75810049c4bea0f2c05f8bc956.png#pic_center)

### 3.3 编译环境配置

完成安装后进一步设置编译环境，通过快捷键 ctrl+shift+p 打开快捷访问，输入打开工作区设置

![在这里插入图片描述](https://img-blog.csdnimg.cn/c9a2325cdfcf4f3592eb30f0de8f1e3e.png#pic_center)

```
{
    "latex-workshop.latex.autoBuild.run":"onSave",
    "latex-workshop.latex.autoBuild.interval":10000,
    "latex-workshop.latex.recipes": 
    [
        {
            "name": "xelatex",
            "tools": 
            [
                "xelatex"
            ]
        },
        {
            "name": "pdflatex",
            "tools":
            [
                "pdflatex"
            ]
        },
        {
            "name": "xelatex(double)",
            "tools": 
            [
                "xelatex",
                "xelatex"
            ]
        },
        {
            "name": "xe->bib->xe(double)",
            "tools": 
            [
                "xelatex",
                "bibtex",
                "xelatex",
                "xelatex"
            ]
        }
    ],
    "latex-workshop.latex.tools": 
    [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": 
            [
                "-synctex=1",
                "-interaction=nonstopmode",
               
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": 
            [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
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
    "latex-workshop.latex.autoClean.run": "onBuilt",//这个其实可要可不要.
    "latex-workshop.latex.clean.fileTypes": [//事实上写个makefile直接make clean就好了
        "*.aux", //而且万一编译错误的话这些文件都会被清除，log文件里面的报错信息也没了
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log",
        "*.fdb_latexmk"
    ],
```

### 附录：

[Ubuntu(20.04 LTS) OS 下 VS Code + LaTeX 快速配置指南](https://zhuanlan.zhihu.com/p/136209984)

[Latex 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)

[texlive Unix/GNU/Linux Install](https://www.tug.org/texlive/quickinstall.html)

[Ubuntu14.04系统下VSCode+Latex遇到问题及相应解决方法，ubuntu14.04vscode](http://www.wld5.com/vscode/15634.html)

[【转】ubuntu添加windows字体](http://lixiang7.lofter.com/post/1b42fc_92cc85)

[Ubuntu 20.04 系统环境下配置LaTeX环境（正反向搜索）](https://zhuanlan.zhihu.com/p/492965557)

[Ubuntu下添加 Latex 添加 .sty 文件](https://blog.csdn.net/gengli2017/article/details/86593360)

[FandoIKai-Regular 字体下载](https://github.com/loveencounterflow/jizura-fonts/blob/master/fonts/FandolKai-Regular.otf)

[解决Ubuntu下latex编译缺少中文字体的错误](https://blog.csdn.net/u014454538/article/details/104503211)