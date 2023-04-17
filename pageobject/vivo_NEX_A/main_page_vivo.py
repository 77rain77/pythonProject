from selenium.webdriver.common.by import By

from base.base_page import Bagepage


class Main_Page_Vivo(Bagepage):
    contentView = (By.ID, "com.qiwu.watch:id/contentView")  # 唤出软键盘区域文本框
    stateImage = (By.ID, "com.qiwu.watch:id/stateImage")  # 头像监听状态按钮  android.widget.ImageView
    muteCheckedView = (By.ID, "com.qiwu.watch:id/muteCheckedView") #喇叭按钮
    avatarView = (By.ID, "com.qiwu.watch:id/avatarView")  # 个人中心图标
    search_buttonch = (By.ID, "com.qiwu.watch:id/search_buttonch")  # 搜索框
    search_button = (By.ID, "com.qiwu.watch:id/search_button")#搜索按钮
    search_edit = (By.ID, "com.qiwu.watch:id/search_edit")#搜索内容输入框
    search_delete_btn = (By.ID, "com.qiwu.watch:id/search_delete_btn")  # 历史内容删除按钮
    text = (By.XPATH, '//*[contains(@text,"{}")]'.format("暂无作品"))#搜索内容不到显示暂无作品图片和文字
    work_name = (By.ID, "com.qiwu.watch:id/work_name")  # 搜索出的作品名称
    EditText = (By.CLASS_NAME, "android.widget.EditText")  # 编辑区
    inputConfirmView = (By.ID, "com.qiwu.watch:id/inputConfirmView")  # 发送按钮
    toKeyboardModeView = (By.ID, "com.qiwu.watch:id/toKeyboardModeView")  # 键盘点击
    toVoiceModeView = (By.ID, "com.qiwu.watch:id/toVoiceModeView")  # 键盘头像状态监听按钮
    text1 =(By.XPATH,'//*[contains(@text,"{}")]'.format("推荐"))
    text2 =(By.XPATH,'//*[contains(@text,"{}")]'.format("新作"))
    text3 =(By.XPATH,'//*[contains(@text,"{}")]'.format("古风"))
    text4 =(By.XPATH,'//*[contains(@text,"{}")]'.format("穿越"))
    text5 =(By.XPATH,'//*[contains(@text,"{}")]'.format("冒险"))
    text6 =(By.XPATH,'//*[contains(@text,"{}")]'.format("男性向"))
    text7 =(By.XPATH,'//*[contains(@text,"{}")]'.format("女性向"))
    text8 =(By.XPATH,'//*[contains(@text,"{}")]'.format("架空"))
    text9 =(By.XPATH,'//*[contains(@text,"{}")]'.format("儿童"))
    text10 =(By.XPATH,'//*[contains(@text,"{}")]'.format("恋爱"))
    text11 =(By.XPATH,'//*[contains(@text,"{}")]'.format("科幻"))
    text12 =(By.XPATH,'//*[contains(@text,"{}")]'.format("武侠"))
    text13 =(By.XPATH,'//*[contains(@text,"{}")]'.format("找寻"))
    text14 =(By.XPATH,'//*[contains(@text,"{}")]'.format("灾难"))
    text15 =(By.XPATH,'//*[contains(@text,"{}")]'.format("经营"))
    text16 =(By.XPATH,'//*[contains(@text,"{}")]'.format("花仙爱上我"))
    text17 =(By.XPATH,'//*[contains(@text,"{}")]'.format("经纪人"))
    text18 =(By.XPATH,'//*[contains(@text,"{}")]'.format("爱上青丘狐"))
    text19 =(By.XPATH,'//*[contains(@text,"{}")]'.format("顶流的日常"))

    def contentView_click(self):  #点击呼出软键盘文本框区域
        self.click(self.contentView)

    def stateImage_click(self):  #点击头像状态监听按钮
        self.click(self.stateImage)

    def muteCheckedView_click(self):  #点击喇叭按钮
        self.click(self.muteCheckedView)

    def avatarView_click(self):  #点击个人中心图标
        self.click(self.avatarView)

    def search_buttonch_click(self):  #点击搜索框
        self.click(self.search_buttonch)

    def search_button_click(self):  #点击搜索按钮
        self.click(self.search_button)

    def search_edit_click(self):  #点击搜索内容输入框
        self.click(self.search_edit)

    def search_edit_input(self,value):  #搜索框输入框输入文字
        self.base_input(self.search_edit,value)

    def search_delete_btn_click(self):  #点击历史内容删除按钮
        self.click(self.search_delete_btn)

    def EditText_click(self):  #点击编辑区
        self.click(self.EditText)

    def EditText_input(self,value):  #编辑区输入文字
        self.base_input(self.EditText,value)

    def inputConfirmView_click(self):  #点击发送按钮
        self.click(self.inputConfirmView)

    def toKeyboardModeView_click(self):  #点击键盘
        self.click(self.toKeyboardModeView)

    def text16_click(self):  #点击花仙爱上我
        self.click(self.text16)

    def toVoiceModeView_click(self):  #点击键盘头像状态监听按钮
        self.click(self.toVoiceModeView)
