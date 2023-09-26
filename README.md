# 复旦自动刷锻脚本

使用复旦智慧体育小程序的 API 实现自动刷锻。
**请自行承担使用第三方软件刷锻的风险**

**GitHub Actions 因为运行时间过长，占用服务器资源，因此被禁用。没有计算机基础的同学请直接参考教程一节。**

## 使用

本节仅供本地配置有 Python 运行环境的用户使用。没有安装 Python 的用户请参考教程。

1. 安装依赖：`pip install -r requirements.txt`
1. 修改 `settings.json` 文件中的 `USER_ID, FUDAN_SPORT_TOKEN` 变量，需要在小程序内抓包获得，详请查看“抓包教程”章节。
1. 查看刷锻路线列表：`python main.py --view`
1. 自动刷锻：`python main.py --route <route_id>`，其中 `route_id` 是刷锻路线列表中的 ID。
1. 可以设置里程和时间，如 `--distance 1200 --time 360`，更多选项请使用 `python main.py --help` 查看。
1. （附加）环境变量 `PLATFORM_OS, PLATFORM_DEVICE` 可以设置刷锻的设备标识，默认值为 `iOS 2016.3.1`
  、`iPhone|iPhone 13<iPhone14,5>`。

## 说明

目前支持的场地有菜地、南区田径场和江湾田径场。

## 教程

在运行前，需要抓包获取 User ID 和 Token。

### 抓包教程

#### iOS 系统

抓包教程可参考 [使用 Stream 抓包](https://www.azurew.com/%e8%bf%90%e7%bb%b4%e5%b7%a5%e5%85%b7/8528.html)
，抓包软件可在 [App Store](https://apps.apple.com/cn/app/stream/id1312141691) 下载。

按照教程内的指引配置到设置证书的步骤，然后在软件内点击 Sniff Now 按钮，打开刷锻小程序刷新一下（确保小程序已经登录），再回到
Stream，点击 Stop Sniffing，然后点击 Sniff
History，选择最近的一条记录，点开后找到开头为 `GET https://sport.fudan.edu.cn/sapi` 的任意一条记录，点进去选择 Request，在
Request Line 中有 `userid=xxx&token=xxx` 的记录，记下这两段信息。

#### Windows 系统

可参考 [教程](https://juejin.cn/post/6920993581758939150/) 进行相应设置。注意：需要把 Fidder 中 HTTPS 部分设置的复选框由
from browers only 改为 from all processes。

在配置完后，微信登录，右上角齿轮进入代理，端口为 127.0.0.1，端口号为 8888（默认）
登录后进入小程序并登录，在 Fiddler 里找到下图中的 ID 和 token
![image](https://user-images.githubusercontent.com/51439899/226794395-42eca333-fb65-4e29-a2cb-b8ce3fd13221.png)

**注意，目前 Token 的有效期为 3 天。**

获取到 User ID 和 Token 后，按照下文的说明本地运行脚本。

### 运行教程

点击页面右侧的 Release 链接（带有绿色 Latest 标签），然后在页面下方的 Assets 中选择一个下载。Windows 系统下载 `windows.zip`
，macOS 系统下载 `macos.zip`。下载后，解压得到一个 `main` 文件夹。

#### Windows

打开 `main` 文件夹，右键单击文件 `settings.json`，打开方式 - 记事本，然后将其中 `USER_ID` 和 `FUDAN_SPORT_TOKEN`
两项后面的内容改成刚刚抓包抓到的值（保留引号）。

按快捷键 `Win + R`，输入 `cmd` 回车，会打开一个黑色窗口。输入 `cd + [空格]`，然后把 `main` 文件夹拖拽到黑色窗口内，按回车。

- 输入命令 `.\main.exe -v` 并按回车，可以查看刷锻路线列表。
- 输入命令 `.\main.exe -r 28` 并按回车，可以开始刷锻。需要参考上面一条命令的输出，把 28
  替换成你需要的数字。这条命令需要执行数分钟，执行结束后会输出 `FINISHED: ***` 字样。

#### macOS

打开 `main` 文件夹，右键单击文件 `settings.json`，打开方式 - 文本编辑，然后将其中 `USER_ID` 和 `FUDAN_SPORT_TOKEN`
两项后面的内容改成刚刚抓包抓到的值（保留引号）。

按快捷键 `Command + [空格]`，输入「终端」，然后打开终端 App，是一个黑色/白色的窗口。输入 `cd + [空格]`，然后把 `main`
文件夹拖拽到窗口内，按回车。

- 输入命令 `./main -v` 并按回车，可以查看刷锻路线列表。
- 输入命令 `./main -r 28` 并按回车，可以开始刷锻。需要参考上面一条命令的输出，把 28
  替换成你需要的数字。这条命令需要执行数分钟，执行结束后会输出 `FINISHED: ***` 字样。
- 如果出现 `permission denied` 报错，则输入命令 `chmod +x ./main` 并按回车，然后重新执行命令。

### Issue

如果在使用过程中遇到了问题，请点击页面顶部的 Issue - New Issue，并在出现的文本框中描述你的问题。

## 致谢
[@habacat](https://github.com/habacat)提供的小程序源码
