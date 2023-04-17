import datetime
import os
from telnetlib import EC

import allure
import pytest
from appium.webdriver import webdriver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#-*-coding:gb18030-*-
# For W3C actions
import logging,sys
import time

from selenium.webdriver.support.wait import WebDriverWait

from base.chat import Chat
from base.config import Config
from base.logcat import LogcatCathcher
from pageobject.login_page import Loginpage
from base.log import Logger
from pageobject.vivo_NEX_A.inside_page_vivo import Inside_Page_Vivo
from pageobject.vivo_NEX_A.main_page_vivo import Main_Page_Vivo
from pageobject.vivo_NEX_A.menu_page_vivo import Menu_Page_Vivo
from pageobject.vivo_NEX_A.startup_page_vivo import Login_Page_Vivo

@allure.severity("critical")
@allure.epic("项目名称: 安卓手机版互动小说")
@allure.feature("登入模块")
@allure.story("用例的标题: 互动小说冒烟测试")
class TestVivoNex():
    l_obj = LogcatCathcher()   #获取app后台运行日志 f
    logger = Logger("appium", CmdLevel=logging.DEBUG, FileLevel=logging.INFO)  #获取日志

    def setup(self) -> None:
        driver = Config()
        self.driver = driver.devices("http://127.0.0.1:4723/wd/hub",r"\yaml\vivonex_phone.yaml")

    def commom(self):
        loginpage = Login_Page_Vivo(self.driver)
        loginpage.button_fist_click()
        loginpage.agreementView_click()
        loginpage.firstTypeLoginView_click()
        #loginpage.manView_click()
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loginpage.positiveView))
        time.sleep(16)
        loginpage.positiveView_click()  # 点击立即开启按钮
        loginpage.permission_allow_button_click()

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step('安装成功后，打开app')
    @allure.step('显示启动页')
    def test_login1(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        mainpage.save_screenshot('进入首页')
        pytest.assume(mainpage.isElementPresent(mainpage.stateImage))

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step('下拉，上划刷新')
    @allure.step('状态显示正常')
    def test_login2(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        mainpage.save_screenshot('进入首页')
        mainpage.swipeDown(t=500,n=2,x=0.5,y=0.2,z=0.7)
        mainpage.swipeUp(t=500,n=30,x=0.5,y=0.7,z=0.2)
        mainpage.save_screenshot('加载完成')
        #pytest.assume(mainpage.is_element_exist("正在加载"))

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step('首页点击右上角用户头像')
    @allure.step('正常进入到我的页面')
    def test_login3(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage=Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        pytest.assume(mainpage.isElementPresent(menupage.user_share))
        mainpage.save_screenshot('我的页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step('点击作品，点击作品名称')
    @allure.step('跳转到作品详情页')
    def test_login4(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage=Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        insidepage.workName_click()
        pytest.assume(mainpage.isElementPresent(insidepage.detail_des))
        mainpage.save_screenshot('作品详情页')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step('状态切换_语音切换文本编辑——点击对话框')
    @allure.step('可切换成文本输入键盘状态以及收起状态')
    def test_login5(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        mainpage.contentView_click()
        time.sleep(2)
        pytest.assume(mainpage.isElementPresent(mainpage.EditText))
        mainpage.save_screenshot('键盘输入')
        mainpage.toVoiceModeView_click()
        time.sleep(2)
        pytest.assume(mainpage.isElementPresent(mainpage.EditText) is False)
        mainpage.save_screenshot('键盘收起')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("作品对话页")
    @allure.step('点击进入作品，点击返回图标')
    @allure.step('成功返回上一页面')
    def test_inside1(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage = Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        insidepage.navigationView_click()
        pytest.assume(mainpage.isElementPresent(mainpage.search_buttonch))
        mainpage.save_screenshot('返回到主页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("作品对话页")
    @allure.step('右侧用户信息_点击右侧蓝色对话气泡')
    @allure.step('点击后无任何反应')
    def test_inside2(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage = Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        insidepage.contentView_click()
        pytest.assume(mainpage.isElementPresent(insidepage.authorNameDes))
        mainpage.save_screenshot('点击气泡无反应')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("作品对话页")
    @allure.step('文本输入状态_输入汉字，数字等')
    @allure.step('数据输入无异常')
    def test_inside3(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage = Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        insidepage.muteCheckedView_click()
        insidepage.clickInputView_click()
        insidepage.inputView_click()
        path_chat = r"\data\\chat"
        data_chat = Chat().chat(path_chat)
        for value in data_chat:
            insidepage.inputView_input(value)
            insidepage.inputConfirmView_click()
            mainpage.save_screenshot('输入数据无误')
        insidepage.toVoiceModeView_click()
        insidepage.muteCheckedView_click()

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('基本信息页_昵称头像点击')
    @allure.step('进入基本信息页')
    def test_my1(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage=Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        mainpage.avatarView_click()
        pytest.assume(mainpage.isElementPresent(menupage.user_id))
        mainpage.save_screenshot('进入基本信息页')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('基本信息页_修改昵称')
    @allure.step('昵称设置正确')
    def test_my2(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        mainpage.avatarView_click()
        path_name = r"\data\\name"
        data_name = Chat().chat(path_name)
        for value in data_name:
            import re
            test_str = re.search(r"\W", value) #\W:匹配任何非单词字符,等价于 [^A-Z a-z 0-9_]
            my_re3 = re.search(r"[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]", value)
            menupage.use_nick_name_click()
            menupage.inputNickNameView_click()
            menupage.inputNickNameView_input(value)
            if 2 <= len(value) <= 8 and my_re3== None:
                menupage.confirmView_click()
                pytest.assume(mainpage.isElementPresent(menupage.user_id))
                if pytest.assume(mainpage.isElementPresent(menupage.user_id))==False:
                    menupage.save_screenshot('账号输入不符合规则')
            elif len(value) <= 2 or len(value) >= 8:
                menupage.confirmView_click()
                menupage.save_screenshot('账号输入不符合规则toast')
                pytest.assume(menupage.is_element_exist("确定"))
                menupage.navigationView_click()
            elif my_re3!= None:
                menupage.confirmView_click()
                menupage.save_screenshot('账号输入不符合规则toast')
                pytest.assume(menupage.is_element_exist("确定"))
                menupage.navigationView_click()
            else:
                pass

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('历史记录点击')
    @allure.step('进入历史记录页')
    def test_my3(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.llHistory_click()
        pytest.assume(menupage.locate_element(menupage.title).text=="历史记录")
        mainpage.save_screenshot('进入历史记录页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('收藏按钮点击')
    @allure.step('进入收藏页面')
    def test_my4(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.llFavorites_click()
        pytest.assume(menupage.locate_element(menupage.title).text=="收藏")
        mainpage.save_screenshot('进入收藏页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('排行榜按钮点击')
    @allure.step('进入排行榜页面')
    def test_my5(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.llRank_click()
        pytest.assume(menupage.locate_element(menupage.title).text=="排行榜")
        mainpage.save_screenshot('进入排行榜页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('我的订单按钮点击')
    @allure.step('进入我的订单页面')
    def test_my6(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.llOrder_click()
        pytest.assume(menupage.locate_element(menupage.title).text=="我的订单")
        mainpage.save_screenshot('进入我的订单页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('点击设置，点击关于晓悟互动小说')
    @allure.step('进入关于我们页')
    def test_my7(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.install_click()
        menupage.install_3_click()
        time.sleep(1)
        pytest.assume(menupage.locate_element(menupage.title).text == "关于我们")
        mainpage.save_screenshot('进入关于我们页')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('点击设置，点击用户协议')
    @allure.step('进入用户协议页')
    def test_my8(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.install_click()
        menupage.install_4_click()
        time.sleep(1)
        pytest.assume(menupage.locate_element(menupage.title).text == "用户协议")
        menupage.confirmView_click()
        mainpage.save_screenshot('进入用户协议页面')
        pytest.assume(mainpage.isElementPresent(menupage.install_4))

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('点击设置，点击隐私协议')
    @allure.step('进入隐私协议页面')
    def test_my9(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.install_click()
        menupage.install_5_click()
        time.sleep(1)
        pytest.assume(menupage.locate_element(menupage.title).text == "隐私协议")
        menupage.confirmView_click()
        mainpage.save_screenshot('进入隐私协议页面')
        pytest.assume(mainpage.isElementPresent(menupage.install_5))

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('点击设置，点击退出登入')
    @allure.step('进入登入页面')
    def test_my10(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.install_click()
        menupage.install_6_click()
        pytest.assume(mainpage.isElementPresent(menupage.ImageView))
        time.sleep(1)
        mainpage.save_screenshot('进入登入页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("我的")
    @allure.step('点击设置，点击意见与反馈')
    @allure.step('进入意见与反馈页面')
    def test_my11(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        menupage = Menu_Page_Vivo(self.driver)
        mainpage.avatarView_click()
        menupage.install_click()
        menupage.install_2_click()
        time.sleep(1)
        pytest.assume(menupage.locate_element(menupage.title).text == "意见与反馈")
        mainpage.save_screenshot('进入意见与反馈页面')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("作品对话页")
    @allure.step('点击作品，点击作品名称')
    @allure.step('跳转到作品详情页')
    def test_inside4(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage = Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        pytest.assume(mainpage.isElementPresent(insidepage.share))
        mainpage.save_screenshot('右上角分享与设置按钮')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step('点击进入作品')
    @allure.step('正常回到首页')
    def test_inside5(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage = Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        insidepage.navigationView_click()
        pytest.assume(mainpage.isElementPresent(mainpage.muteCheckedView))
        mainpage.save_screenshot('正常返回首页')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step('点击搜索按钮')
    @allure.step('正确搜索到作品')
    def test_inside6(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        mainpage.search_buttonch_click()
        mainpage.search_edit_input("花仙爱上我")
        mainpage.search_button_click()
        pytest.assume(mainpage.locate_element(mainpage.work_name).text == "花仙爱上我")
        mainpage.save_screenshot('正常搜索出作品')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("广告")
    @allure.step('点击进入作品点击广告')
    @allure.step('跳转到广告安装界面')
    def test_advertisement1(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage = Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        time.sleep(7)
        insidepage.container_click()
        time.sleep(3)
        pytest.assume(mainpage.is_element_exist("安装"))
        mainpage.save_screenshot('进入到广告安装界面')

    @pytest.mark.flaky(reruns=0, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.test
    @allure.title("文本")
    @allure.step('语音模式下进入到对话页，点击晓悟头像，在监听状态时点击喇叭')
    @allure.step('切换为文本模式')
    def test_text1(self):
        self.commom()
        mainpage = Main_Page_Vivo(self.driver)
        insidepage = Inside_Page_Vivo(self.driver)
        mainpage.text16_click()
        time.sleep(15)
        mainpage.stateImage_click()
        mainpage.muteCheckedView_click()
        pytest.assume(mainpage.isElementPresent(insidepage.clickInputView))
        mainpage.save_screenshot('切换为文本模式')



    def teardown(self) -> None:
        #pass
        #停止读取日志
        self.l_obj.catch_logcat()
        # os.system("pause")
        os.system('adb kill-server')
        self.driver.quit()
        #self.driver.reset()#卸载重装应用




