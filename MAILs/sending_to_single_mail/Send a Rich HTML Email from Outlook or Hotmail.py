import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

receiver = 'sultonov25dilshod625@gmail.com'
sender = 'halimovhalimjon420@gmail.com'
password_nd = os.environ.get('python_smplib')

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Hello world"

body = """
<h2>HAVE A NICE DAY, MY BRO</h2>

About myself I am a good boy for only myself.
Only I have a huge amount of bad marks in every subject. I recommend you to improve your skills in each fields !!!
"""

mime_text = MIMEText(body, 'html')
message.attach(mime_text)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, password_nd)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()
