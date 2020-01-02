import smtplib#构建smtp协议
import email#发送邮件
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header





# SMTP服务器,这里使用163邮箱
mail_host = "smtp.163.com"
# 发件人邮箱
mail_sender = "lhsfromcia@163.com"
# 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
mail_license = "rootroot666"
# 收件人邮箱，可以为多个收件人
mail_receivers = "578524983@qq.com"

mm = MIMEMultipart('related')

# 邮件主题
subject_content = """Python邮件测试"""
# 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
mm["From"] = "sender_name<lhsfromcia@163.com>"
# 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
mm["To"] = "receiver_1_name<578524983@qq.com>,receiver_2_name<mestorylhs@163.com>"
# 设置邮件主题
mm["Subject"] = Header(subject_content,'utf-8')

# 邮件正文内容
body_content = """你好，这是一个测试邮件！"""
# 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
message_text = MIMEText(body_content,"plain","utf-8")
# 向MIMEMultipart对象中添加文本对象
mm.attach(message_text)

# 二进制读取图片
image_data = open('./pictures/test1.jpg','rb')
atta = MIMEText(image_data.read(), 'base64', 'utf-8')
image_data.close()
# 设置读取获取的二进制数据


# 关闭刚才打开的文件

atta["Content-Disposition"] = 'attachment; filename="test1.jpg"'
# 添加图片文件到邮件信息当中去
mm.attach(atta)


# 构造附件
atta = MIMEText(open('./files/test001.txt', 'rb').read(), 'base64', 'utf-8')
# 设置附件信息
atta["Content-Disposition"] = 'attachment; filename="test001.txt"'
# 添加附件到邮件信息当中去
mm.attach(atta)

# 创建SMTP对象
stp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 25)
# set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
stp.login(mail_sender,mail_license)
# 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
# 关闭SMTP对象
stp.quit()











