# 数学小工具

这是一组为高等数学作业而制作的数学小工具

## 支持的数学功能

- 求导
- 求极限
- 泰勒展开
- 解方程
- 绘图
- 表达式求值

## 辅助工具

- 命令翻译器 (简化命令的输入)
- 运行工具 (提供对用户更加友好的操作方式)

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

### .NET 6

运行命令翻译器和运行工具所需

.NET 7 或许也可以

若只是运行命令翻译器或运行工具，则只需要运行时

若要编译命令翻译器，则可能需要SDK

可以从Microsoft的网站[下载](https://dotnet.microsoft.com/download)

### Windows Powershell

运行命令翻译器和运行工具所需

此软件一般已经预装在Windows中

如果使用 GNU/Linux 或 macOS 并且想使用命令翻译器，请尝试将 math.csx 第40行的`powershell`改成`pwsh`，并安装 Powershell

如果使用 GNU/Linux 或 macOS 并且还想使用运行工具，你需要对 mathIn.ps1 第6行进行适当修改

## 使用说明

未完待续
