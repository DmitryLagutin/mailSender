import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


from email.mime.multipart import MIMEMultipart
import json
import datetime
from time import sleep

# получаем данные об аккаунте из json файла
json_file = open("data.json", encoding='utf-8')
data = json.loads(json_file.read())
json_file.close()

# получаем все email адреса для рассылки
f = open('res_emails.txt', 'r', encoding='utf-8')
emails = f.readlines()
f.close()

smtp_server = data["smtp_server"]
port = data['port']
sender_email = data['sender_email']
password = data['password']

timestamp = int(datetime.datetime.now().timestamp())

receiver_email = 'dimalaga@mail.ru'
message = 'Message {0}'.format(timestamp)


HTML = open('index.html', encoding="utf-8")
messageHTML = HTML.read()
HTML.close()


server = smtplib.SMTP(smtp_server, port)
server.ehlo()
server.login(sender_email, password)
try:
    for email in emails:
        timestamp1 = int(datetime.datetime.now().timestamp())
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Супер предложение {0}'.format(timestamp1 + 1)
        msg.attach(MIMEText(messageHTML, 'html'))
        text = msg.as_string()
        server.sendmail(sender_email, email, text)
        sleep(data['sleep'])


except Exception as e:
    print("Что то пошло не так!")
finally:
    server.quit()
