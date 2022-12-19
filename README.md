# 数学小工具

这是一组为高等数学作业而制作的数学小工具

使用 SymPy 进行符号计算

## 支持的数学功能

- 求导
- 求极限
- 求积分
- 泰勒展开
- 解方程
- 绘图
- 表达式求值

## 辅助工具

- 命令翻译器 (简化命令的输入)
- 运行工具 (提供对用户更加友好的操作方式)

## 系统要求

### 基础计算

- 推荐
  - Windows 11
  - Windows 10
  - GNU/Linux
- 支持
  - Android + Termux
  - MacOS
- 已终止支持
  - Windows 7
  - Windows Vista

### 绘图

- 推荐
  - Windows 11
  - Windows 10
- 支持
  - GNU/Linux
  - MacOS
- 已终止支持
  - Windows 7
  - Windows Vista

### 命令翻译器

- 推荐
  - Windows 11
  - Windows 10
- 已终止支持
  - Windows 7
- 需要修改
  - GNU/Linux
  - MacOS

### 运行工具

- 推荐
  - Windows 11
  - Windows 10
- 已终止支持
  - Windows 7
- 需要修改
  - GNU/Linux
  - MacOS 

## 依赖项

### [Python](https://www.python.org/)

Python解释器，是运行软件所必需的

推荐版本: 3.11 或 3.10

可以从 Microsoft Store 获取，不需要调整环境变量

也可以通过其他方式安装，可能需要调整环境变量

### [SymPy](https://www.sympy.org/)

用于符号计算，是实现基本功能所必需的

可以使用`pip`安装

`pip install sympy`

SymPy的依赖项在安装时会自动被安装。

### [Matplotlib](https://matplotlib.org/)

用于绘图，如果需要使用绘图功能则推荐安装

如果没有安装绘图用软件包，绘图功能将以字符画的形式实现

可以使用`pip`安装

`pip install matplotlib`

Matplotlib的依赖项在安装时会自动被安装。

### [Anaconda](https://www.anaconda.com/)

Anaconda 包括了 Python, SymPy, Matplotlib

如果已经安装了Anaconda，则不需要安装前面的三项

可以从其网站获取

需要调整环境变量使其Python解释器在Path路径内

### [.NET 6](https://dotnet.microsoft.com/)

运行命令翻译器和运行工具所需

.NET 7 或许也可以

若只是运行命令翻译器或运行工具，则只需要运行时

若要编译命令翻译器，则可能需要SDK

