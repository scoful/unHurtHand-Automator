from util import *


def tao_bao_platform(self):
    # 打开淘宝
    self.d.app_start("com.taobao.taobao", wait=True)
    time.sleep(20)

    open_red_pack(self)

    # 更新最新版淘宝app，定位首页右上角的入口
    if self.d.xpath(
            '//*[@resource-id="com.taobao.taobao:id/sv_search_view"]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[1]/android.widget.ImageView[2]').exists:
        self.d.xpath(
            '//*[@resource-id="com.taobao.taobao:id/sv_search_view"]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[1]/android.widget.ImageView[2]').click()
    else:
        logging.error("页面上找不到双11淘宝活动入口！")
        return

    # 等待界面出现完整
    self.d.xpath('//*[@text="双11合伙人，全民开喵铺，瓜分20亿红包"]').wait(20)
    if self.d.xpath('//*[@text="双11合伙人，全民开喵铺，瓜分20亿红包"]').exists:
        while True:
            # 收喵币和升级
            tao_bao_cat_coins(self)
            # 做任务
            tao_bao_cat_tasks(self)
    else:
        logging.error("双11淘宝活动页面打不开！")
        return


def open_red_pack(self):
    # 先拆每日红包
    # 搜索框点击
    if self.d.xpath('//*[@content-desc="搜索"]').exists:
        self.d.xpath('//*[@content-desc="搜索"]').click()
        short_wait()
    else:
        logging.error("搜索框定位不到")
        return
    # 输入《https://s.click.taobao.com/i8ds4yv》搜索
    self.d.xpath('//*[@resource-id="com.taobao.taobao:id/searchEdit"]').set_text("https://s.click.taobao.com/i8ds4yv")
    short_wait()
    # 点击搜索按钮
    if self.d.xpath('//*[@text="搜索"]').exists:
        self.d.xpath('//*[@text="搜索"]').click()
        short_wait()
    else:
        logging.error("搜索按钮定位不到")
        return
    time.sleep(6)
    while not self.d.xpath('//*[@text="分享邀好友，继续开宝箱"]').exists:
        if self.d.xpath('//*[@text="拆今日红包"]').exists:
            self.d.xpath('//*[@text="拆今日红包"]').click()
            short_wait()
        if self.d.xpath('//*[@text="再拆一次"]').exists:
            self.d.xpath('//*[@text="再拆一次"]').click()
            short_wait()
    self.d.xpath('//*[@content-desc="转到上一层级"]').click()
    short_wait()
    self.d.press("back")
    short_wait()
    self.d.xpath('//*[@resource-id="com.taobao.taobao:id/btn_go_back"]').click()


def tao_bao_cat_coins(self):
    if self.d.xpath(
            '//*[@resource-id="com.taobao.taobao:id/layermanager_penetrate_webview_container_id"]/android.widget'
            '.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]').exists:
        self.d.xpath(
            '//*[@resource-id="com.taobao.taobao:id/layermanager_penetrate_webview_container_id"]/android.widget'
            '.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]').click()
    time.sleep(1)
    # 收喵币
    self.d.click(0.498, 0.682)
    short_wait()
    if self.d.xpath('//*[@text="直接收下"]').exists:
        self.d.xpath('//*[@text="直接收下"]').click()
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


def tao_bao_cat_tasks(self):
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
        if self.d.xpath('//*[@content-desc="捉猫猫"]').exists:
            self.d.xpath('//*[@content-desc="捉猫猫"]').click()
            time.sleep(10)
        else:
            self.d.press("back")
            time.sleep(1)
            if self.d.xpath('//*[@text="正在前往会场"]').exists:
                self.d.press("back")
                time.sleep(1)
            if self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').exists:
                self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').click()
    elif self.d.xpath('//*[@text="去签到"]').exists:
        self.d.xpath('//*[@text="去签到"]').click()
        time.sleep(10)

        if self.d.xpath('//*[@resource-id="content"]/android.view.View[8]/android.view.View[7]/android.view.View[1]') \
                .exists:
            self.d.xpath('//*[@resource-id="content"]/android.view.View[8]/android.view.View[7]/android.view.View[1]') \
                .click()
            short_wait()
            if self.d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[4]') \
                    .exists:
                self.d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[4]') \
                    .click()
        elif self.d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]').exists:
            self.d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]').click()
            short_wait()
            if self.d.xpath('//*[@text="签到"]').exists:
                self.d.xpath('//*[@text="签到"]').click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        if self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').exists:
            self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').click()
    elif self.d.xpath('//*[@text="去查看"]').exists:
        short_wait()
        self.d.press("back")
        short_wait()
        if self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').exists:
            self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').click()
    else:
        time.sleep(1)
        if self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').exists:
            self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.widget.Button[1]').click()
