from selenium.webdriver.common.by import By
from base.base_page import Bagepage


class Inside_Page_Vivo(Bagepage):
    share = (By.XPATH, '//*[@resource-id="com.qiwu.watch:id/actionLayout"]/android.widget.ImageView[1]')  # 分享按钮
    install = (By.XPATH, '//*[@resource-id="com.qiwu.watch:id/actionLayout"]/android.widget.ImageView[2]')  # 三个点按钮
    authorNameDes = (By.ID, "com.qiwu.watch:id/authorNameDes")  #作者
    workName = (By.ID, "com.qiwu.watch:id/workName")  # 作品名称
    workIcon = (By.ID, "com.qiwu.watch:id/workIcon")  # 作品图标
    information = (By.XPATH, '//*[contains(@text,"{}")]'.format("查看详情"))  # 查看详情按钮
    container = (By.ID, "com.qiwu.watch:id/container")  # 广告主体
    contentView = (By.ID, "com.qiwu.watch:id/contentView")  # 对话语句
    toKeyboardModeView = (By.ID, "com.qiwu.watch:id/toKeyboardModeView")  # 键盘点击
    muteCheckedView = (By.ID, "com.qiwu.watch:id/muteCheckedView")  # 喇叭点击
    stateImage = (By.ID, "com.qiwu.watch:id/stateImage")  # 头像状态点击
    stateHintText = (By.ID, "com.qiwu.watch:id/stateHintText")  # 状态显示词
    inputView = (By.ID, "com.qiwu.watch:id/inputView")  # 文字输入框
    inputConfirmView = (By.ID, "com.qiwu.watch:id/inputConfirmView")  # 发送按钮
    navigationView = (By.ID, "com.qiwu.watch:id/navigationView")  # 返回按钮
    clickInputView = (By.ID, "com.qiwu.watch:id/clickInputView")  # 点击输入
    card_restart = (By.ID, "com.qiwu.watch:id/card_restart")  # 重新开始按钮
    card_detail = (By.ID, "com.qiwu.watch:id/card_detail")  # 作品简介按钮
    card_favourite = (By.ID, "com.qiwu.watch:id/card_favourite")  # 收藏按钮
    card_report_the_problem = (By.ID, "com.qiwu.watch:id/card_report_the_problem")  # 我要上报问题按钮
    begin = (By.XPATH, '//android.widget.FrameLayout[1]/android.widget.ImageView[1]')#为你重新开始提示框或者收藏作品成功提示框，您上报的问题我们已经记录
    detail_start = (By.ID, "com.qiwu.watch:id/detail_start")  # 继续体验按钮
    favorite_btn = (By.ID, "com.qiwu.watch:id/favorite_btn")  # 收藏按钮
    detail_des = (By.ID, "com.qiwu.watch:id/detail_des")  # 简介文本
    toVoiceModeView = (By.ID, "com.qiwu.watch:id/toVoiceModeView")  # 输入框头像按钮点击


    def share_click(self):  #点击分享按钮
        self.click(self.share)

    def install_click(self):  #点击三个点
        self.click(self.install)

    def authorNameDes_click(self):  #点击作者名
        self.click(self.authorNameDes)

    def workName_click(self):  #点击作品名称
        self.click(self.workName)

    def workIcon_click(self):  #点击作品图标名称
        self.click(self.workIcon)

    def information_click(self):  #点击查看详情按钮
        self.click(self.information)

    def container_click(self):  #点击广告主体
        self.click(self.container)

    def toKeyboardModeView_click(self):  #点击键盘
        self.click(self.toKeyboardModeView)

    def muteCheckedView_click(self):  #点击喇叭
        self.click(self.muteCheckedView)

    def stateImage_click(self):  #点击头像监听状态
        self.click(self.stateImage)

    def inputView_click(self):  #点击文字输入框
        self.click(self.inputView)

    def inputView_input(self,value):#输入文字
        self.base_input(self.inputView,value)

    def inputConfirmView_click(self):  #点击发送按钮
        self.click(self.inputConfirmView)

    def navigationView_click(self):  #点击返回按钮
        self.click(self.navigationView)

    def clickInputView_click(self):  #点击 点击输入框
        self.click(self.clickInputView)

    def card_restart_click(self):  #点击重新开始按钮
        self.click(self.card_restart)

    def card_detail_click(self):  #点击作品简介按钮
        self.click(self.card_detail)

    def card_favourite_click(self):  #点击收藏按钮
        self.click(self.card_favourite)

    def card_report_the_problem_click(self):  #点击我要上报问题按钮
        self.click(self.card_report_the_problem)

    def detail_start_click(self):  #点击继续体验按钮
        self.click(self.detail_start)

    def favorite_btn_click(self):  #点击收藏按钮
        self.click(self.favorite_btn)

    def contentView_click(self):  #点击对话语句
        self.click(self.contentView)

    def toVoiceModeView_click(self):  #输入框头像按钮点击
        self.click(self.toVoiceModeView)


