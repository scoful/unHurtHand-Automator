# unHurtHand-Automator

## 背景介绍

自娱自乐学习python的副产品，不伤手自动任务系列，自动有风险，入坑需谨慎。

**PS1：据说阿里大大有风控的，99 划算节养章鱼用脚本的最后满级分到 1 分或者 1 毛，so只适用于个人偷懒，交流学习**

**PS2：本project的诞生离不开 UIAutomator2 ，一个 Python 封装的安卓自动化测试库，比原生 adb shell 命令强大得多，方便得多，一个强大的轮子。**

**PS3：本项目仅在分辨率为 1080X1920 的 9:16 的设备下测试过，其他设备不保证**

**PS4：欢迎看到的朋友推荐一下还有哪些可以做自动任务的，一起搞搞**

## 实现功能
1. 蚂蚁森林，支持支付宝版本：10.1.80.8050,最新的10.1.82.9020已经不支持了，等更新下一版看看吧，每次更新都有变化
   - 收集自己的能量
   - 收集好友的能量
2. 2019双11支付宝app上的全民开喵铺
   - 自动收取喵币
   - 自动升级领红包
   - 自动签到
   - 对以下任务自动操作
     - <去浇水>任务
     - <去浏览>任务
     - <去完成>任务
3. 2019双11淘宝app上的全民开喵铺
   - 自动收取喵币
   - 自动升级领红包
   - 自动签到
   - 对以下任务自动操作
     - <去浏览>任务
     - <去签到>任务
     - <去查看>任务
   - 自动拆红包
4. 支付宝-领积分，支持支付宝版本：10.1.82.9020
    - 自动领积分

## 安装与运行

### pc端

- 如果你没有安装 Python，请先安装 [Python3.*](https://www.python.org/downloads/) 以上版本

- 如果你没有安装 adb，请先安装，以下是adb官方介绍
  - Android 调试桥 (adb)，https://developer.android.google.cn/studio/command-line/adb
  - 官方下载地址，[adb下载](https://developer.android.google.cn/studio/releases/platform-tools.html)，下载后，把解压后的文件夹的路径添加到环境变量的 `Path` 中，方便全局调用

- 以上都安装后，下载本项目代码到本地，进入根目录，打开 `CMD` 或者 `Powershell` 或是其他任何终端，执行以下命令，安装python依赖：

  ```python
  # 打开终端
  # 以下是一整行
  python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
  ```

- adb调试有2种连接安卓手机的方式，一种usb直连，一种pc和安卓手机处于同一wifi局域网的条件下用wifi连接。具体的操作可参考，[官方介绍](https://developer.android.google.cn/studio/command-line/adb)

- adb连接成功后，获取 device 名称，并填写至 main.py：

  ```powershell
  # 终端上执行以下命令，获取device值
  adb devices
  ```

- adb 连接后，执行以下命令在手机安装 ATX 应用，包含httprpc服务的apk到手机，`atx-agent, minicap, minitouch`，具体介绍可以看，[uiautomator2项目](https://github.com/openatx/uiautomator2)，安装之前打开手机的开发者选项、
USB调试、USB安装等功能

  ```python
  python3 -m uiautomator2 init
  ```

- 在手机上打开 ATX ，点击 `启动 UIAutomator` 选项，确保 UIAutomator 是运行的。

- 如何运行这个脚本:

  ```python
  # 在该项目的文件夹根目录打开
  python main.py
  ```

- 能动就说明能成功运行，接下来你可以退出脚本(`Ctrl`+`C` 或者 关掉终端窗口)，在 `main.py` 中修改你的配置。

### 安卓端

待续，在试验用哪个app比较方便运行python脚本，目前收集有，qpython3L，termux，Pydroid 3，目前只成功在termux上运行，不过比较复杂。

## 说明

### 必改参数

- device

  在pc上通过`adb devices`来获得

  在安卓上写死：`http://0.0.0.0:7912`

- 选择运行的任务，true表示运行，一次跑一个任务
  - is_ant_forest_on
  - is_zhi_fu_bao_to_2019_on
  - is_tao_bao_to_2019_on
  - is_zhi_fu_bao_gain_points_on

### 可选参数

- is_app_lock

  是否有app九宫格锁，true有

- lock_points

  如果有app九宫格锁，填入解锁的点坐标，可通过weditor来获得，具体介绍看，[weditor项目](https://github.com/openatx/weditor)



## 待完成任务

- 代码优化
- 安卓端自动运行python脚本，如有哪位大神知道怎么在安卓端运行python脚本，麻烦推荐一下，谢谢！
- Q-Q


## Discussing
- [在github上提问](https://github.com/scoful/unHurtHand-Automator/issues/new "在github上提问")

- wechat：scoful

- QQ：1269717999

- email：1269717999@qq.com
