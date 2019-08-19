import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

smtp_server = "p519990.mail.ihc.ru"
port = 25  # For starttls
sender_email = "aaa@lagunasun.ru"
receiver_email = 'dimalaga@mail.ru'
password = 'go4no4123'

message = ' 9834'

# Create a secure SSL context
context = ssl.create_default_context()

messagePlain = 'Visit nitratine.net for some great tutorials and projects!'
HTML = open('index.html')
messageHTML = HTML.read()
HTML.close()

msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Пример'

msg.attach(MIMEText(messagePlain, 'plain'))
#with open('preview.jpg', 'rb') as fp:
#    img = MIMEImage(fp.read())
#    print(img)
#msg.attach(img)
msg.attach(MIMEText(messageHTML, 'html'))

text = msg.as_string()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
