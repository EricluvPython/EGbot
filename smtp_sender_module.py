import smtplib

from email.header import Header

from email.mime.text import MIMEText

import sys





def send_email(SMTP_host="smtp.163.com", from_account="yourname@163.com", from_passwd="yourpassword", to_account="anotheraccount@QQ.com", subject="EGBot Auto Reply", content="Test email"):

	email_client = smtplib.SMTP(SMTP_host)          # connect to host

	email_client.login(from_account, from_passwd)   # login to account

	# create msg

	msg = MIMEText(content, 'plain', 'utf-8')   # text-only email

	msg['Subject'] = Header(subject, 'utf-8')   # set subject

	msg['From'] = from_account      # sender mail

	msg['To'] = to_account          # receiver mail

	email_client.sendmail(from_account, to_account, msg.as_string())  # send the mail

	print("Email successfully sent!")

	

	email_client.quit()  # quit the client

 

if __name__ == '__main__':

	# usage: python3 smtp_sender_module.py [TO_ACCOUNT] [EMAIL_CONTENT]

	# input: 2 args: email sender, email body

	# output: 1 string: indicating mail successfully delivered

	to_account = sys.argv[1]	# email destination

	content = sys.argv[2]     	# email body

	send_email(to_account=to_account, content=content)

	sys.exit(0)
