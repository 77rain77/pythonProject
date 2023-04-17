import os
import time
import pytest
#import os,sys
if __name__== "__main__" :

    _name="RAIN"
    #sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    pytest.main()
    time.sleep(3)
    os.system('allure generate ./temp -o ./reports --clean')
    #os.system('allure open ./reports')
    #os.system('allure serve ./temp')
    #晓悟app逻辑：首次安装打开，进入个人信息保护指引，点击同意进入到登入界面，不同意则退出，到达登入界面之后登入成功则获取手机定位权限，存储权限
    #adb shell pm list packages查看手机上所有按照的包名
    #adb shell
    #dumpsys package com.qiwu.watch获取活动列表
    #weditor
    #com.qiwu.watch
    #com.qiwu.app.module.hostactivity.MfrMessageActivity
    #com.qiwu.app.module.MainActivity
    #com.qiwu.app.module.LaunchActivity
    #adb shell getprop ro.build.version.release  获取系统版本
    #[1283482648]!]
