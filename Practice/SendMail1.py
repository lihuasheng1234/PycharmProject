import smtplib#构建smtp协议
import email#发送邮件
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText):

        strFrom = fromAdd
        strTo = ', '.join(toAdd)

        server = "smtp.163.com"
        mail_sender = "lhsfromcia@163.com"
        mail_sender = "lhsfromcia@163.com"


        # 设定root信息
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        #设定纯文本信息
        msgText = MIMEText(plainText, 'plain', 'utf-8')
        msgAlternative.attach(msgText)

        #设定HTML信息
        msgText = MIMEText(htmlText, 'html', 'utf-8')
        msgAlternative.attach(msgText)

       #设定内置图片信息
        fp = open('test.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

       #发送邮件
        smtp = smtplib.SMTP()
       #设定调试级别，依情况而定
        smtp.set_debuglevel(1)
        smtp.connect(server)
        smtp.login(mail_sender, mail_sender)
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        smtp.quit()
        return


mail_receivers = ["578524983@qq.com","mestorylhs@163.com"]
sender = '***'
receiver = ["578524983@qq.com","mestorylhs@163.com"]
subject = 'python email test'
smtpserver = 'smtp.163.com'
username =  "lhsfromcia@163.com"
password = "rootroot666"

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!','html','utf-8')
msgRoot.attach(msgText)

fp = open('./pictures/test1.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(username, receiver, msgRoot.as_string())
smtp.quit()
