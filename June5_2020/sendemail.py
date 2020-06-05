# -*- coding: utf-8 -*-
"""sendemail

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YK88eXVdRXyr7bFlYf3twrYqcxylf_Eq
"""

from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="myemail@gmail.com"
    from_password="mypassword"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br> Thanks!" % (height, average_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)