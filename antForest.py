from util import *


def ant_forest(self):
    # 打开支付宝
    self.d.app_start("com.eg.android.AlipayGphone", wait=True)
    # 开app九宫锁
    if self.isAppLock:
        self.d.swipe_points(self.lockPoints, 0.2)
        short_wait()
    time.sleep(20)
    # 先点击去首页
    if self.d.xpath('//*[@text="首页"]').exists:
        self.d.xpath('//*[@text="首页"]').click()
    short_wait()
    # 搜索框点击
    if self.d.xpath('//*[@resource-id="com.alipay.mobile.base.commonbiz:id/home_title_search_button"]').exists:
        self.d.xpath('//*[@resource-id="com.alipay.mobile.base.commonbiz:id/home_title_search_button"]').click()
        short_wait()
    else:
        logging.error("搜索框定位不到")
        return
    # 输入《蚂蚁森林》搜索
    self.d.xpath('//*[@resource-id="com.alipay.mobile.antui:id/search_bg"]').set_text("蚂蚁森林")
    short_wait()
    # 点击搜索按钮
    if self.d.xpath('//*[@text="搜索"]').exists:
        self.d.xpath('//*[@text="搜索"]').click()
        short_wait()
    else:
        logging.error("搜索按钮定位不到")
        return
    # 进入搜索结果
    if self.d.xpath('//*[@text="进入"]').exists:
        short_wait()
        self.d.xpath('//*[@text="进入"]').click()
    else:
        logging.error("蚂蚁森林搜索结果的进入字样定位不到")
        return
    # 收集自己的能量
    # 循环3次，保证多余的能量也能收集到
    for i in range(3):
        collect_energy(self)
    # 收集完滚动到底部，点击查看更多好友，进入
    self.d(scrollable=True).scroll.to(description="查看更多好友")
    if self.d.xpath("//*[contains(@text, '查看更多好友')]").exists:
        self.d.xpath("//*[contains(@text, '查看更多好友')]").click()
    else:
        logging.error("《查看更多好友》定位不到")
        return
    # 进入所有好友收集能量
    in_my_friends(self)

    # 结束关闭支付宝
    self.d.app_stop("com.eg.android.AlipayGphone")


def collect_energy(self):
    self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').wait(20)
    # 获取能量收集页面上所有可以点的按钮
    for elem in self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').all():
        # 以下按钮都不点
        if elem.text == "成就" or elem.text == "发消息" or elem.text == "弹幕" or \
                elem.text == "浇水" or elem.text == "公益林" or elem.text == "背包" \
                or elem.text == "通知" or elem.text == "任务" or elem.text == "攻略":
            continue
        else:
            # 点击收集能量
            elem.click()
            time.sleep(3)
            # 新活动入口，硬编码关闭
            if self.d.xpath('//*[@text="推荐你选择绿色出行，为地球节省碳排放"]').exists:
                short_wait()
                self.d.press("back")
                if self.d.xpath('//*[@text="我知道了"]').exists:
                    self.d.xpath('//*[@text="我知道了"]').click()


def in_my_friends(self):
    # 先滚到最下，获取最多的好友集
    self.d(scrollable=True).scroll.to(description="没有更多了")
    # 再回到顶部，从上往下走
    self.d(scrollable=True).scroll.toBeginning()
    a = 1
    while self.d.xpath(
            '//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[2]/android.view.View[' + str(
                a) + ']').exists:
        short_wait()
        logging.info(f"第{a}个")
        # 依次点进好友页面
        if self.d.xpath(
                '//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[2]/android.view.View[' + str(
                    a) + ']').exists:
            self.d.xpath(
                '//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[2]/android.view.View[' + str(
                    a) + ']').click()
        else:
            # TODO 时不时就报定位不到，需要调试
            logging.error(f"能量收集页面上的第{a}个好友定位不到")
            continue
        self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').wait(5)
        # 收集好友能量
        if self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').exists:
            collect_energy(self)
            short_wait()
            self.d.press("back")
        a = a + 1
        self.d.swipe_ext("up", scale=0.1)
        time.sleep(3)

    logging.info(f"{a}个好友收集完毕")
