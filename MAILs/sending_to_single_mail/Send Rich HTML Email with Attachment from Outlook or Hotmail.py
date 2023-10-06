import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

receiver = 'sultonov25dilshod625@gmail.com'
sender = 'halimovhalimjon420@gmail.com'
password_nd = os.environ.get('python_smplib')

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Hello world"

body = """
<h2 bg-color="red" >HAVE A NICE DAY, MY BRO</h2>


<h2>An Unordered HTML List</h2>

<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>  

<h2>An Ordered HTML List</h2>

<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol> 

<a href="https://www.kun.uz">kun.uz web sayti</a>

About myself I am a good boy for only myself.
Only I have a huge amount of bad marks in every subject. I recommend you to improve your skills in each fields !!!
"""

mime_text = MIMEText(body, 'html')
message.attach(mime_text)

attachment_path = 'tiger.jpeg'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attachment_file).read())
encoders.encode_base64(payload)
payload.add_header('Content-disposition', 'attachment', filename=attachment_path)

message.attach(payload)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, password_nd)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()
