#import datetime
from datetime import datetime
from lib2to3.pgen2 import driver

import allure
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class Bagepage:
    #打开浏览器
    def __init__(self,driver):
        self.driver=driver
    # def open_browser(self):
    #     global driver
    #     global server
    #     server = "http://127.0.0.1:4723/wd/hub"
    #     self.driver = webdriver.Remote(server, caps)
    #     driver = self.driver
    #     self.driver.implicitly_wait(5)#隐性等待
    ImageView = (By.CLASS_NAME, "android.widget.ImageView")  # 弹出的警告

        #加载网页
    def get(self,url):
        self.get(url)

        #定位元素
    def locate_element(self,args):
        return self.driver.find_element(*args)

    def ImageView_pop(self): #弹出toast
        return self.isElementPresent(self.ImageView)

    def isElementPresent(self, args):
        try:
            self.locate_element(args)
            #print("定位到了，不是错的")
            return True
        except Exception as e:
            print(e)
            #print("定位不到，就是错的")
            return False



        #设置值
    def send_keys(self,args,value):
        self.locate_element(args).send_keys(value)

        #单击
    def click(self,args):
        self.locate_element(args).click()

        #清除输入框
    def clear(self,args):
        self.locate_element(args).clear()

        #输入文本
    def base_input(self,args,value):
        self.clear(args)
        self.send_keys(args,value)


        #获取文本信息
    def get_text(self,args):
        return self.locate_element(args).text

        #回到首页
    def go_home(self):
        self.driver.gotoHomePage()

        #获取title
    def get_title(self):
        return self.driver.title

        #进入框架
    def goto_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)

        #出框架
    def out_frame(self):
        self.driver.switch_to.default_content()

        #选择下拉框
    def choice_select_by_value(self, args):
        sel=Select(self.locate_element(args))
        sel.select_by_value("1")

    def reinstall_app(self,app_name):
        ret = self.driver.is_app_installed(bundle_id=app_name)
        print(ret)
        # 判断app是否已经安装
        # 如果没有安装我们就给它安装

    def uninstall_app(self,app_name):
        self.driver.remove_app(app_id=app_name)
        #卸载
        # app_id: 应用程序的包名

        #显式等待
    def wait(self,args):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(args))  # (By.ID,id)这里传的是个元组

        #隐式等待
        #self.driver.implicitly_wait(10)

    def swipeUp(self,t=500,n=1,x=1,y=1,z=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * x  # x坐标
        y1 = l['height'] * y  # 起始y坐标
        y2 = l['height'] * z  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=500, n=1,x=1,y=1,z=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * x  # x坐标
        y1 = l['height'] * y  # 起始y坐标
        y2 = l['height'] * z  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=500, n=1,x=1,y=1,z=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * x
        y1 = l['height'] * y
        x2 = l['width'] * z
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1,x=1,y=1,z=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * x
        y1 = l['height'] * y
        x2 = l['width'] * z
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def always_allow(self, number,allow,allow1):
        # allow = (By.ID, "com.android.permissioncontroller:id/permission_allow_always_button")
        # allow = ('xpath',"//*[@text='始终允许']")
        #allow = ('xpath', "//*[contains(@text,'始终允许')]")
        self.driver.find_element(*allow).click()
        for i in range(number):
            #allow1 = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(allow1))
                e.click()
            #except Exception as e:这是自定义的异常
            except:
                self.save_screenshot("权限授权错误")



    def save_screenshot(self, img_doc):
        '''
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        '''
        OUTPUTS_DIR = "./image"
        file_name = OUTPUTS_DIR + "/{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), img_doc)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, img_doc, allure.attachment_type.PNG)
        #case_logger.info("页面截图文件保存在：{}".format(file_name))

    #判断元素是否在页面上存在
    def is_element_exist(self, element):
        source = self.driver.page_source
        #print(source)
        if element in source:
            return True
        else:
            return False

    #获取toast
    def find_toast(self, message, timeout=10, poll=0.01):
        try:
            message ='//*[@text=\'{}\']'.format(message)  # Toast内容
            element = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.XPATH, message)))
            context = element.get_attribute("text")
            print(context)
            return True
        except Exception as e:
            print(("Get Toast Error : ", e))
            return False



    def position_click(self,x,y):
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        real_x = width*x
        real_y = height*y
        postions = (real_x, real_y)
        self.driver.tap(postions)














