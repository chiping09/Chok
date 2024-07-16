import smtplib

message = """From: From joe <joe@blow.com>
To: To chiping <chiping@chiping-vmware-virtual-platform.com>
MINE-version: 1.0
Content-type: text/html
Subject: Test HTML Email

This is an email message sent as HTML
<b>This is a test HTML Message.</b>
<h1>This is Headling </h1>
"""
try:
    smtp = smtplib.SMTP("192.168.207.131")
    smtp.sendmail("chiping@chiping-vmware-virtual-platform.com","chiping@chiping-vmware-virtual-platform.com", message)
    print("Email sent successfully")
except Exception as err:
    print(str(err))