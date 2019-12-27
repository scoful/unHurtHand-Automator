from automator import Automator
import sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == '__main__':
    # 安卓本地运行
    # device = 'http://0.0.0.0:7912'
    # pc运行,adb devices 命令后得出的结果
    device = '53aac21b'

    # 是否有app九宫锁
    is_app_lock = False
    # 九宫锁解锁的点的坐标，可以通过Weditor来获取每个点的相对坐标
    lock_points = [(0.235, 0.575), (0.494, 0.571), (0.756, 0.859), (0.243, 0.863)]
    # 是否开启蚂蚁森林自动收能量任务
    is_ant_forest_on = True
    # 是否开启支付宝app领积分自动任务
    is_zhi_fu_bao_gain_points_on = True
    # 是否开启支付宝app2019双11活动自动任务
    is_zhi_fu_bao_to_2019_on = False
    # 是否开启淘宝app2019双11活动自动任务
    is_tao_bao_to_2019_on = False

    instance = Automator(device, is_app_lock, lock_points, is_ant_forest_on, is_zhi_fu_bao_to_2019_on,
                         is_tao_bao_to_2019_on, is_zhi_fu_bao_gain_points_on)
    # 启动脚本。
    instance.start()
