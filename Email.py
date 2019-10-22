import smtplib
from utils import log
from email.mime.text import MIMEText
from email.header import Header

class email:
    def __init__(self):
        self.hostname = "smtp.qq.com"
        self.hostport = 465
        self.username = ""
        self.passcode = ""
        self.sender_mail = ""
        self.receiver_mails = ""

    def build_msg(self, subject, content, receivers):
        msg = MIMEText(content, "plain", "utf-8")
        msg['subject'] = Header(subject, "utf-8")
        msg['From'] = self.sender_mail
        msg['To'] = ';'.join(receivers)
        return msg

    def send_mail(self, email):
        try:
            smtp = smtplib.SMTP_SSL(self.hostname, self.hostport)
            smtp.login(self.username, self.passcode)
            msg = self.build_msg(email['subject'], email['content'], self.receiver_mails)
            smtp.sendmail(self.sender_mail, self.receiver_mails, msg.as_string())
            log("Successfully send email from {} to {}".format(msg['From'], msg['To']))
            smtp.quit()
        except smtplib.SMTPException as e:
            log("Failed to send email")
            log(str(e))