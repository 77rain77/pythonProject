import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import Bagepage
from base.chat import Chat
from base.config import Config


class Loginpage(Bagepage):
    allow = ('xpath', "//*[contains(@text,'始终允许')]")
    allow1 = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    number=2
    def allow_always(self):
        self.always_allow(self.number,self.allow,self.allow1)

    # username_loc=(By.NAME,"username")
    # password_loc=(By.NAME,"password")
    # submit_loc=(By.XPATH,"")
    # def login_ecshop(self,username="admin",password="admin123"):
    #     self.send_keys(self.username_loc,username)
    #     self.send_keys(self.password_loc,passwor

    # device1="\yaml\\vivonex_phone.yaml"
    # device2="\yaml\\iphone"
    # server="http://127.0.0.1:4723/wd/hub"
    # def config(self):
    #     self.devices(self.device1,self.server)
    agreementid=(By.ID,"com.qiwu.watch:id/agreementView")#同意协议按钮
    firstTypeLoginView=(By.ID,"com.qiwu.watch:id/firstTypeLoginView")#游客登入按钮
    positiveView=(By.ID,"com.qiwu.watch:id/positiveView")#弹窗授权按钮
    permission_allow_button=(By.ID,"com.android.permissioncontroller:id/permission_allow_button")#允许授权按钮
    #FrameLayout=(By.CLASS_NAME,"android.widget.FrameLayout")
    TextView = (By.ID, "com.qiwu.watch:id/contentView")#唤出软键盘按钮
    EditText=(By.CLASS_NAME,"android.widget.EditText")#编辑区
    inputConfirmView=(By.ID, "com.qiwu.watch:id/inputConfirmView")#发送按钮
    toKeyboardModeView=(By.ID,"com.qiwu.watch:id/toKeyboardModeView")#键盘点击
    inputView=(By.ID,"com.qiwu.watch:id/inputView")#作品页输入框
    stateImage=(By.ID,"com.qiwu.watch:id/stateImage")#监听状态按钮  android.widget.ImageView
    avatarView=(By.ID,"com.qiwu.watch:id/avatarView")#个人中心图标
    nickNameView=(By.ID,"com.qiwu.watch:id/nickNameView")#昵称修改按钮
    confirmView=(By.ID,"com.qiwu.watch:id/confirmView")#确认修改昵称按钮
    loc = '//*[contains(@text,"{}")]'.format("昵称格式不正确")
    inputNickNameView=(By.ID,"com.qiwu.watch:id/inputNickNameView")#昵称修改文本
    navigationView=(By.ID,"com.qiwu.watch:id/navigationView")#返回按钮
    toast=(By.XPATH,loc)
    path_chat=r"\data\\chat"
    path_name=r"\data\\name"
    def login_free(self):
        self.click(self.agreementid)
        self.click(self.firstTypeLoginView)
        e = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.positiveView))
        e.click()
        try:
            self.click(self.permission_allow_button)
            #time.sleep(2)
        except:
            self.save_screenshot("权限请求错误")
        time.sleep(2)
        #print(self.is_element_exist("经纪人"))
        assert self.is_element_exist("经纪人")
        for n in range(16):
            self.swipLeft()
        time.sleep(1)
        self.click(self.TextView)
        self.send_keys(self.EditText,"我想看青丘狐")
        self.click(self.inputConfirmView)
        assert self.is_element_exist("青丘狐")
        time.sleep(1)
        data_chat=Chat()
        self.data_chat=data_chat.chat(self.path_chat)
        self.click(self.toKeyboardModeView)
        for i in self.data_chat:
            self.send_keys(self.inputView,i)
            self.click(self.inputConfirmView)
        self.driver.back()
        for n in range(10):
            self.swipeUp()
        self.click(self.avatarView)#点击互动小说主页的头像
        time.sleep(1)
        self.click(self.avatarView)#个人中心的头像编辑
        #self.click(self.nickNameView)#昵称修改按钮
        #time.sleep(1)#进入到昵称修改界面，需要进行等待
        data_name=Chat()
        self.data_name=data_name.chat(self.path_name)
        for i in self.data_name:
            self.click(self.nickNameView)
            #self.wait(10,0.1,self.EditText)
            time.sleep(1)
            self.clear(self.EditText)
            self.send_keys(self.EditText, i)
            #print(self.data_name)
            if 2<=len(i)<=8:
                self.click(self.confirmView)
                time.sleep(1)
                assert self.is_element_exist("账号")
            elif len(i)<=2 or len(i)>=8:
                self.click(self.confirmView)
                #time.sleep(1)
                self.find_toast("昵称格式不正确")
                #assert self.is_element_exist("昵称格式不正确")
                self.click(self.navigationView)
            else:
               pass









