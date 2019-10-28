import uiautomator2 as u2

from antForest import *


class Automator:
    def __init__(self, device: str, isAppLock: False, lockPoints: []):
        self.d = u2.connect(device)
        self.dWidth, self.dHeight = self.d.window_size()
        self.isAppLock = isAppLock
        self.lockPoints = lockPoints
        print("屏幕分辨率：" + str(self.dWidth) + ", " + str(self.dHeight))

    def start(self):
        """
        启动脚本
        """
        # while True:
        start_time = datetime.datetime.now()
        try:
            ant_forest(self)
        except:
            self.d.app_stop("com.eg.android.AlipayGphone")
        end_time = datetime.datetime.now()
        time_cost = end_time - start_time

        print("结束，总耗时：" + str(time_cost))
