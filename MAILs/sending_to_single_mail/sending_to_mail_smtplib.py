import os
import smtplib

receiver = 'sultonov25dilshod625@gmail.com'
sender = 'halimovhalimjon420@gmail.com'
password_nd = os.environ.get('python_smplib')
SMS = """Subject: HAVE EXTREMELY BEST DAY\n\n
HAVE A NICE DAY, MY BRO

About myself I am a good boy for only myself.
Only I have a huge amount of bad marks in every subject. I recommend you to improve your skills in each fields !!!
"""
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, password_nd)
server.sendmail(sender, receiver, SMS)
server.quit()
