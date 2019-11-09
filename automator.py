import uiautomator2 as u2

from antForest import *
from taoBaoTo2019 import *
from zhiFuBaoTo2019 import *
from zhiFuBaoGainPoints import *


class Automator:
    def __init__(self, device: str, is_app_lock: False, lock_points: [], is_ant_forest_on: False,
                 is_zhi_fu_bao_to_2019_on: False, is_tao_bao_to_2019_on: False, is_zhi_fu_bao_gain_points_on: False):
        self.d = u2.connect(device)
        self.dWidth, self.dHeight = self.d.window_size()
        self.isAppLock = is_app_lock
        self.lockPoints = lock_points
        logging.info(f'屏幕分辨率： {self.dWidth}, {self.dHeight}')
        self.isAntForestOn = is_ant_forest_on
        self.isZhiFuBaoT2019On = is_zhi_fu_bao_to_2019_on
        self.isTaoBaoT2019On = is_tao_bao_to_2019_on
        self.isZhiFuBaoGainPointsOn = is_zhi_fu_bao_gain_points_on

    def start(self):
        """
        启动脚本
        """
        start_time = datetime.datetime.now()
        try:
            if self.isAntForestOn:
                ant_forest(self)
            if self.isZhiFuBaoT2019On:
                zhi_fu_bao_platform(self)
            if self.isTaoBaoT2019On:
                tao_bao_platform(self)
            if self.isZhiFuBaoGainPointsOn:
                gain_points(self)
        except Exception as result:
            logging.error(f"未知错误！{result}")
            return
            # 结束关闭支付宝
            self.d.app_stop("com.eg.android.AlipayGphone")
            # 结束关闭淘宝
            self.d.app_stop("com.taobao.taobao")
        end_time = datetime.datetime.now()
        time_cost = end_time - start_time
        logging.info(f"结束，总耗时：{time_cost}")
