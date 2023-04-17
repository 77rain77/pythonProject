from selenium.webdriver.common.by import By

from base.base_page import Bagepage


class Login_Page_HuaweiWatch(Bagepage):
    cbAgreement=(By.ID, "com.qiwu.childwatch:id/cbAgreement")  # 同意协议按钮
    tvUserAgreement=(By.ID, "com.qiwu.childwatch:id/tvUserAgreement") #用户协议链接
    tvPrivacyAgreement=(By.ID, "com.qiwu.childwatch:id/tvPrivacyAgreement") #隐私协议链接
    #tvExit=(By.ID, "com.qiwu.childwatch:id/tvExit")  # 退出按钮
    tvExit = (By.ID, "com.qiwu.childwatch:id/vLeft")  # 退出按钮
    #tvEnter=(By.ID, "com.qiwu.childwatch:id/tvEnter")  # 进入按钮
    tvEnter = (By.ID, "com.qiwu.childwatch:id/vRight")  # 进入按钮
    systemui=(By.CLASS_NAME,"//*[@text='晓悟故事']")
    tvTitle=(By.ID, "com.qiwu.childwatch:id/tvTitle")  # 协议标题
    FrameLayout=(By.CLASS_NAME, "android.widget.FrameLayout")  # 退出程序主页面
    permit_btn=(By.ID, "com.android.packageinstaller:id/permission_allow_button")  # 允许权限按钮
    forbid_btn=(By.ID, "com.android.packageinstaller:id/permission_deny_button")  # 禁止权限按钮

    def cbAgreement_click(self):#点击同意协议按钮
        self.click(self.cbAgreement)

    def tvUserAgreement_click(self):#点击用户协议链接
        self.click(self.tvUserAgreement)

    def tvPrivacyAgreement_click(self):#点击隐私协议按钮
        self.click(self.tvPrivacyAgreement)

    def tvExit_click(self):#点击退出按钮
        self.click(self.tvExit)

    def tvEnter_click(self):#点击进入按钮
        self.click(self.tvEnter)
    #不点击已阅读按钮则弹出“请阅读并同意”toast，点击完成则进入权限选择界面

    def systemui_click(self):
        self.click(self.systemui)

    def FrameLayout_click(self): #点击退出程序主页面按钮
        self.click(self.FrameLayout)

    def permit_btn_click(self):
        self.click(self.permit_btn)  #点击允许授权按钮

    def forbid_btn_click(self):
        self.click(self.forbid_btn)  #点击禁止授权按钮
