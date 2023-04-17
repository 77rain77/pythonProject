import os
import yaml
from appium.webdriver import webdriver
from appium import webdriver
class Config:
    # def __init__(self,driver):
    #     self.driver=driver
    # 返回该脚本的绝对路径
    # print(os.path.abspath(__file__))
    # 返回脚本上一层目录路径
    root_path1 = os.path.dirname(os.path.abspath(__file__))
    print(root_path1)
    #返回脚本上上层目录
    root_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(root_path2)
    #global path
    #print(DESIRED_CAPS_YAML_PATH)
    def devices(self,server,path):
        DESIRED_CAPS_YAML_PATH = self.root_path2 + path
        # 从desired_caps.yaml读取driver配置数据
        #server = "http://127.0.0.1:4723/wd/hub"
        stream = open(DESIRED_CAPS_YAML_PATH,'r',encoding='utf-8')
        data = yaml.load(stream, Loader=yaml.FullLoader)
        caps = {'platformName': data['platformName'], 'appium:deviceName': data['appium:deviceName'],
                'appium:noReset': data['appium:noReset'],'appium:fullReset': data['appium:fullReset'],
                'appium:appPackage': data['appium:appPackage'], 'appium:appActivity': data['appium:appActivity'],
                'appium:ensureWebviewsHavePages': data['appium:ensureWebviewsHavePages'],"appium:nativeWebScreenshot":data['appium:nativeWebScreenshot'],
                "appium:newCommandTimeout":data['appium:newCommandTimeout'],"appium:connectHardwareKeyboard":data['appium:connectHardwareKeyboard'],
                "unicodeKeyboard":data['unicodeKeyboard'],"resetKeyboard":data['resetKeyboard'],"automationName":data['automationName'],
                "skipServerInstallation":data['skipServerInstallation'],"skipDeviceInitialization":data['skipDeviceInitialization']}
        driver = webdriver.Remote(server, caps)
        print(caps)
        driver.implicitly_wait(8)
        return driver
        #stream.close()
#"\yaml\\vivonex_phone.yaml"


if __name__ == '__main__':
    aa=Config()
    aa.devices("http://127.0.0.1:4723/wd/hub",r"\yaml\\vivonex_phone.yaml")