from selenium.webdriver.common.by import By

from base.base_page import Bagepage


class menuone_Page_HuaweiWatch(Bagepage):
    homepage=(By.XPATH,"//*[@resource-id='com.qiwu.childwatch:id/rvMenu']/android.view.ViewGroup[1]/android.view.ViewGroup[1]")#主页
    #Ranking=(By.XPATH,"//*[@resource-id='com.qiwu.childwatch:id/rvMenu']/android.view.ViewGroup[2]/android.view.ViewGroup[1]")#排行榜
    Ranking = (By.XPATH, "//*[@text='排行榜']")
    #collect=(By.XPATH,"//*[@resource-id='com.qiwu.childwatch:id/rvMenu']/android.view.ViewGroup[3]/android.view.ViewGroup[1]")#收藏，新版本
    collect=(By.XPATH, "//*[@text='收藏']")
    #save=(By.XPATH,"//*[@resource-id='com.qiwu.childwatch:id/rvMenu']/android.view.ViewGroup[4]/android.view.ViewGroup[1]")#存档
    save=(By.XPATH, "//*[@text='存档']")
    #menu按钮没有id可以定位，只能用xpath方法，不准确，需要上滑才能实现，第三个也可以是新版本的点击按钮
    tvBottom=(By.ID,"com.qiwu.childwatch:id/tvBottom")#登入注册按钮,退出登入按钮
    cvBottom=(By.CLASS_NAME,"android.view.View")#取消登入按钮
    ivCodeLogin=(By.ID,"com.qiwu.childwatch:id/ivCodeLogin")#二维码图片
    #请使用微信扫码登入
    flDelete=(By.ID,"com.qiwu.childwatch:id/flDelete")#收藏界面删除按钮
    tvCancel=(By.ID,"com.qiwu.childwatch:id/tvCancel")#取消删除收藏
    tvConfirm=(By.ID,"com.qiwu.childwatch:id/tvConfirm")#确定删除收藏，确定删除昵称
    tvContent=(By.ID,"com.qiwu.childwatch:id/tvContent")#删除收藏作品名，text 野蛮女友-曼婷
    tvUserName=(By.ID,"com.qiwu.childwatch:id/tvUserName")#用户ID
    etContent=(By.ID,"com.qiwu.childwatch:id/etContent")#昵称输入框
    ivDelete=(By.ID,"com.qiwu.childwatch:id/ivDelete")#昵称输入框删除
    ImageView=(By.CLASS_NAME,"android.widget.ImageView")  # 弹出的警告
    vNationalRanking=(By.ID,"com.qiwu.childwatch:id/vNationalRanking")  # 全国榜
    tvTime=(By.ID,"com.qiwu.childwatch:id/tvTime")  # 每日00:30更新数据
    myid=(By.ID,"com.qiwu.childwatch:id/me")  # 我的
    ivRanking=(By.ID,"com.qiwu.childwatch:id/ivRanking")  # 全国榜排名

    def homepage_click(self):
        self.click(self.homepage)

    def ranking_click(self):
        self.click(self.Ranking)

    def collect_click(self):
        self.click(self.collect)

    def save_click(self):
        self.click(self.save)

    def tvbottom_click(self):
        self.click(self.tvBottom)

    def cvbottom_click(self):
        self.click(self.cvBottom)

    def flDelete_click(self):
        self.click(self.flDelete)

    def tvCancel_click(self):
        self.click(self.tvCancel)

    def tvConfirm_click(self):
        self.click(self.tvConfirm)

    def tvUserName_click(self):
        self.click(self.tvUserName)

    def etContent_click(self):
        self.click(self.etContent)

    def etContent_input(self,args,value):
        self.base_input(args,value)

    def ivDelete_click(self):
        self.click(self.ivDelete)



    def ImageView_pop(self):
        return self.isElementPresent(self.ImageView)