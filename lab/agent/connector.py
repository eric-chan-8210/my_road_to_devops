import json
import smtplib
from netmiko import ConnectHandler
from email.mime.text import MIMEText
from email.header import Header

usermail = 'ronaldinho8210@tom.com'
mail_pass = '6yhnMJU&'
alert_mail = 'ronaldinho8210@hotmail.com'
smtp_server = 'smtp.tom.com'
smtp_port = '25'

class Net:
    def __init__(self, device_type, host, username, password):
        self.dev_info = {'device_type':device_type, 'host':host, 'username':username, 'password':password}

    def connect(self):
        return ConnectHandler(**self.dev_info)
    
    def reconnect(self):
        self.dev_conn.disconnect()
        self.dev_conn = self.connect()

    def to_json(self, data_source, file_path):
        with open(file_path, 'w') as f:
            json.dump(data_source, fp=f, indent=4)

    def send_mail(self, body, subject):
        message = MIMEText(body, 'html', 'utf-8')
        message['Subject'] = Header(subject, 'uft-8')
        message['From'] = usermail
        message['To'] = alert_mail
        sender = smtplib.SMTP(smtp_server, smtp_port)
        sender.login(usermail, mail_pass)
        sender.send_mail(usermail, alert_mail, message.as_string())
        sender.quit()
        
