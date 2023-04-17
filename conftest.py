import os

import pytest
import yaml
#from ruamel import yaml
from base.chat import Chat

root_path1 = os.path.dirname(os.path.abspath(__file__))
print(root_path1)
#返回脚本上上层目录
root_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(root_path2)

@pytest.fixture()
def noreset(path=r"\yaml\xiaoxun_watch"):
    DESIRED_CAPS_YAML_PATH = root_path1 + path
    stream = open(DESIRED_CAPS_YAML_PATH, 'r', encoding='utf-8')
    data = yaml.load(stream, Loader=yaml.FullLoader)
    data['appium:noReset'] = True
    print(data)
    with open(DESIRED_CAPS_YAML_PATH, mode='w',encoding='utf-8') as f:
        f.truncate()#清除文件
    with open(DESIRED_CAPS_YAML_PATH, mode='a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)#写入文件
    # yield "分割线"
    # DESIRED_CAPS_YAML_PATH = root_path1 + path
    # stream = open(DESIRED_CAPS_YAML_PATH, 'r', encoding='utf-8')
    # data = yaml.load(stream, Loader=yaml.FullLoader)
    # data['appium:noReset'] = False
    # print(data)
    # with open(DESIRED_CAPS_YAML_PATH, mode='w', encoding='utf-8') as f:
    #     f.truncate()
    # with open(DESIRED_CAPS_YAML_PATH, mode='a', encoding='utf-8') as f:
    #     yaml.dump(data=data, stream=f, allow_unicode=True)



# if __name__ == '__main__':
#     aa=aa()
#     aa.noreset()
    #aa.bb()
