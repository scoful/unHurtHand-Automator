from util import *


def zhi_fu_bao_platform(self):
    # 打开支付宝
    self.d.app_start("com.eg.android.AlipayGphone", wait=True)
    # 开app九宫锁
    if self.isAppLock:
        self.d.swipe_points(self.lockPoints, 0.2)
        short_wait()
    time.sleep(20)
    if self.d.xpath('//*[@resource-id="com.alipay.android.phone.openplatform:id/home_advertisement"]').exists:
        self.d.xpath('//*[@resource-id="com.alipay.android.phone.openplatform:id/home_advertisement"]').click()
    else:
        logging.error("双11支付宝活动找不到入口")
        return
    # 等待界面出现完整
    self.d.xpath('//*[@text="双11合伙人，全民开喵铺，瓜分20亿红包"]').wait(20)
    if self.d.xpath('//*[@text="双11合伙人，全民开喵铺，瓜分20亿红包"]').exists:
        while True:
            # 收喵币和升级
            zhi_fu_bao_platform_cat_coins(self)
            # 做任务
            zhi_fu_bao_platform_cat_tasks(self)
    else:
        logging.error("双11支付宝活动页面打不开！")
        return


def zhi_fu_bao_platform_cat_coins(self):
    if self.d.xpath('//*[@text="关闭"]').exists:
        self.d.xpath('//*[@text="关闭"]').click()
    time.sleep(1)
    # 收喵币
    self.d.click(0.498, 0.682)
    time.sleep(1)
    # 升级领红包
    if self.d.xpath('//*[@resource-id="root"]/android.view.View[1]/android.widget.Button[2]').exists:
        self.d.xpath('//*[@resource-id="root"]/android.view.View[1]/android.widget.Button[2]').click()
        time.sleep(5)
        # 关闭升级页面
        if self.d.xpath('//*[@text="开心收下"]').exists:
            self.d.xpath('//*[@text="开心收下"]').click()
        if self.d.xpath('//*[@text="关闭"]').exists:
            self.d.xpath('//*[@text="关闭"]').click()
    else:
        logging.error("升级领红包的位置定位不到")
        return
    time.sleep(2)
    if self.d.xpath('//*[@text="关闭"]').exists:
        self.d.xpath('//*[@text="关闭"]').click()


def zhi_fu_bao_platform_cat_tasks(self):
    # 点击领喵币
    if self.d.xpath('//*[@resource-id="root"]/android.view.View[1]/android.widget.Button[3]').exists:
        self.d.xpath('//*[@resource-id="root"]/android.view.View[1]/android.widget.Button[3]').click()
    else:
        logging.error("领喵币的位置定位不到")
        return
    time.sleep(2)
    # 签到
    if self.d.xpath('//*[@text="签到"]').exists:
        logging.info("还没签到")
        self.d.xpath('//*[@text="签到"]').click()
        time.sleep(2)
        # 关闭签到提醒页，进入支日历
        if self.d.xpath('//*[@text="开心收下"]').exists:
            self.d.xpath('//*[@text="开心收下"]').click()
        time.sleep(2)
        if self.d.xpath('//*[@resource-id="com.alipay.mobile.nebula:id/h5_rl_title"]').exists:
            logging.info("进入了支日历")
            time.sleep(2)
            # 退回领喵币中心
            self.d.press("back")
            logging.info("退出支日历")
        time.sleep(1)

    if self.d.xpath('//*[@text="去浏览"]').exists:
        self.d.xpath('//*[@text="去浏览"]').click()
        time.sleep(3)
        self.d.press("back")
        short_wait()
        if self.d.xpath('//*[@text="关闭"]').exists:
            self.d.xpath('//*[@text="关闭"]').click()
    if self.d.xpath('//*[@text="去完成"]').exists:
        self.d.xpath('//*[@text="去完成"]').click()
        time.sleep(3)
        time.sleep(3)
        self.d.press("back")
        short_wait()
        if self.d.xpath('//*[@text="关闭"]').exists:
            self.d.xpath('//*[@text="关闭"]').click()
    if self.d.xpath('//*[@text="去浇水"]').exists:
        self.d.xpath('//*[@text="去浇水"]').click()
        time.sleep(3)
        self.d(scrollable=True).scroll.to(description="查看更多好友")
        if self.d.xpath("//*[contains(@text, '查看更多好友')]").exists:
            self.d.xpath("//*[contains(@text, '查看更多好友')]").click()
        else:
            logging.error("《查看更多好友》定位不到")
            return
        short_wait()
        self.d.xpath('//*[@resource-id="J_rank_list_append"]/android.view.View[1]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="浇水"]').click()
        time.sleep(2)
        if self.d.xpath(
                '//android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]').exists:
            self.d.xpath(
                '//android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]').click()
        short_wait()
        self.d.press("back")
        short_wait()
        self.d.press("back")
        short_wait()
        self.d.press("back")
        short_wait()
    if self.d.xpath('//*[@text="关闭"]').exists:
        self.d.xpath('//*[@text="关闭"]').click()