可以从Microsoft的网站[下载](https://dotnet.microsoft.com/download)

### [Windows Powershell](https://learn.microsoft.com/powershell/)

运行命令翻译器和运行工具所需

此软件一般已经预装在Windows中

如果使用 GNU/Linux 或 macOS 并且想使用命令翻译器，请尝试将 math.csx 第40行的`powershell`改成`pwsh`，并安装 Powershell

如果使用 GNU/Linux 或 macOS 并且还想使用运行工具，你需要对 mathIn.ps1 第6行进行适当修改

### [Visual Studio Code](https://code.visualstudio.com/)

这是运行工具调用的文本编辑器

可以通过修改 mathIn.ps1 修改使用的文本编辑器

可以从 Microsoft Store 获取

## 安装方法

### 安装 Python

如果运行以下命令，能正常显示Python版本，则Python已安装

`python --version`

（输出示例：`Python 3.11`，输出随Python版本变化）

从 Microsoft Store 获取即可

- [Python 3.11](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K)
- [Python 3.10](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)
- [Python 3.9](https://apps.microsoft.com/store/detail/python-39/9P7QFQMJRFP7)
- [Python 3.8](https://apps.microsoft.com/store/detail/python-38/9MSSZTT1N39L)
- [Python 3.7](https://apps.microsoft.com/store/detail/python-37/9NJ46SX7X90P)

或者从[python.org](https://www.python.org/)获取

### 安装 SymPy 和 Matplotlib

可以通过以下命令列出已安装的Python软件包

`pip list`

运行以下命令安装SymPy和Matplotlib

`pip install sympy`

`pip install matplotlib`

### 获取数学工具（不含编译好的命令翻译器）

#### 方法1：下载压缩包

在页面的上部找到绿色的 Code 按钮，然后点击下拉列表的最后一项 Download ZIP

#### 方法2：通过 Git 获取

假设需要把工具安装在 `<path>/MathTools`

1. `cd <path>`
2. `git clone https://github.com/HPLZH/MathTools.git`

##### 附：安装 Git

如果运行以下命令，能正常显示Git版本，则Git已安装

`git --version`

（输出示例：`git version 2.39.0.windows.1`，输出随Git版本变化）

运行以下命令安装Git

`winget install --id Git.Git -e --source winget`

### 安装 .NET 6

可以通过以下命令列出.NET安装信息

`dotnet --info`

运行以下命令安装 .NET 6 Runtime

`winget install Microsoft.DotNet.Runtime.6`

运行以下命令安装 .NET 6 SDK

`winget install Microsoft.DotNet.SDK.6`

### 获取命令翻译器

#### 方法1：下载二进制文件

在页面右侧找到 Releases, 下载最新版本

然后将其中的文件解压到 MathTools 文件夹

注意，解压时应该解压到`.../MathTools/`而不是`.../MathTools/math/`

#### 方法2：使用 dotnet-script 编译

在安装了 dotnet-script 之后使用 math_build.cmd 编译

##### 附：安装 dotnet-script

如果运行以下命令，能正常显示dotnet-script版本，则dotnet-script已安装

`dotnet script --version`

（输出示例：`1.4.0`，输出随dotnet-script版本变化）

运行以下命令安装（需要 .NET 6 SDK）

`dotnet tool install dotnet-script -g`

## 使用说明

### 数学命令的参数

| 功能       | 命令名称      | 参数               |
|:--------:|:---------:|----------------|
| 求导数      | diff      | x                |
| 求导函数     | diff      |                  |
| 求n阶导数    | diffn     | n x              |
| 求n阶导函数   | diffn     | n                |
| 求极限      | lim       | x                |
| 求左极限      | lim       | x -              |
| 求右极限      | lim       | x +              |
| 求不定积分    | integrate |                  |
| 求定积分     | integrate | a ~ b            |
| 求泰勒多项式   | series    | n x<sub>0</sub>  |
| 求麦克劳林多项式 | series    | n                |
| 解单个方程    | solve     |                  |
| 求解集      | solveset  |                  |
| 绘图（默认范围） | draw      |                  |
| 绘图（a~b）  | draw      | a b              |
| 求函数值     | fx        | x                |
| 计算       | calc      |                  |

### Python

用法：

`python -m <name> [funcs] [args]`

`<name>` : 命令名称

`[func]` : 可选，要处理的函数表达式

`[args]` : 参数

例：`python -m lim "sin(x)/x" "cos(x)" 0`

要处理的函数表达式可以通过管道传入，例如：

`Write-Output "sin(x)/x" | python -m lim 0`

多个命令可以串联执行：

`Write-Output "sin(x)" | python -m diff | python -m lim 0`

### 命令翻译器

令 `command` = `<name> [funcs] [args]`

`<name>` : 命令名称

`[func]` : 可选，要处理的函数表达式（正常情况下不要使用）

`[args]` : 参数

用法：

`./math [funcs] <command> [command ...]`

`./math.exe [funcs] <command> [command ...]`

`dotnet script ./math.csx -- [funcs] <command> [command ...]`

`[func]` : 可选，要处理的函数表达式

例：`./math "sin(x)" "cos(x)" diffn 2 lim 0`

要处理的函数表达式可以通过管道传入，例如：

`Write-Output "sin(x)" "cos(x)" | ./math diffn 2 lim 0`

多个命令可以串联执行，但没有这个必要

### 运行工具

双击运行`mathIn.cmd`

然后控制台窗口中出现 `Command : `

然后输入命令，语法类似于命令翻译器：

`Command : <command> [command ...]`

例：`Command : diffn 2 lim 0`

（开头的`Command : `是程序输出的，不需要输入）

按下 Enter 完成输入后，在新打开的 VS Code 窗口中输入要处理的函数表达式，一行一个

在关闭 VS Code 窗口后，等待一小段时间，然后在新打开的 VS Code 窗口中查看结果
