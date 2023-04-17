import datetime
import os
import time
import allure
import pytest
from base.chat import Chat
from base.config import Config
from base.logcat import LogcatCathcher
from pageobject.xiaoxun_watch.main_page import First_Page_XiaoXun
from pageobject.xiaoxun_watch.menu_page import menuone_Page_XiaoXun
from pageobject.xiaoxun_watch.startup_page import Login_Page_XiaoXun


@allure.severity("critical")  #严重缺陷
@allure.epic("项目名称: 小寻手表互动小说")
@allure.feature("冒烟测试")
@allure.story("用例的标题: 小寻手表互动小说冒烟测试")
class Testxiaoxun():
    l_obj = LogcatCathcher()#获取app后台运行日志

    def setup(self) -> None:
        driver = Config()
        self.driver = driver.devices("http://127.0.0.1:4723/wd/hub",r"\yaml\xiaoxun_watch")

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.smoke
    def test_delete_image(self):
        os.system(r"del /q/a/f/s C:\Users\qiwu-PM\PycharmProjects\pythonProject\image")

    def common(self):
        startup = Login_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        self.driver.implicitly_wait(3)
        startup.permit_btn_click()
        self.driver.implicitly_wait(10)

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("登入页界面是否显示卡顿")
    @allure.step('安装成功后，打开app')
    @allure.step('在勾选协议界面，快速左右滑动页面')
    def test_login(self):
        startup = Login_Page_XiaoXun(self.driver)
        self.driver.implicitly_wait(5)
        pytest.assume(startup.is_element_exist("用户协议"))
        pytest.assume(startup.is_element_exist("隐私政策"))
        startup.swipRight(200,3,0.9,0.5,0.1)
        startup.save_screenshot('登入页面向右滑动三次')
        startup.swipLeft(200,3,0.1,0.5,0.9)
        startup.save_screenshot('登入页面向左滑动三次')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("协议勾选")
    @allure.step("未勾选'已阅读并同意'点击进入")
    def test_login1(self):
        startup = Login_Page_XiaoXun(self.driver)
        startup.tvEnter_click()
        pytest.assume(startup.ImageView_pop())
        startup.save_screenshot('未勾选协议点击进入')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("协议勾选")
    @allure.step("勾选'已阅读并同意'点击退出，再次进入app")
    def test_login2(self):
        startup = Login_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.driver.launch_app()#启动app
        pytest.assume(startup.is_element_exist("用户协议"))
        pytest.assume(startup.is_element_exist("隐私政策"))

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("协议勾选")
    @allure.step("勾选'已阅读并同意'右滑退出，再次进入app")
    def test_login3(self):
        startup = Login_Page_XiaoXun(self.driver)
        startup.swipRight(200,3,0.9,0.5,0.1)
        startup.driver.launch_app()  # 启动app
        pytest.assume(startup.is_element_exist("用户协议"))
        pytest.assume(startup.is_element_exist("隐私政策"))

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("用户协议界面")
    @allure.step("点击用户协议进入页面上下滑动")
    def test_agreement1(self):
        startup = Login_Page_XiaoXun(self.driver)
        startup.tvUserAgreement_click()
        time.sleep(6)
        pytest.assume(startup.is_element_exist("用户协议"))
        pytest.assume(startup.is_element_exist("隐私协议")==False)
        startup.swipeUp(200,5,0.5,0.9,0.1)
        startup.swipeDown(200,3,0.5,0.1,0.9)
        startup.save_screenshot('用户协议界面滑动正常')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("隐私协议界面")
    @allure.step("点击隐私协议进入页面上下滑动")
    def test_agreement2(self):
        startup = Login_Page_XiaoXun(self.driver)
        startup.tvPrivacyAgreement_click()
        time.sleep(6)
        pytest.assume(startup.is_element_exist("隐私协议"))
        #pytest.assume(startup.is_element_exist("用户协议") == False)
        startup.swipeUp(200,5,0.9,0.5,0.1)
        startup.swipeDown(200,3,0.9,0.5,0.1)
        startup.save_screenshot('隐私协议界面滑动正常')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("进入麦克风权限获取页面")
    @allure.step("安装成功，勾选'已阅读并同意'，点击进入")
    def test_login4(self):
        startup = Login_Page_XiaoXun(self.driver)
        #firstpage=First_Page_HuaweiWatch(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        time.sleep(1)
        pytest.assume(startup.isElementPresent(startup.permit_btn))
        if startup.isElementPresent(startup.permit_btn)==False:
            startup.save_screenshot('未进入到麦克风授权页面')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("进入麦克风权限获取页面")
    @allure.step("安装成功，勾选'已阅读并同意'，点击进入")
    @allure.step("给予权限后退出，再次打开app")
    def test_login5(self):
        startup = Login_Page_XiaoXun(self.driver)
        firstpage = First_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        startup.driver.implicitly_wait(5)
        startup.permit_btn_click()
        time.sleep(3)
        startup.driver.background_app(4)
        time.sleep(3)
        pytest.assume(startup.isElementPresent(firstpage.ivMicGuide))
        startup.save_screenshot("授权未生效")

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("进入麦克风权限获取页面")
    @allure.step("安装成功，勾选'已阅读并同意'，点击进入")
    @allure.step("点击禁止麦克风权限")
    def test_access1(self):
        startup = Login_Page_XiaoXun(self.driver)
        firstpage = First_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        self.driver.implicitly_wait(3)
        startup.swipeUp(200,1,0.7,0.5,0.5)
        startup.forbid_btn_click()
        startup.save_screenshot('提示麦克风权限被拒绝')
        pytest.assume(startup.isElementPresent(firstpage.ivMicGuide))
        pytest.assume(startup.ImageView_pop())
        startup.save_screenshot('进入新手引导')

    # @pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("进入麦克风权限获取页面")
    @allure.step("安装成功，勾选'已阅读并同意'，点击进入")
    @allure.step("点击禁止麦克风权限，点击麦克风按钮弹出权限再次拒绝")
    def test_access2(self):
        startup = Login_Page_XiaoXun(self.driver)
        firstpage = First_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        self.driver.implicitly_wait(3)
        startup.swipeUp(200, 1, 0.7, 0.5, 0.5)
        startup.forbid_btn_click()
        startup.save_screenshot('提示麦克风权限被拒绝')
        firstpage.ivMicGuide_click()
        startup.forbid_btn_click()
        pytest.assume(startup.isElementPresent(firstpage.ivGuideOne))
        pytest.assume(startup.ImageView_pop())
        startup.save_screenshot('进入新手引导')

    # @pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.usefixtures("noreset")
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.test
    @allure.title("进入麦克风权限获取页面")
    @allure.step("拒绝麦克风权限，在新手引导第一页退出app")
    @allure.step("再次进入，弹出获取麦克风权限弹窗")
    def test_access3(self):
        startup = Login_Page_XiaoXun(self.driver)
        firstpage = First_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        self.driver.implicitly_wait(3)
        startup.swipeUp(200, 1, 0.7, 0.5, 0.5)
        startup.forbid_btn_click()
        startup.save_screenshot('提示麦克风权限被拒绝')
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        startup.driver.launch_app()
        pytest.assume(startup.isElementPresent(startup.permit_btn))
        startup.save_screenshot('麦克风权限弹窗')
        # startup.driver.background_app(4)
        # pytest.assume(startup.isElementPresent(startup.permit_btn))
        # startup.save_screenshot('麦克风权限弹窗')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("进入麦克风权限获取页面")
    @allure.step("安装成功，勾选'已阅读并同意'，点击进入")
    @allure.step("点击允许麦克风权限")
    def test_access4(self):
        startup = Login_Page_XiaoXun(self.driver)
        firstpage = First_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        self.driver.implicitly_wait(3)
        startup.permit_btn_click()
        pytest.assume(startup.isElementPresent(firstpage.ivMicGuide))
        startup.save_screenshot('进入新手引导且未提示麦克风权限被拒绝')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("进入麦克风权限获取页面")
    @allure.step("未获取麦克风权限时点击麦克风，再次弹出麦克风获取权限页面")
    @allure.step("给予麦克风权限")
    def test_access5(self):
        startup = Login_Page_XiaoXun(self.driver)
        firstpage = First_Page_XiaoXun(self.driver)
        startup.cbAgreement_click()
        startup.tvEnter_click()
        self.driver.implicitly_wait(3)
        startup.swipeUp(200,1, 0.7, 0.5, 0.5)
        startup.forbid_btn_click()
        firstpage.ivMicGuide_click()
        startup.permit_btn_click()
        time.sleep(20)
        startup.save_screenshot('进入首页对话页')
        pytest.assume(startup.isElementPresent(firstpage.tvNpcName))

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("启动页")
    @allure.step("在启动页页面，快速左右滑动页面")
    def test_login6(self):
        startup = Login_Page_XiaoXun(self.driver)
        #startup.swipRight(100, 5, 0.5, 0.5, 0.6)
        startup.swipLeft(100, 5, 0.9, 0.5, 0.1)
        pytest.assume(startup.isElementPresent(startup.cbAgreement))
        startup.save_screenshot('正常进入app')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("新手引导")
    @allure.step("在新手引导第二页，查看ui界面显示当线条跃动")
    def test_guidance3(self):
        firstpage = First_Page_XiaoXun(self.driver)
        self.common()
        pytest.assume(firstpage.isElementPresent(firstpage.ivGuideOne))
        firstpage.ivMicGuide_click()
        pytest.assume(firstpage.isElementPresent(firstpage.ivGuideTwo))
        firstpage.save_screenshot('显示当线条跃动语句')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step("点击导航栏按钮")
    @allure.step("点击游客用户名")
    def test_home(self):
        firstpage = First_Page_XiaoXun(self.driver)
        menupage=menuone_Page_XiaoXun(self.driver)
        self.common()
        firstpage.ivMicGuide_click()
        time.sleep(20)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        time.sleep(1)
        firstpage.ivMenu_click()
        pytest.assume(firstpage.isElementPresent(menupage.Ranking))
        firstpage.save_screenshot('跳转到个人中心页面')
        menupage.tvUserName_click()
        pytest.assume(firstpage.isElementPresent(menupage.Ranking))
        firstpage.save_screenshot('游客用户名不可修改')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step("首页可以正常上下左右滑动")
    def test_home2(self):
        firstpage = First_Page_XiaoXun(self.driver)
        self.common()
        firstpage.ivMicGuide_click()
        time.sleep(20)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        time.sleep(1)
        #firstpage.swipRight(100, 5, 0.7, 0.5, 0.8)
        firstpage.swipLeft(100, 5, 0.9, 0.5, 0.1)
        firstpage.swipeUp(100, 5, 0.5, 0.9, 0.1)
        firstpage.swipeDown(100, 5, 0.5, 0.1, 0.9)
        firstpage.save_screenshot('首页可以正常滑动')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step("首页顶部下拉滑动有刷新效果且底部上拉无提示")
    def test_home3(self):
        firstpage = First_Page_XiaoXun(self.driver)
        self.common()
        firstpage.ivMicGuide_click()
        time.sleep(20)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.swipeDown(100, 1, 0.2, 0.5, 1)
        #pytest.assume(firstpage.is_element_exist('为你推荐'))
        firstpage.swipeUp(100, 17, 0.5, 0.7, 0.1)
        pytest.assume(firstpage.is_element_exist('为你推荐')==False)
        #pytest.assume(firstpage.ImageView_pop())
        firstpage.save_screenshot('首页底部无法上拉且无提示')
        firstpage.ivMicGuide_click()
        firstpage.tvTitle_click()
        pytest.assume(firstpage.is_element_exist('晓悟故事'))
        firstpage.save_screenshot('点击title无跳转')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("作品进入")
    @allure.step("点击一个免费作品，直接进入游戏")
    def test_works(self):
        firstpage = First_Page_XiaoXun(self.driver)
        self.common()
        firstpage.ivMicGuide_click()
        time.sleep(22)
        pytest.assume(firstpage.isElementPresent(firstpage.ivVolume))
        firstpage.save_screenshot('进入免费作品')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("登入注册")
    @allure.step("点击登入/注册按钮，跳转到二维码")
    def test_enter(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(20)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        time.sleep(1)
        firstpage.ivMenu_click()
        menupage.tvbottom_click()
        pytest.assume(firstpage.isElementPresent(menupage.ivCodeLogin))
        firstpage.save_screenshot('登入二维码页面')
        menupage.cvbottom_click()
        pytest.assume(menupage.ImageView_pop())
        firstpage.save_screenshot('登录取消')


    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("个人中心")
    @allure.step("在排行榜页面，点击导航栏按钮")
    def test_personal(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        #firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.ivMenu_click()
        time.sleep(1)
        menupage.ranking_click()
        pytest.assume(firstpage.is_element_exist('1'))
        pytest.assume(firstpage.is_element_exist('2'))
        pytest.assume(firstpage.is_element_exist('3'))
        pytest.assume(firstpage.is_element_exist('4'))
        menupage.swipeUp(100, 10, 0.5, 0.9, 0.1)
        menupage.swipeDown(100, 5, 0.5, 0.1, 0.9)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        pytest.assume(firstpage.isElementPresent(menupage.Ranking))
        firstpage.save_screenshot('排行榜页面进入个人中心')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("个人中心")
    @allure.step("在收藏页面点击作品名跳转到对话流")
    def test_personal2(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        time.sleep(1)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.tvTitle_click()
        firstpage.cbFavorite_click()
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.ivMenu_click()
        time.sleep(1)
        menupage.collect_click()
        firstpage.tvWorksName1_click()
        pytest.assume(firstpage.isElementPresent(firstpage.tvNpcName))
        firstpage.save_screenshot('进入到对话页')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("个人中心")
    @allure.step("在存档页面点击作品名跳转到对话流")
    def test_personal3(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.ivMenu_click()
        time.sleep(1)
        menupage.save_click()#点击存档按钮
        firstpage.tvWorksName1_click()
        pytest.assume(firstpage.isElementPresent(firstpage.tvNpcName))
        firstpage.save_screenshot('进入到对话页')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("个人中心")
    @allure.step("在存档页面进入作品，再次返回存档页面")
    def test_personal4(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.ivMenu_click()
        time.sleep(1)
        menupage.save_click()  # 点击存档按钮
        firstpage.save_screenshot('存档前')
        firstpage.tvWorksName1_click()
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.save_screenshot('回到存档后')
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.save_screenshot('回到菜单页')
        pytest.assume(firstpage.isElementPresent(menupage.Ranking))
        firstpage.save_screenshot('存档页面进入个人中心')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3,reruns_delay=3)#失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("个人中心")
    @allure.step("在收藏页面点击收藏作品删除按钮")
    @allure.step("在收藏页面点击取消删除收藏作品按钮")
    @allure.step("在收藏页面点击确定删除收藏作品按钮")
    def test_personal5(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.tvTitle_click()
        firstpage.cbFavorite_click()
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.ivMenu_click()
        time.sleep(1)
        menupage.collect_click()
        menupage.flDelete_click()
        pytest.assume(firstpage.isElementPresent(menupage.tvCancel))
        firstpage.save_screenshot('进入是否删除收藏界面')
        menupage.tvCancel_click()
        pytest.assume(firstpage.isElementPresent(menupage.flDelete))
        firstpage.save_screenshot('点击取消删除按钮')
        menupage.flDelete_click()
        menupage.tvConfirm_click()
        time.sleep(1)
        pytest.assume(firstpage.isElementPresent(firstpage.tvWorksName1)==False)
        firstpage.save_screenshot('点击确定删除按钮')
        pytest.assume(firstpage.is_element_exist("收藏夹空荡荡的呢"))

    @pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("个人中心")
    @allure.step("点击新版本")
    def test_personal6(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.ivMenu_click()
        time.sleep(1)
        firstpage.swipeUp(100, 1, 0.5, 0.7, 0.3)
        menupage.collect_click()
        pytest.assume(menupage.ImageView_pop())
        firstpage.save_screenshot('已是最新版本')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("对话页")
    @allure.step("点击音量键")
    def test_inside(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.ivVolume_click()
        pytest.assume(firstpage.isElementPresent(firstpage.vVolumeDecrease))
        firstpage.save_screenshot('音量修改界面')
        for i in range(10):
            firstpage.vVolumeDecrease_click()
        firstpage.save_screenshot('显示静音状态')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("对话页")
    @allure.step("快速点击唤醒球多次")
    def test_dialogue(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        for i in range(20):
            if firstpage.isElementPresent(firstpage.tvNpcName):
                firstpage.tvNpcName_click()
            elif firstpage.isElementPresent(firstpage.viewAsr):
                firstpage.viewAsr_click()
            else:
                firstpage.viewIdle_click()
        pytest.assume(firstpage.isElementPresent(firstpage.viewIdle))
        firstpage.save_screenshot('快速切换唤醒球')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("对话页")
    @allure.step("对话页静置三分钟")
    def test_dialogue2(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        time.sleep(190)
        pytest.assume(firstpage.isElementPresent(firstpage.vAchievement))
        firstpage.save_screenshot('对话页静置三分钟')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("作品详情页")
    @allure.step("点击收藏按钮")
    def test_details(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.tvTitle_click()
        firstpage.cbFavorite_click()
        pytest.assume(menupage.ImageView_pop())
        firstpage.save_screenshot('收藏成功')
        firstpage.cbFavorite_click()
        pytest.assume(menupage.ImageView_pop())
        firstpage.save_screenshot('取消成功')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("作品详情页")
    @allure.step("在作品详情页右滑返回")
    def test_details2(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.tvTitle_click()
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        pytest.assume(firstpage.isElementPresent(firstpage.ivVolume))
        firstpage.save_screenshot('回到对话页')

    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.smoke
    @allure.title("首页")
    @allure.step("点击历练榜和我的成就")
    def test_ranking_list(self):
        self.common()
        firstpage = First_Page_XiaoXun(self.driver)
        firstpage.ivMicGuide_click()
        time.sleep(22)
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        pytest.assume(firstpage.isElementPresent(firstpage.vRanking))
        pytest.assume(firstpage.isElementPresent(firstpage.vAchievement))
        firstpage.save_screenshot('存在历练榜和我的成就')
        firstpage.vRanking_click()
        pytest.assume(firstpage.is_element_exist("全国榜"))
        firstpage.save_screenshot('进入全国榜')
        for i in range(15):
            firstpage.swipeUp(100, 5, 0.5, 0.9, 0.1)
        pytest.assume(firstpage.is_element_exist("30"))
        firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
        firstpage.vAchievement_click()
        pytest.assume(firstpage.is_element_exist("历练点"))
        firstpage.save_screenshot('进入我的成就')


    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.order
    @allure.title("新手引导")
    @allure.step("在新手引导第一页，退出app重新进入")
    def test_guidance1(self):
        firstpage = First_Page_XiaoXun(self.driver)
        self.common()
        time.sleep(3)
        aa=firstpage.driver.current_activity()
        print(aa)
        firstpage.swipRight(100, 5, 0.1, 0.5, 0.9)
        firstpage.driver.launch_app()
        #firstpage.driver.background_app(5)
        time.sleep(2)
        pytest.assume(firstpage.isElementPresent(firstpage.ivGuideOne))
        firstpage.save_screenshot('进入新手引导页第一页')
        firstpage.driver.update_settings({"appium:noReset": False})

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.order
    @allure.title("新手引导")
    @allure.step("在新手引导第二页，退出app重新进入")
    def test_guidance2(self):
        firstpage = First_Page_XiaoXun(self.driver)
        self.common()
        firstpage.driver.update_settings({"appium:noReset": True})
        firstpage.ivMicGuide_click()
        firstpage.swipRight(100, 5, 0.1, 0.5, 0.9)
        firstpage.driver.launch_app()
        #firstpage.driver.background_app(5)
        time.sleep(2)
        pytest.assume(firstpage.isElementPresent(firstpage.ivGuideOne))
        firstpage.save_screenshot('进入新手引导页第一页')
        firstpage.driver.update_settings({"appium:noReset": False})

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.order
    @allure.title("进入麦克风权限获取页面")
    @allure.step("未获取麦克风权限时，点击麦克风，进入授权界面")
    @allure.step("退出软件，再次打开app,处于麦克风授权页面，点击允许授权")
    def test_access4(self):
        startup = Login_Page_XiaoXun(self.driver)
        firstpage = First_Page_XiaoXun(self.driver)
        firstpage.driver.update_settings({"appium:noReset": True})
        startup.cbAgreement_click()
        startup.tvEnter_click()
        self.driver.implicitly_wait(3)
        startup.swipeUp(200, 1, 0.7, 0.5, 0.5)
        startup.forbid_btn_click()
        firstpage.ivMicGuide_click()
        firstpage.swipRight(200, 1, 0.1, 0.5, 0.9)
        time.sleep(2)
        startup.driver.launch_app()
        #firstpage.driver.background_app(5)
        time.sleep(3)
        pytest.assume(startup.isElementPresent(startup.permit_btn))
        startup.save_screenshot('此时在麦克风权限页面')
        startup.permit_btn_click()
        pytest.assume(startup.isElementPresent(firstpage.ivMenu))
        startup.save_screenshot('获取麦克风权限成功')

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.login
    @allure.title("登入状态下")
    @allure.step("点击退出登入")
    @allure.step("点击确认退出登入")
    def test_already(self):
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        time.sleep(3)
        firstpage.ivMenu_click()
        menupage.tvbottom_click()
        pytest.assume(firstpage.isElementPresent(menupage.tvCancel))
        firstpage.save_screenshot('弹出确定退出toast')
        menupage.tvConfirm_click()
        pytest.assume(firstpage.isElementPresent(menupage.ImageView_pop()))
        firstpage.save_screenshot('退出成功toast')
        time.sleep(2)
        menupage.tvbottom_click()
        pytest.assume(firstpage.isElementPresent(menupage.ivCodeLogin))
        firstpage.save_screenshot('登入二维码')


    # @pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.login
    @allure.title("登入状态下")
    @allure.step("点击退出登入")
    @allure.step("点击取消退出登入")
    def test_already2(self):
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        time.sleep(3)
        firstpage.ivMenu_click()
        menupage.tvbottom_click()
        pytest.assume(firstpage.isElementPresent(menupage.tvCancel))
        firstpage.save_screenshot('弹出确定退出toast')
        menupage.tvCancel_click()
        pytest.assume(firstpage.isElementPresent(menupage.tvBottom))
        firstpage.save_screenshot('取消退出登入')


    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.login
    @allure.title("登入状态下")
    @allure.step("昵称输入验证")
    def test_already2(self):
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        path = r"\data\\name"
        chat=Chat().chat(path)
        time.sleep(3)
        firstpage.ivMenu_click()
        for value in chat:
            menupage.tvUserName_click()
            menupage.etContent_click()
            menupage.etContent_input(menupage.etContent, value)
            menupage.tvConfirm1_click()
            import re
            test_str = re.search(r"\W", value)
            if test_str != None:
                pytest.assume(firstpage.isElementPresent(menupage.ivDelete))
                firstpage.save_screenshot('昵称格式输入错误')
                firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
                time.sleep(3)
            elif len(value)>6:
                pytest.assume(firstpage.isElementPresent(menupage.tvUserName))
                firstpage.save_screenshot('昵称格式输入错误')
                time.sleep(3)
            else:
                pytest.assume(firstpage.isElementPresent(menupage.tvUserName))
                firstpage.save_screenshot('昵称格式输入正确')
                time.sleep(3)
            # if firstpage.isElementPresent(menupage.ivDelete):
            #     firstpage.swipRight(100, 1, 0.1, 0.5, 0.9)
            #     break
            # else:
            #     break

    #@pytest.mark.skip()  # 跳过该条用例
    @pytest.mark.flaky(reruns=3, reruns_delay=3)  # 失败重试两次，中间间隔三秒
    @pytest.mark.login
    @allure.title("登入状态下")
    @allure.step("点击昵称删除按钮")
    def test_already3(self):
        firstpage = First_Page_XiaoXun(self.driver)
        menupage = menuone_Page_XiaoXun(self.driver)
        firstpage.ivMenu_click()
        menupage.tvUserName_click()
        menupage.ivDelete_click()
        menupage.tvConfirm1_click()
        time.sleep(1)
        pytest.assume(menupage.ImageView_pop())
        firstpage.save_screenshot("昵称删除按钮正确")


    #@pytest.mark.skip(reason='该类不需要执行测试')  # 跳过该条用例
    def teardown(self) -> None:
        #pass
        #停止读取日志
        self.l_obj.catch_logcat()
        # os.system("pause")
        os.system('adb kill-server')
        self.driver.quit()


