import smtplib
from utils import log, EmailConfigException, valid_addr
from email.mime.text import MIMEText
from email.header import Header

class email:
    def __init__(self, hostname, hostport, username, passcode, sender_mail, receiver_mails):
        if hostname == "" or (0 < hostport <= 65535) is False:
            log("Hostname and host port is invalid. Check config file.")
            raise EmailConfigException
        if username == "" or passcode == "":
            log("Username and passcode is invalid. Check config file.")
            raise EmailConfigException
        if valid_addr(sender_mail) is False:
            log("Invalid sender email. Check config file.")
            raise EmailConfigException
        for receiver in receiver_mails:
            if valid_addr(receiver) is False:
                log("Invalid receiver email. Check config file.")
                raise EmailConfigException
        self.hostname = hostname
        self.hostport = hostport
        self.username = username
        self.passcode = passcode
        self.sender_mail = sender_mail
        self.receiver_mails = receiver_mails

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