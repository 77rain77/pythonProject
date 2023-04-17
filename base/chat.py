import os
import yaml
from appium.webdriver import webdriver
from appium import webdriver
class Chat:
    root_path1 = os.path.dirname(os.path.abspath(__file__))
    #print(root_path1)
    # 返回脚本上上层目录
    root_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(root_path2)
    def chat(self,path):
        DESIRED_CAPS_YAML_PATH = self.root_path2 + path
        # 从desired_caps.yaml读取driver配置数据
        #server = "http://127.0.0.1:4723/wd/hub"
        stream = open(DESIRED_CAPS_YAML_PATH,'r',encoding='utf-8')
        data = yaml.load(stream, Loader=yaml.FullLoader)
        print(data)
        return data



if __name__ == '__main__':
    aa = Chat()
    aa.chat(r"\yaml\\xiaoxun_watch")
