from automator import Automator

if __name__ == '__main__':
    # 安卓本地运行
    device = 'http://0.0.0.0:7912'
    # pc运行,adb devices 命令后得出的结果
    # device = '53aac21a'

    # 是否有app九宫锁
    isAppLock = False
    # 九宫锁解锁的点的坐标，可以通过Weditor来获取每个点的相对坐标
    lockPoints = [(0.235, 0.575), (0.494, 0.571), (0.756, 0.573), (0.501, 0.716), (0.239, 0.859), (0.76, 0.72),
                  (0.756, 0.863)]

    instance = Automator(device, isAppLock, lockPoints)
    # 启动脚本。
    instance.start()
