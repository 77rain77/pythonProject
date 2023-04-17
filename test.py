import time

from appium import webdriver
from pygame import mixer
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.config import Config


class TestEcshop():
    # caps = {}
    # caps["platformName"] = "Android"
    # caps["appium:deviceName"] = "4d06665b"
    # # caps["appium:noReset"] = "true"
    # caps["appium:appPackage"] = "com.qiwu.life"
    # caps["appium:appActivity"] = ".ui.activity.MainActivity"
    # # caps["appium:appActivity"] ="com.android.baselibrary.test.TestActivity"
    # # caps["appium:ensureWebviewsHavePages"] = True
    # # caps["appium:nativeWebScreenshot"] = True
    # # caps["appium:newCommandTimeout"] = 3600
    # # caps["appium:connectHardwareKeyboard"] = True
    # # caps['unicodeKeyboard'] = True  # 使用unicodeKeyboard的编码方式来发送字符串
    # # caps['resetKeyboard'] = True  # 将键盘给隐藏起来
    # # caps['noReset']=True
    # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    # time.sleep(3)
    # def always_allow(self, number=10):
    #     for i in range(number):
    #         if self.driver.getPageSource().contains("允许") and self.driver.getPageSource().contains(
    #                 "禁止") and self.driver.getPageSource().contains("授权"):
    #             try:
    #                 self.driver.findElement(By.xpath("//..[contains(@text,'允许')]")).click()
    #             except:
    #                 self.driver.findElement(By.xpath("//..[contains(@text,'授权')]")).click()
    #         else:
    #             break
    #date = time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))
    # def always_allow(self, number=2):
    #     # loc = (By.ID, "com.android.permissioncontroller:id/permission_allow_always_button")
    #     # loc = ('xpath',"//*[@text='始终允许']")
    #     # self.driver.find_element(*loc).click()
    #     loc = ('xpath', "//*[contains(@text,'始终允许')]")
    #     self.driver.find_element(*loc).click()
    #     OUTPUTS_DIR = '..\image'
    #     file_name = OUTPUTS_DIR + "\{}_{}.png"
    #     print(file_name)
    #     for i in range(number):
    #         loc1=(By.ID,"com.android.permissioncontroller:id/permission_allow_button")
    #         try:
    #             e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc1))
    #             e.click()
    #         except :
    #             print("adfa")
    # driver = Config()
    # driver=driver.devices(server="http://127.0.0.1:4723/wd/hub",path="\yaml\\vivonex_phone.yaml")
    # mixer.init()
    # mixer.music.load(r'C:\Users\qiwu-PM\PycharmProjects\pythonProject\music\y1169.mp3')  # 加载要播放的录音文件
    # mixer.music.play()  # 后台播放录音
    # #print("fsdjkahfkahfdkja")
    message = '//*[@text=\'{}\']'.format("yutuytuytu")  # Toast内容
    print(message)
    vVolumeIncrease = (By.ID, "com.qiwu.adultwatch:id/vVolumeIncrease")  # 音量加键
    print(vVolumeIncrease)


if __name__ == "__main__":
    # 调用始终允许函数
    a=TestEcshop()
    #a.always_allow()


#driver.quit()


