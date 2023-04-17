import datetime
import os

import allure
import pytest
from appium.webdriver import webdriver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#-*-coding:gb18030-*-
# For W3C actions
import logging,sys
import time

from base.chat import Chat
from base.config import Config
from base.logcat import LogcatCathcher
from pageobject.login_page import Loginpage
from base.log import Logger

#写入日志



class TestEcshop():
    l_obj = LogcatCathcher()#获取app后台运行日志 f


#前提先设置开启电话权限和麦克风权限，其他权限关闭
    def setup(self) -> None:
        # caps = {}
        # caps["platformName"] = "Android"
        # caps["appium:deviceName"] = "4d06665b"
        # #caps["appium:noReset"] = "true"#启动app时不要清除原始的数据，打开此控件之后只会出现一次”始终允许“和一次”允许“，未打开此控件则会出现一次”始终允许“和两次”允许“
        # #caps["appium:fullReset"] = False
        # caps["appium:appPackage"] = "com.qiwu.life"
        # caps["appium:appActivity"] = ".ui.activity.MainActivity"
        # #caps["appium:appActivity"] = ".ui.activity.LaunchActivity"
        # caps["appium:ensureWebviewsHavePages"] = True
        # caps["appium:nativeWebScreenshot"] = True
        # caps["appium:newCommandTimeout"] = 3600
        # caps["appium:connectHardwareKeyboard"] = True
        # caps["unicodeKeyboard"] = True  # 使用unicodeKeyboard的编码方式来发送字符串
        # caps["resetKeyboard"] = True  # 将键盘给隐藏起来
        # global driver
        # global server
        # global nowTime
        # server = "http://127.0.0.1:4723/wd/hub"
        # self.driver = webdriver.Remote(server, caps)
        # self.driver.implicitly_wait(10)
        # driver=self.driver
        driver = Config()
        self.driver = driver.devices("http://127.0.0.1:4723/wd/hub",r"\yaml\vivonex_phone.yaml")



    #@allure.step(title="yiyayiyayou")
    # @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
    # @allure.testcase("http://www.baidu.com/", "测试用例的地址")
    # @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
    # allure.dynamic.title("用例标题")
    # allure.dynamic.description("用例描述")
    #@pytest.mark.skipif(1 == 1, reason='该类不需要执行测试')满足条件则跳过用例
    #@pytest.mark.xfail(strict=True)预期测试失败用例，strict=True若在执行测试用例时结果为xpass，那么设置该参数后会使测试记录为失败，reason='期望失败的理由'
    #可以在设置raises 参数。设置该参数后，如果执行失败，则标记为常规Fail，除非是出现raises设置的错误，才会显示xfail。

    #@pytest.mark.repeat(2)#该用例重复执行两次
    #@pytest.mark.flaky(reruns=2, reruns_delay=10)# 用例失败后重新运行2次，重运行之间的间隔时间为10s
    @allure.step(title="互动小说游客登入操作")
    #@pytest.mark.skip()#跳过该条用例
    def test_login(self):
        ip = Loginpage(self.driver)
        ip.login_free()
        #time.sleep(5)

    @pytest.mark.skip(reason='该类不需要执行测试')#跳过该条用例
    @allure.step(title="授权用例")
    def test_allow(self):
        ip = Loginpage(self.driver)
        ip.allow_always()
        #self.driver.allow_always()
        #assert "yunxu" in self.driver.page_source


    #@pytest.mark.skip()#跳过该条用例
    @allure.step(title="一个不能发日志的日志用例")
    def test_priht(self):
        logger = Logger("appium",CmdLevel=logging.DEBUG,FileLevel=logging.INFO)
        logger.debug("debug message!")
        logger.info("info message!")
        logger.warn("warning message!")
        logger.error("error message!")
        logger.critical("critical message!")
        # log.start_log()
        # log.end_log()

    def teardown(self) -> None:
        #pass
        #停止读取日志
        self.l_obj.catch_logcat()
        # os.system("pause")
        os.system('adb kill-server')
        self.driver.quit()




