# 复旦自动刷锻脚本

使用复旦智慧体育小程序的 API 实现自动刷锻。

**GitHub Actions 因为运行时间过长，占用服务器资源，因此被禁用。没有计算机基础的同学请直接参考教程一节。**

## 使用

本节仅供本地配置有 Python 运行环境的用户使用。没有安装 Python 的用户请参考教程。

- 安装依赖：`pip install -r requirements.txt`
- 修改 `settings.json` 文件中的 `USER_ID, FUDAN_SPORT_TOKEN` 变量，需要在小程序内抓包获得，详请查看“抓包教程”章节。
- 查看刷锻路线列表：`python main.py --view`
- 自动刷锻：`python main.py --route <route_id>`，其中 `route_id` 是刷锻路线列表中的 ID。
- 可以设置里程和时间，如 `--distance 1200 --time 360`，更多选项请使用 `python main.py --help` 查看。
- （附加）环境变量 `PLATFORM_OS, PLATFORM_DEVICE` 可以设置刷锻的设备标识，默认值为 `iOS 2016.3.1`
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

### 运行教程

获取到 User ID 和 Token 后，按照下文的说明本地运行脚本。

点击页面右侧的 Release 链接（带有绿色 Latest 标签），然后在页面下方的 Assets 中选择一个下载。Windows 系统下载 `windows.zip`
，macOS 系统下载 `macos.zip`。下载后，解压得到一个 `main` 文件夹。

#### Windows

1. 打开下载好的 `main` 文件夹，右键单击文件 `settings.json`，打开方式 - 记事本。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/81a1a320-3d85-4236-a204-4380ee4545ea)

2. 将文件中 `USER_ID` 和 `FUDAN_SPORT_TOKEN`
两项后面的内容改成刚刚抓包抓到的值（保留引号），然后保存并关闭窗口。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/810afd57-43ff-4904-86a2-1865b6564b31)

3. 按快捷键 `Win + R`，输入 `cmd` 回车，会打开一个黑色窗口。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/76d4305f-c938-4b23-bb78-dd2390179e9f)

4. 输入 `cd + [空格]`，然后把 `main` 文件夹拖拽到黑色窗口内，按回车。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/3c7ab9db-9212-468b-b50b-c8f92538308e)

5. 依次输入以下命令（命令输入完成后按回车执行）：
   - `.\main.exe -v` （查看所有可以刷锻的路径）
   - `.\main.exe -r [id]`（`id` 是你要刷锻的路径编号，在下图中为 33，意思是南区田径场课外活动，图里不在刷段时间，如果在刷段时间是可以正常刷锻的）

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/aacd8fc6-4bb0-4b40-bf11-ae7837bba047)


#### macOS

1. 打开下载好的 `main` 文件夹，右键单击文件 `settings.json`，打开方式 - 文本编辑。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/0a1557d3-e858-4d7d-b37e-ce7b8a59d0cc)

2. 将文件中 `USER_ID` 和 `FUDAN_SPORT_TOKEN`
两项后面的内容改成刚刚抓包抓到的值（保留引号），然后保存并关闭窗口。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/f7686126-0361-4e2d-bc71-8a8ad228a91a)

3. 按快捷键 `Command + [空格]`，输入「终端」，然后打开终端 App，是一个黑色/白色的窗口。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/515e7c36-437a-4c80-834b-7d59388ed1aa)

4. 输入 `cd + [空格]`，然后把 `main` 文件夹拖拽到窗口内，按回车。

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/bb0c16e1-ea9a-436a-8114-6fb492d407a9)

5. 依次输入以下命令（命令输入完成后按回车执行）：
   - `chmod +x ./main` （只有第一次执行要输入，之后无须输入）
   - `./main -v` （查看所有可以刷锻的路径）
   - `./main -r [id]`（`id` 是你要刷锻的路径编号，在下图中为 33，意思是南区田径场课外活动）

![](https://github.com/fsy2001/fudan-sport-automator/assets/55231108/85f64e7e-5f2e-4c52-9899-8172f79a9cbc)

### 反馈与讨论

如果在使用过程中遇到了问题，或者希望提出建议，请点击页面顶部的 Discussions - New Discussion，选择一个类别，并描述你的问题。

如果你**确信**脚本有 Bug，可以点击页面顶部的 Issue - New Issue 来新建一个 Issue。

## 致谢

感谢 [@habacat](https://github.com/habacat) 提供的小程序源码




