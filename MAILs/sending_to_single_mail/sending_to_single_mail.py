import yagmail
import os
from datetime import datetime
import pandas as pd
from pathlib import Path

sender = 'sultonov25dilshod625@gmail.com'
receiver = 'halimovhalimjon420@gmail.com'

subject = "About true love"

content = """
HAVE A NICE DAY, MY BRO

About myself I am a good boy for only myself.
Only I have a huge amount of bad marks in every subject. I recommend you to improve your skills in each fields !!!
"""
yag = yagmail.SMTP(user=sender, password=os.environ.get('password_for_yamail_python'))


def send_sms_to_mail():
    yag.send(to=receiver, subject=subject, contents=content)
    print("Email send")


def send_twenty_min():
    yag.send(to=receiver, subject=subject, contents=content)
    time.sleep(15)
    send_twenty_min()


def send_by_everyday():
    if datetime.now().hour == 13 and datetime.now().minute == 15:
        yag.send(to=receiver, subject=subject, contents=content)
        time.sleep(60)
        send_by_everyday()


# --------------------------------------------------------------------------------------------------------------

def send_email_by_csv_file_readline_by_mr_sultonov():
    with open('contacts.csv', 'r') as file:
        lists = file.readlines()[1:]
        for i in lists:
            new_list = [i.split(',')][0]
            yag.send(to=new_list[1], subject=f'Hello {new_list[0]}', contents=content)


def send_email_by_csv_pandas_by_mr_sultonov_d():
    df = pd.read_csv('contacts.csv')
    for i, n in df.iterrows():
        yag.send(to=n['email'], subject=f"Hello {n['name']}", contents=content)


def send_email_by_csv_pandas_from_selected_files_by_mr_sultonov_d():
    root_dir = Path('files')

    df = pd.read_csv('contacts.csv')
    for i in root_dir.rglob('*.txt'):
        if i.is_file():
            df['path'] = i
    for i, n in df.iterrows():
        yag.send(to=n['email'], subject=f"Hello my new friend {n['name']}!!!", contents=[content, n['path']])


# --------------------------------------------------------------------------------------------------------------

def send_email_with_txt_files():
    df = pd.read_csv('contacts_more.csv')
    for i, n in df.iterrows():
        new_content = [f'''
        Hey, {n['name']}. You have to play {n['amount']}
        Dilshod is attached!''', 'file_01.txt']
        yag.send(to=n['email'], subject=subject, contents=new_content)


def send_email_with_txt_files_modernised():
    df = pd.read_csv('contacts_more.csv')
    for i, n in df.iterrows():
        with open(f'{n["name"]}.txt', 'w') as file:
            file.write(f"{n['amount']}")
        new_content = f'''
        Hey, {n['name']}. You have to play {n['amount']}
        Dilshod is attached!'''
        yag.send(to=n['email'], subject=subject, contents=[new_content, f'{n["name"]}.txt'])
