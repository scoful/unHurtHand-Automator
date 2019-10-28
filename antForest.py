from util import *


def ant_forest(self):
    # 打开支付宝
    self.d.app_start("com.eg.android.AlipayGphone", wait=True)
    # 开app九宫锁
    if self.isAppLock:
        self.d.swipe_points(self.lockPoints, 0.2)
    # 搜索框点击
    self.d.xpath('//*[@resource-id="com.alipay.mobile.base.commonbiz:id/home_title_search_button"]').click()
    # 输入蚂蚁森林搜索
    self.d.xpath('//*[@resource-id="com.alipay.mobile.antui:id/search_bg"]').set_text("蚂蚁森林")
    short_wait()
    # 点击搜索按钮
    self.d.xpath('//*[@text="搜索"]').click()
    # 进入搜索结果
    self.d.xpath('//*[@text="进入"]').click()
    # 收集自己的能量
    collect_energy(self)
    # 收集完滚动到底部
    self.d(scrollable=True).scroll.to(description="查看更多好友")
    if self.d.xpath("//*[contains(@text, '查看更多好友')]").exists:
        self.d.xpath("//*[contains(@text, '查看更多好友')]").click()
    else:
        print("找不到《查看更多好友》的入口，退出")
        return
    # 进入所有好友收集能量
    in_my_friends(self)
    # 结束关闭支付宝
    self.d.app_stop("com.eg.android.AlipayGphone")

def collect_energy(self):
    try:
        self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').wait(10)
        if self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').exists:
            m = 0
            for elem in self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').all():
                m = m + 1
                # print(m)
                if elem.text == "成就" or elem.text == "发消息" or elem.text == "弹幕" or \
                        elem.text == "浇水" or elem.text == "公益林" or elem.text == "背包" \
                        or elem.text == "通知" or elem.text == "任务" or elem.text == "攻略":
                    continue
                else:
                    self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button[' + str(m) + ']').click()
                    # 2019年双11活动入口，硬编码关闭
                    if self.d.xpath(
                            '//*[@resource-id="J_home_panel"]/android.view.View[1]/android.view.View[1]/android.view.View[1]').exists:
                        self.d.xpath(
                            '//*[@resource-id="J_home_panel"]/android.view.View[1]/android.view.View[1]/android.view.View[1]').click()
                    # 如果不小心进入了合种，硬编码关闭
                    if self.d.xpath('//*[@resource-id="J-guide"]/android.view.View[1]/android.view.View[3]').exists:
                        self.d.press("back")
                short_wait()
            # print("收集能量over")
        else:
            print("出异常了，退出重来吧！")
    except():
        print("出问题了")
        return


def in_my_friends(self):
    self.d(scrollable=True).scroll.to(description="没有更多了")
    self.d(scrollable=True).scroll.toBeginning()
    a = 0
    x0, y0, x1, y1 = 0, 0, 0, 0
    for elem in self.d.xpath('//*[@resource-id="J_rank_list_append"]/android.view.View').all():
        a = a + 1
        # print("第" + str(a))
        if a == 1:
            x0 = elem.center()[0]
            y0 = elem.center()[1]
        if a == 2:
            x1 = elem.center()[0]
            y1 = elem.center()[1]
        self.d.xpath('//*[@resource-id="J_rank_list_append"]/android.view.View[' + str(a) + ']').click()
        try:
            self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').wait(5)
            if self.d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button').exists:
                collect_energy(self)
                short_wait()
                self.d.press("back")
            if y1 != 0:
                self.d.swipe(x1, y1, x0, y0, 0.1)
        except():
            print("出问题了！")
            return
