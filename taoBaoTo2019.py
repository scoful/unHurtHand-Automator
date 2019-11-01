from util import *


def taoBao_platform(self):
    # 打开淘宝
    self.d.app_start("com.taobao.taobao", wait=True)
    time.sleep(20)
    if self.d.xpath('//*[@text="狂欢开场"]').exists:
        self.d.xpath('//*[@text="狂欢开场"]').click()
        time.sleep(2)
        self.d.press("back")
        short_wait()
    else:
        logging.error("找不到狂欢开场入口！")
        return
    if self.d.xpath('//*[@text="领红包"]').exists:
        self.d.xpath('//*[@text="领红包"]').click()
    else:
        logging.error("页面上找不到双11淘宝活动入口！")
        return
    # 等待界面出现完整
    self.d.xpath('//*[@text="双11合伙人，全民开喵铺，瓜分20亿红包"]').wait(20)
    if self.d.xpath('//*[@text="双11合伙人，全民开喵铺，瓜分20亿红包"]').exists:
        while True:
            # 收喵币和升级
            taoBao_cat_coins(self)
            # 做任务
            taoBao_cat_tasks(self)
    else:
        logging.error("双11淘宝活动页面打不开！")
        return


def taoBao_cat_coins(self):
    if self.d.xpath(
            '//*[@resource-id="com.taobao.taobao:id/layermanager_penetrate_webview_container_id"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]').exists:
        self.d.xpath(
            '//*[@resource-id="com.taobao.taobao:id/layermanager_penetrate_webview_container_id"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]').click()
    time.sleep(1)
    # 收喵币
    self.d.click(0.498, 0.682)
    short_wait()
    if self.d.xpath('//*[@text="翻倍领取"]').exists:
        self.d.xpath('//*[@text="翻倍领取"]').click()
        short_wait()
        self.d.press("back")
        time.sleep(1)
    time.sleep(1)
    # 升级领红包
    if self.d.xpath('//*[@text="升级领红包"]').exists:
        self.d.xpath('//*[@text="升级领红包"]').click()
        time.sleep(5)
    else:
        logging.error("升级领红包的位置定位不到")
        return
    # 关闭升级页面
    if self.d.xpath('//*[@text="关闭"]').exists:
        self.d.xpath('//*[@text="关闭"]').click()


def taoBao_cat_tasks(self):
    # 点击领喵币
    if self.d.xpath('//*[@text="领喵币"]').exists:
        self.d.xpath('//*[@text="领喵币"]').click()
        time.sleep(2)
    else:
        logging.error("领喵币的位置定位不到")
        return
    # 签到
    if self.d.xpath('//*[@text="签到"]').exists:
        self.d.xpath('//*[@text="签到"]').click()
        time.sleep(2)
    self.d.swipe(self.dWidth / 2, self.dHeight / 2, self.dWidth / 2, 0, 1)
    if self.d.xpath('//*[@text="去浏览"]').exists:
        self.d.xpath('//*[@text="去浏览"]').click()
        time.sleep(25)
        if self.d.xpath('//*[@text="领红包"]').exists:
            self.d.xpath('//*[@text="领红包"]').click()
            time.sleep(10)
        else:
            self.d.press("back")
            time.sleep(1)
            if self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').exists:
                self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').click()
    else:
        time.sleep(1)
        if self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').exists:
            self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').click()
