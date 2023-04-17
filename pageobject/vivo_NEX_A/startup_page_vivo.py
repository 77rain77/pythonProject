from selenium.webdriver.common.by import By

from base.base_page import Bagepage


class Login_Page_Vivo(Bagepage):
    button_fist = (By.ID, "com.qiwu.watch:id/button_fist")  # 同意协议按钮
    button_second = (By.ID, "com.qiwu.watch:id/button_second")#不同意协议按钮
    firstTypeLoginView = (By.ID, "com.qiwu.watch:id/firstTypeLoginView")  # 游客登入按钮
    secondTypeLoginView=(By.ID,"com.qiwu.watch:id/secondTypeLoginView") #手机号登入按钮
    agreementView = (By.ID, "com.qiwu.watch:id/agreementView")  # 我已阅读并同意按钮
    jumpView = (By.ID, "com.qiwu.watch:id/jumpView")  # 下次再说
    voiceView = (By.ID, "com.qiwu.watch:id/voiceView")  # 语音交互选择框
    muteView = (By.ID, "com.qiwu.watch:id/muteView")  # 文本交互选择框
    manView = (By.ID, "com.qiwu.watch:id/manView")  # 我是男生按钮
    womanView = (By.ID, "com.qiwu.watch:id/womanView")  # 我是女生按钮
    inputPhoneView=(By.ID,"com.qiwu.watch:id/inputPhoneView") #输入手机号
    inputCodeView=(By.ID,"com.qiwu.watch:id/inputCodeView") #输入验证码
    loginView=(By.ID,"com.qiwu.watch:id/loginView") #手机号登入按钮
    titleLayout=(By.ID,"com.qiwu.watch:id/titleLayout") #返回按钮
    sendCodeView=(By.ID,"com.qiwu.watch:id/sendCodeView") #获取验证码按钮
    positiveView = (By.ID, "com.qiwu.watch:id/positiveView")  # 立即开启按钮
    negativeView = (By.ID, "com.qiwu.watch:id/negativeView")  # 退出立即体验按钮
    permission_allow_button = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")  # 允许授权按钮
    permission_deny_button=(By.ID,"com.android.permissioncontroller:id/permission_deny_button") #禁止授权按钮


    def button_fist_click(self):  #点击同意协议按钮
        self.click(self.button_fist)

    def button_second_click(self):  #点击不同意协议按钮
        self.click(self.button_second)

    def firstTypeLoginView_click(self):   #点击游客登入按钮
        self.click(self.firstTypeLoginView)

    def secondTypeLoginView_click(self):  #点击输入手机号登入按钮
        self.click(self.secondTypeLoginView)

    def agreementView_click(self):  #点击阅读并同意按钮
        self.click(self.agreementView)

    def jumpView_click(self):  #点击下次再说
        self.click(self.jumpView)

    def voiceView_click(self):  #点击语音交互选择框
        self.click(self.voiceView)

    def muteView_click(self):  #点击文本交互选择框
        self.click(self.muteView)

    def manView_click(self):  #点击我是男生按钮
        self.click(self.manView)

    def womanView_click(self):  #点击我是女生按钮
        self.click(self.womanView)

    def inputPhoneView_click(self):  #点击请输入手机号
        self.click(self.inputPhoneView)

    def inputPhoneView_input(self,value):#输入手机号
        self.base_input(self.inputPhoneView,value)

    def inputCodeView_click(self):#点击请输入验证码输入框
        self.click(self.inputCodeView)

    def inputCodeView_input(self,value):#输入验证码
        self.base_input(self.inputCodeView,value)

    def loginView_click(self):  #点击确定手机号登入
        self.click(self.loginView)

    def titleLayout_click(self):  #点击返回按钮
        self.click(self.titleLayout)

    def sendCodeView_click(self):  #点击获取验证码按钮
        self.click(self.sendCodeView)

    def positiveView_click(self):  #点击立即开启按钮
        self.click(self.positiveView)

    def negativeView_click(self):  #点击退出立即体验按钮
        self.click(self.negativeView)

    def permission_allow_button_click(self):  #点击允许授权按钮
        self.click(self.permission_allow_button)

    def permission_deny_button_click(self):#点击禁止授权按钮
        self.click(self.permission_deny_button)





