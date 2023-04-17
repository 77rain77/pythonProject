import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
import os,sys
from email import encoders
from_addr = 'test@qiwu.ai'#发送邮箱
password = 'Abcd7777'#鉴权码
# 收信方邮箱
to_addr = 'chenyudie@qiwu.ai'#接收邮箱
# 发信服务器
smtp_server = 'smtp.exmail.qq.com'
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
#msg = MIMEText('my first email send by python','plain','utf-8')
msg = MIMEMultipart()
msg.attach(MIMEText('你们都是大佬，而我是个小垃圾……', 'plain', 'utf-8'))
msg['Subject']="教我写代码"
msg['From']=Header("test@qiwu.ai")#发件人邮箱
msg['To'] =Header("chenyudie@qiwu.ai")#收件人邮箱
att1=MIMEText(open('../reports/index.html','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'
att1['Content-Disposition']='attachment;filename="index.html"' #filename 填什么，邮件里边展示什么
msg.attach(att1)
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()

