import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import json
import datetime

json_file = open("data.json", encoding='utf-8')
data = json.loads(json_file.read())
json_file.close()



smtp_server = data["smtp_server"]
port = data['port']
sender_email = data['sender_email']
password = data['password']

timestamp = int(datetime.datetime.now().timestamp())


receiver_email = 'dimalaga@mail.ru'

message = 'Message {0}'.format(timestamp)


# messagePlain = 'Visit nitratine.net for some great tutorials and projects!'
HTML = open('index.html', encoding="utf-8")
messageHTML = HTML.read()
HTML.close()

msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Супер предложение {0}'.format(timestamp+1)

# msg.attach(MIMEText(messagePlain, 'plain'))
msg.attach(MIMEText(messageHTML, 'html'))

text = msg.as_string()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    # TODO: Send email here
except Exception as e:
    print(e)
finally:
    server.quit()
