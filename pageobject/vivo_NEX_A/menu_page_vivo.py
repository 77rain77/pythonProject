from selenium.webdriver.common.by import By
from base.base_page import Bagepage



class Menu_Page_Vivo(Bagepage):
    avatarView = (By.ID, "com.qiwu.watch:id/avatarView")  # 个人中心图标
    nameView = (By.ID, "com.qiwu.watch:id/nameView")  # 用户昵称或者作品名称
    bind_phone = (By.ID, "com.qiwu.watch:id/bind_phone")  # 绑定手机号
    llHistory = (By.ID, "com.qiwu.watch:id/llHistory")  # 历史记录按钮
    llFavorites = (By.ID, "com.qiwu.watch:id/llFavorites")  # 收藏按钮
    llRank = (By.ID, "com.qiwu.watch:id/llRank")  # 排行榜按钮
    llOrder = (By.ID, "com.qiwu.watch:id/llOrder")  # 我的订单按钮
    user_share = (By.ID, "com.qiwu.watch:id/user_share")  # 分享按钮
    check_update = (By.ID, "com.qiwu.watch:id/check_update")  # 检查更新按钮或者选择作品按钮
    install = (By.XPATH, '//*[contains(@text,"{}")]'.format("设置"))#设置按钮
    manage = (By.XPATH, '//*[contains(@text,"{}")]'.format("管理"))  # 管理按钮
    check_all = (By.ID, "com.qiwu.watch:id/check_all")  # 全选按钮
    delete = (By.ID, "com.qiwu.watch:id/delete")  # 删除按钮
    timeView = (By.ID, "com.qiwu.watch:id/timeView")  # 历史时间记录
    manage_out = (By.XPATH, '//*[contains(@text,"{}")]'.format("管理"))  # 退出管理按钮
    favorite_icon = (By.ID, "com.qiwu.watch:id/favorite_icon")  # 收藏按钮
    order = (By.XPATH, '//*[contains(@text,"{}")]'.format("暂无订单"))  # 暂无订单
    order_all = (By.XPATH, '//*[contains(@text,"{}")]'.format("全部订单"))  # 全部订单
    order_finish = (By.XPATH, '//*[contains(@text,"{}")]'.format("已完成"))  # 已完成
    install_1 = (By.XPATH, '//*[contains(@text,"{}")]'.format("系统权限设置"))  # 系统权限设置按钮
    install_2 = (By.XPATH, '//*[contains(@text,"{}")]'.format("意见与反馈"))  # 意见与反馈按钮
    install_3 = (By.XPATH, '//*[contains(@text,"{}")]'.format("关于晓悟互动小说"))  # 关于晓悟互动小说按钮
    install_4 = (By.XPATH, '//*[contains(@text,"{}")]'.format("用户协议"))  # 用户协议按钮
    install_5 = (By.XPATH, '//*[contains(@text,"{}")]'.format("隐私协议"))  # 隐私协议按钮
    install_6 = (By.XPATH, '//*[contains(@text,"{}")]'.format("退出登录"))  # 退出登录按钮
    navigationView = (By.ID, "com.qiwu.watch:id/navigationView")  # 返回按钮
    use_nick_name = (By.ID, "com.qiwu.watch:id/use_nick_name")  # 昵称修改按钮
    user_id = (By.ID, "com.qiwu.watch:id/user_id")  # 用户id
    inputNickNameView = (By.ID, "com.qiwu.watch:id/inputNickNameView")  # 昵称输入框
    confirmView = (By.ID, "com.qiwu.watch:id/confirmView")  # 确认修改昵称按钮 我已阅读按钮
    ImageView = (By.CLASS_NAME, "android.widget.ImageView")  # 昵称格式输入不正确，请重新输入提示
    title = (By.ID, "com.qiwu.watch:id/title")  # 我的页面主题



    def avatarView_click(self):  #点击个人中心图标
        self.click(self.avatarView)

    def nameView_locate(self):  #定位昵称或者作品名称
        self.locate_element(self.nameView)

    def bind_phone_click(self):  #点击绑定手机号
        self.click(self.bind_phone)

    def llHistory_click(self):  #点击历史记录按钮
        self.click(self.llHistory)

    def llFavorites_click(self):  #点击收藏按钮
        self.click(self.llFavorites)

    def llRank_click(self):  #点击排行榜按钮
        self.click(self.llRank)

    def llOrder_click(self):  #点击我的订单按钮
        self.click(self.llOrder)

    def user_share_click(self):  #点击分享按钮
        self.click(self.user_share)

    def check_update_click(self):  #点击检查更新按钮或者选择作品按钮
        self.click(self.check_update)

    def install_click(self):  #点击设置按钮
        self.click(self.install)

    def manage_click(self):  #点击管理按钮
        self.click(self.manage)

    def favorite_icon_click(self):  #点击收藏按钮
        self.click(self.favorite_icon)

    def order_all_click(self):  #点击全部订单按钮
        self.click(self.order_all)

    def order_finish_click(self):  #点击已完成
        self.click(self.order_finish)

    def install_1_click(self):  #点击系统权限设置按钮
        self.click(self.install_1)

    def install_2_click(self):  #点击意见与反馈按钮
        self.click(self.install_2)

    def install_3_click(self):  #点击关于互动小说按钮
        self.click(self.install_3)

    def install_4_click(self):  #点击用户协议按钮
        self.click(self.install_4)

    def install_5_click(self):  #点击隐私登入协议
        self.click(self.install_5)

    def install_6_click(self):  #点击退出登入
        self.click(self.install_6)

    def navigationView_click(self):  #点击返回按钮
        self.click(self.navigationView)

    def use_nick_name_click(self):  #点击昵称修改按钮
        self.click(self.use_nick_name)

    def user_id_locate(self):  #定位用户id
        self.locate_element(self.user_id)

    def inputNickNameView_click(self):  #点击昵称输入框
        self.click(self.inputNickNameView)

    def inputNickNameView_input(self, value):  # 输入昵称
        self.base_input(self.inputNickNameView, value)

    def confirmView_click(self):  #确认修改昵称
        self.click(self.confirmView)


