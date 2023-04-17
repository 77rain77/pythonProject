# coding=utf-8
import os
import subprocess
from datetime import datetime

#COMMAND = "adb logcat -v threadtime"  # 常量
COMMAND ="adb logcat -v time |find 'com.qiwu.watch'"
#COMMAND="adb shell logcat -v time"
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), "logs")
#print(log_path)
#object

class LogcatCathcher(object):
    def __init__(self):
        self.log_file = None
        self.hf = None
        self._create_hf()
        self.p_obj = subprocess.Popen(
            args=COMMAND,
            stdin=None, stdout=self.hf,
            stderr=self.hf, shell=False)

    def _create_hf(self):
        global now_time1
        now_time1 = datetime.now().strftime("%Y%m%d_%H%M%S")
        print(now_time1)
        os.system(r"del /q/a/f/s C:\Users\qiwu-PM\PycharmProjects\pythonProject\logs")
        self.log_file = os.path.join(log_path, "Logcat_" + now_time1 + ".txt")
        # 因为没指定具体路径，默认就是在当前脚本运行的路径下创建这个log_fil
        self.hf = open("%s" % self.log_file, "wb")

    def catch_logcat(self):
        self.p_obj.terminate()
        self.p_obj.kill()
        self.hf.close()  # 关闭文件句柄#
        # os.system('adb kill-server')
        return os.path.abspath(self.log_file)


#forfiles /S /D 0 /P "C:\Users\qiwu-PM\PycharmProjects\pythonProject\logs" /M "*" /C "cmd /C if @isdir==FALSE del @path"
#forfiles /S /D -90 /P "C:\Users\qiwu-PM\PycharmProjects\pythonProject\logs" /M "*" /C "cmd /C if @isdir==FALSE del @path"

if __name__ == '__main__':
    l_obj = LogcatCathcher()
    print("Logcat log has saved to %s" % l_obj.catch_logcat())
    os.system("pause")#暂停命令
    #print("停止进程")
