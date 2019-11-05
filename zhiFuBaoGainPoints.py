from util import *


def gain_points(self):
    # 打开支付宝
    self.d.app_start("com.eg.android.AlipayGphone", wait=True)
    # 开app九宫锁
    if self.isAppLock:
        self.d.swipe_points(self.lockPoints, 0.2)
        short_wait()
    time.sleep(20)
    # 搜索框点击
    if self.d.xpath('//*[@resource-id="com.alipay.mobile.base.commonbiz:id/home_title_search_button"]').exists:
        self.d.xpath('//*[@resource-id="com.alipay.mobile.base.commonbiz:id/home_title_search_button"]').click()
        short_wait()
    else:
        logging.error("搜索框定位不到")
        return
    # 输入《领积分》搜索
    self.d.xpath('//*[@resource-id="com.alipay.mobile.antui:id/search_bg"]').set_text("领积分")
    short_wait()
    # 点击搜索按钮
    if self.d.xpath('//*[@text="搜索"]').exists:
        self.d.xpath('//*[@text="搜索"]').click()
        short_wait()
    else:
        logging.error("搜索按钮定位不到")
        return
    # 进入搜索结果
    if self.d.xpath('//*[@text="支付宝会员"]').exists:
        short_wait()
        self.d.xpath('//*[@text="支付宝会员"]').click()
    else:
        logging.error("领积分搜索结果的进入字样定位不到")
        return
    time.sleep(10)
    if self.d.xpath('//*[@text="领积分"]').exists:
        short_wait()
        self.d.xpath('//*[@text="领积分"]').click()
        time.sleep(5)
    else:
        logging.error("领积分按钮定位不到")
        return
    while self.d.xpath('//*[@text="点击领取"]').exists:
        short_wait()
        self.d.xpath('//*[@text="点击领取"]').click()
        short_wait()
