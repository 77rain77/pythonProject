from selenium.webdriver.common.by import By

from base.base_page import Bagepage


class First_Page_XiaoXun(Bagepage):
    tvNpcName=(By.ID, "com.qiwu.watch:id/viewDialogue")#作品内页麦克风人物对话按钮
    ivMicGuide=(By.ID, "com.qiwu.watch:id/ivMic")#首页麦克风按钮
    viewIdle=(By.ID,"com.qiwu.watch:id/viewIdle")#作品页麦克风唤醒球
    #waveLineView=(By.ID,"com.qiwu.watch:id/waveLineView")#麦克风线条
    viewAsr=(By.ID,"com.qiwu.watch:id/viewAsr")#对话页线条
    waveLineView=(By.ID, "com.qiwu.watch:id/guideBottomView")  # 麦克风线条
    ivGuideOne=(By.ID,"com.qiwu.watch:id/ivGuideOne")#引导第一页
    ivGuideTwo=(By.ID,"com.qiwu.watch:id/ivGuideTwo")#引导第二页
    ivTips=(By.ID,"com.qiwu.watch:id/ivTips")#标签
    vRanking=(By.ID,"com.qiwu.watch:id/vRanking")#历练榜
    vAchievement=(By.ID,"com.qiwu.watch:id/vAchievement")#我的成就
    #ivMenu=(By.ID,"com.qiwu.adultwatch:id/ivMenu")#菜单按钮
    ivMenu=(By.ID, "com.qiwu.watch:id/tvNickname")  # 菜单按钮
    tvWorksName=(By.XPATH,"//*[@text='异星来客']")#作品名
    tvTitle=(By.ID,"com.qiwu.watch:id/tvTitle")#作品标题
    cbFavorite=(By.ID,"com.qiwu.watch:id/cbFavorite")#收藏按钮
    ivVolume=(By.ID,"com.qiwu.watch:id/saVolume")#音量键
    vVolumeDecrease=(By.ID,"com.qiwu.watch:id/saLessen")#音量减键
    vVolumeIncrease=(By.ID,"com.qiwu.watch:id/saAdd")#音量加键
    CheckBox=(By.CLASS_NAME,"android.widget.CheckBox")#显示文字
    tvWorksName1=(By.XPATH, "//*[@text='兔子成精']")  # 作品名

    def ivMicGuide_click(self):  # 点击麦克风
        self.click(self.ivMicGuide)

    # 断言“当线条跃动时”toast，由于不能键盘输入，这段时间要等待久一点，之后会进入到作品对话页

    def tvNpcName_click(self):  # 点击麦克风
        self.click(self.tvNpcName)

    def vRanking_click(self):  # 点击历练榜
        self.click(self.vRanking)

    def vAchievement_click(self):  # 点击我的成就
        self.click(self.vAchievement)

    def viewAsr_click(self):
        self.click(self.viewAsr)

    def viewIdle_click(self):
        self.click(self.viewIdle)

    def swipe(self):  # 向右滑动回到首页
        self.swipRight()

    def ivMenu_click(self):  # 点击菜单按钮
        self.click(self.ivMenu)

    def tvWorksName_click(self):  # 点击作品名
        self.click(self.tvWorksName)

    def tvTitle_click(self):  # 点击作品名
        self.click(self.tvTitle)

    def cbFavorite_click(self):  # 点击收藏
        self.click(self.cbFavorite)

    def ivVolume_click(self):  # 点击音量键
        self.click(self.ivVolume)

    def vVolumeDecrease_click(self):  # 点击音量减键
        self.click(self.vVolumeDecrease)

    def vVolumeIncrease_click(self):  # 点击音量加键
        self.click(self.vVolumeIncrease)

    def CheckBox_click(self):  # 点击显示文字
        self.click(self.CheckBox)

    def tvWorksName1_click(self):  # 点击排行榜野蛮女友
        self.click(self.tvWorksName1)