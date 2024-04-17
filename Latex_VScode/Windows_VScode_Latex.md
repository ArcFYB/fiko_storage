> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/weixin_45477628/article/details/130511209)

#### 使用VSCode借助TEXlive编写[Latex](https://so.csdn.net/so/search?q=Latex&spm=1001.2101.3001.7020)文档及常见Latex操作

* [引言](#_1)
* [个人配置](#_3)
* [电脑中安装Texlive编译器](#Texlive_5)
* [VSCode中安装插件](#VSCode_21)
* [VSCode中进行配置](#VSCode_46)
* * [更正](#_55)
* [Latex操作](#Latex_217)
* [参考链接](#_227)

引言
--

VSCode是微软开发的一款编辑器，插件很多，功能强大，不仅可以用来编写程序也可以用来写文档。为了节约磁盘空间，想把所有任务用一个软件完成，所以选用VSCode挑战一下。

个人配置
----

电脑：Win10（已[安装VSCode](https://so.csdn.net/so/search?q=%E5%AE%89%E8%A3%85VSCode&spm=1001.2101.3001.7020)）

电脑中安装Texlive编译器
---------------

LaTeX是一种基于[TeX](https://so.csdn.net/so/search?q=TeX&spm=1001.2101.3001.7020)的标记语言和编程语言，所以类似于其他编程语言Python等，Latex的文档也需要一个专门的编译器进行编译。我选择的是TexLive。  
在清华大学镜像网站中找到TeXlive镜像：  
[镜像网址链接](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)  
选择想要安装的版本，建议直接下载iso文件，这样可以离线安装。  
![选择想安装的版本(2023.05.05)](https://img-blog.csdnimg.cn/200c7272577c4ff7a7bc16b52b05192d.png)  
双击打开以后右键点击bat文件以管理员身份运行，开始安装  
![以管理员身份运行](https://img-blog.csdnimg.cn/821579c59452410e823d4fd20279d69b.png)  
个性化修改安装位置，不修改也可以，看个人  
![安装选项界面](https://img-blog.csdnimg.cn/f2553c5f134a45a99473d98bf98f3c32.png)  
编辑器如果要使用VSCode的话可以不用TeXworks前端。  
![取消勾选Texworks前端](https://img-blog.csdnimg.cn/3a6f8b84030b46968a842ceaad01cb83.png)  
安装完成后测试是否安装好。  
![安装完成](https://img-blog.csdnimg.cn/8a17d1bcba6d4f60a6dc7c00ed1d796f.png)  
输入指令`tex -v`测试是否安装完成  
![测试是否安装完成](https://img-blog.csdnimg.cn/b74a9d62301247198b9aa730e044d4b5.png)

VSCode中安装插件
-----------

在VSCode中安装Latex workshop插件。  
![Workshop插件](https://img-blog.csdnimg.cn/d3cd1cf8c7084780952f3382bae8d113.png)  
此时按说可以在VSCode中进行编写和查看了，比如：  
新建后缀为`.tex`的文件，然后写入以下内容：

```
`\documentclass[UTF8]{ctexart}
\begin{document}
你好，world!
\end{document}` 

*   1
*   2
*   3
*   4
```

如下图所示：  
![新建tex文件并写入内容](https://img-blog.csdnimg.cn/e8d04bdb7d0b4faab59edcfe9d45c39d.png)  
然后`ctrl+s`保存一下就可以看到文件夹内出现了一系列文件：  
![文件夹内出现文件](https://img-blog.csdnimg.cn/a08e9db848dd4969b75abdc637d2a01d.png)  
如果没有也可以使用页面右上角的蓝色`build`按钮，建立项目。  
![建立项目](https://img-blog.csdnimg.cn/807fd0319ee747f99a92fda1bcdb61e2.png)  
就可以生成`pdf`。  
![PDF内容](https://img-blog.csdnimg.cn/048279902419464292fc6c8bd6b79085.png)  
还有一种更快捷的方式就是在VSCode中打开侧边栏的`TEX`选项。  
![侧边TEX选项](https://img-blog.csdnimg.cn/7dbdcb0dd4574fc4baa7779d59e5c0d7.png)  
然后在`COMMANDS`栏目中点击`Build LaTeX project`就可以生成`pdf`，点击`View LaTeX PDF`就可以在侧边预览PDF。  
![细节图](https://img-blog.csdnimg.cn/9dbeb033e3b442178f0325bc0a39e3d5.png)  
在`.tex`文件中进行编写，然后保存就可以在侧边PDF中实时预览效果。  
当然仅有以上内容写文档可能只能满足初步要求，可能需要对VSCode中的插件选项进行配置。

VSCode中进行配置
-----------

VSCode中的设置按照控制的内容可以分为界面设置、编译器设置、插件设置；按照适用范围可以分为用户设置、工作空间设置、文件夹设置。  
用户设置（`User Settings`）就是对于任何文件都适用的；工作空间设置（`Workspace Settings`）就是对于工作空间内的文件适用的设置；文件夹设置（`Folder Settings`）就是对当前文件的环境进行配置。  
打开VSCode中的用户设置,可以通过`ctrl+,`，或者`File->Preference->settings`，或者通过`ctrl+shift+p`，然后输入`settings`打开用户设置，进行全局设置。  
对于工作区和文件夹设置一般是以文件夹形式存在的，比如对于一个文件夹想进行文件夹设置，需要在文件夹内建立一个`.vscode`文件夹，在里面写一些`.json`文件来进行文件夹设置的说明。有点类似于Python中把写好的程序作为包打包一样，需要写一个`__init__.py`文件来说明包含的内容。如下所示对TEST文件夹进行文件夹设置：  
![文件夹设置](https://img-blog.csdnimg.cn/3eea194366e54db3bd99f55cbf32e793.png)  
而WorkSpace的设置就是以`.code-workspace`结尾的文件，里面说明了与该工作区关联的文件夹以及相应的VScode配置信息。也就是在任意位置写一个后缀为`.code-workspace`的文件，说明界面、路径、编辑器、插件等设置内容然后双击这个文件就可以打开这个工作区。  
![工作区设置](https://img-blog.csdnimg.cn/ba0631966ac543ef922c5c4930f1a14d.png)  
如果要在工作区里禁用插件，需要先点击插件然后选择禁用(工作区)，关闭工作区需要点击`File->Close Workspace`。在文件夹内没有禁用插件功能。

### 更正

本部分内容参考：[texlive2023+vscode安装与配置（简洁版）](https://zhuanlan.zhihu.com/p/624932249)比较好。  
打开VScode中的设置文件，如下所示：  
![第一步](https://img-blog.csdnimg.cn/db82d56c53fd44eebec4616610bbd8b4.png#pic_center)  
然后打开`settings.json`  
![第二步](https://img-blog.csdnimg.cn/c55d80b539ed4dd0a39044567906cf6f.png#pic_center)  
![第三步](https://img-blog.csdnimg.cn/dbb774b37e594c0f9096f798ad76395b.png#pic_center)  
不过其中的内容需要注意，如果没有内容的话，可以全文替换；如果有内容，在原来内容的最后一句加上英文逗号以后再把配置粘贴进去，同时要注意缩进报错。

```
`//------------------------------LaTeX 配置----------------------------------
    // 设置是否自动编译
    "latex-workshop.latex.autoBuild.run":"never",
    //右键菜单
    "latex-workshop.showContextMenu":true,
    //从使用的包中自动补全命令和环境
    "latex-workshop.intellisense.package.enabled": true,
    //编译出错时设置是否弹出气泡设置
    "latex-workshop.message.error.show": false,
    "latex-workshop.message.warning.show": false,
    // 编译工具和命令
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
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
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
            "env": {}
        },

        {
            "name": "lualatex",
            "command": "lualatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-shell-escape",//这个命令行在网上的Latex Workshop设置里一般没有，所以直接recipe会报错
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
    // 用于配置编译链
    "latex-workshop.latex.recipes": [
        {
            "name": "PDFLaTeX",
            "tools": [
                "pdflatex"
            ]
        },
        {
            "name": "LuaLaTeX",
            "tools": [
                "lualatex"
            ]
        },
        {
            "name": "XeLaTeX",
            "tools": [
                "xelatex"
            ]
        },
        {
            "name": "BibTeX",
            "tools": [
                "bibtex"
            ]
        },
        {
            "name": "LaTeXmk",
            "tools": [
                "latexmk"
            ]
        },
        {
            "name": "xelatex -> bibtex -> xelatex*2",
            "tools": [
                "xelatex",
                "bibtex",
                "xelatex",
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
    ],
    //文件清理。此属性必须是字符串数组
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux",
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
    //设置为onFaild 在构建失败后清除辅助文件
    "latex-workshop.latex.autoClean.run": "onFailed",
    // 使用上次的recipe编译组合
    "latex-workshop.latex.recipe.default": "lastUsed",
    //使用 SumatraPDF 预览编译好的PDF文件
    // 设置VScode内部查看生成的pdf文件
    "latex-workshop.view.pdf.viewer": "tab",
    // PDF查看器用于在\ref上的[View on PDF]链接
    "latex-workshop.view.pdf.ref.viewer": "auto",
    "editor.renderControlCharacters": false` ![][img-0]
```

以上是手动对齐以后的内容。

Latex操作
-------

常见命令：  
![命令](https://img-blog.csdnimg.cn/a22b0c6308c8408890f01f266a924e4c.png#pic_center)  
常见环境命令：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/70a6dca9fff849189807c4b18da11747.png)  
至于使用什么宏包，参考：

1. [LaTeX 宏包（\usepackage)](https://blog.csdn.net/qq_37556330/article/details/106190148)
2. [LaTeX：数学公式](https://blog.csdn.net/weixin_39679367/article/details/109966436#:~:text=%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E7%94%A8%E5%88%B0%E7%9A%84%E4%B8%80%E4%BA%9B%E5%8C%85%EF%BC%9A%20usepackage%20%7Bamsmath%7D%20%25%20%E6%9C%80%E5%9F%BA%E6%9C%AC%E7%9A%84%E5%8C%85%20%25%20usepackage%20%5Bfleqn%5D,usepackage%20%7Bamsmath%2C%20amsfonts%2C%20amsthm%2C%20stackrel%2C%20amssymb%7D%20%25%20%E7%94%A8%E4%BA%8E%E6%8F%92%E5%85%A5%E5%85%AC%E5%BC%8F)

参考链接
----

* [使用VSCode编写LaTex](https://zhuanlan.zhihu.com/p/38178015)
* [最新版win10安装Texlive2022和Texstudio2022教程](https://blog.csdn.net/xiamuandsansan/article/details/124433788#:~:text=%E9%A6%96%E5%85%88%E8%BF%9B%E5%85%A5%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6%E5%BC%80%E6%BA%90%E8%BD%AF%E4%BB%B6%E9%95%9C%E5%83%8F%E7%BD%91%E7%AB%99%EF%BC%9A%20texlive%E4%B8%8B%E8%BD%BD%20%E7%BD%91%E7%AB%99%E5%9C%B0%E5%9D%80%EF%BC%9A%20https%3A%2F%2Fmirrors.tuna.tsinghua.edu.cn%2FCTAN%2Fsystems%2Ftexlive%2FImages%2F%20%E4%B8%8B%E8%BD%BD%E4%B8%8A%E5%9B%BE%E4%B8%AD%E7%9A%84,texlive2022.iso%20%E4%B8%8B%E8%BD%BD%E5%AE%8C%E5%AE%89%E8%A3%85%E5%8C%85%E4%B9%8B%E5%90%8E%E8%A7%A3%E5%8E%8B%20%E9%80%89%E6%8B%A9%E4%B8%8A%E5%9B%BE%E4%B8%AD%E7%9A%84install-tl-windows%E5%8F%B3%E9%94%AE%20%E4%BB%A5%E7%AE%A1%E7%90%86%E5%91%98%E8%BA%AB%E4%BB%BD%E8%BF%90%E8%A1%8C%20%E6%8E%A5%E4%B8%8B%E6%9D%A5%E5%8F%AF%E4%BB%A5%E4%BF%AE%E6%94%B9%E5%AE%89%E8%A3%85%E8%B7%AF%E5%BE%84%EF%BC%8C%E7%84%B6%E5%90%8E%E7%82%B9%E5%87%BB%20%E5%AE%89%E8%A3%85)
* [基于VSCode搭建LaTeX写作环境](https://zhuanlan.zhihu.com/p/103355604)
* [VSCode中的设置](https://app.yinxiang.com/fx/87ffd347-dfcf-4611-a247-0c883637afec)
* [【VS Code】文件夹（Folder）和工作区（Workspace）的使用](https://blog.csdn.net/myRealization/article/details/118385489)
* [关于VSCode中工作区的讲解与使用工作区还你一个轻量的VSCode](https://zhuanlan.zhihu.com/p/54770077)

[img-0]:data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAgCAMAAABemGpIAAAA51BMVEUAAAD///9/f/+qqqp/f7+SkpJ/f5+AgJl/f5V/f5J/f46AgIyAgIt7e457e418fIt4eI54eI58fIl9fYh6eop6eop7e4l5eYt7e4h4eIt6eoh3eoh5eYl6eoh3eot5eYl4eop3eYh5eYl4eop4eIl3eYp4eol4eIl4eIl4eIl3eYl4eIh4eYl4eIl4eIh4eYl4eYl3eYl3eIl4eYh3eYl3eYl4eYl4eIh3eIh4eYl4eYh4eYh4eIh4eYl3eIl4eYh4eYh4eYh4eIh3eIh3eIl3eIl4eYh3eIl4eYh3eIl4eYh3eIl3eIhMcpwIAAAATHRSTlMAAQIDBAcICgwOEhQWGx0hIiQnKzAyNjk6REdLUFZcY2RpcHF5foSIioyNjpOZnaCirba5ur7EztLT19vf4uPk6uzu8PL09/j5+v3+H2iShQAAAL1JREFUGBntwWlTQWEAhuEnCm+WtJeILHGONm1KobIU7v//e3rHNE0nR3wz07guLf0PpupE5SvqukZeLjT35GO/BY68qsDHiSYUBoArL3OLdRWWh6lh3Rj9EjgdAQ+b+mHnCRiWApp09AZ00vqW7QMvh/K1UQdG5aDGwpdY93FNEbrAuovJ2nrEclY1Xe4daB9ImS7QSetPu8/AIH+GVU9qhvVrvpyvaaaV0hCrd6y5pF6hsa05JSrFiJYW5xOvCyNP+hx2EAAAAABJRU5ErkJggg==