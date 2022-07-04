import getpass, email, sys

from imapclient import IMAPClient

import re, sys



def imap_receive(hostname='imap.163.com',username='yourname@163.com',passwd='yourpassword'):

	c = IMAPClient(hostname, ssl= True)  # create client object

	try:

		c.login(username, passwd)   # login to account

	except c.Error:

		print('Could not log in')   # in case anything goes wrong

		sys.exit(1)

	else:

		c.id_({"name": "IMAPClient", "version": "2.1.0"})   # to avoid "unsafe login" rejection

		c.select_folder('INBOX', readonly = False)          # load the mail inbox

		result = c.search('UNSEEN')                         # select the unseen mails

				

		msgdict = c.fetch(result, ['BODY.PEEK[]'] )	# a dictionary of the mail content to be processed

			

		

		for message_id, message in msgdict.items():     # this is set in case multiple emails are present

						

			message_decoded = {}			# decode dictionary from binary to utf8

			for key, value in message.items():      # iteration over all items

				try:

					new_key = key.decode('utf-8')       # decode the message to utf8

				except AttributeError:                  # in case anything is already in utf8

					new_key = key

				try:

					new_value = value.decode('utf-8')

				except AttributeError:

					new_value = value

				message_decoded[new_key] = new_value    # write decoded dictionary

			

			e = email.message_from_string(message_decoded['BODY[]'])                        # to find the value of the body			

			subject = email.header.make_header(email.header.decode_header(e['SUBJECT']))    # to find the email subject

			mail_from = email.header.make_header(email.header.decode_header(e['From']))     # to find the email sender			

			mail_from = ''.join(re.findall('<.*?>',str(mail_from)))[1:-1]			# match the email address

			

			maintype = e.get_content_maintype()     # in case the mail wasn't plain text

			if maintype == 'multipart':

				for part in e.get_payload():        # basically only take the text part

					if part.get_content_maintype() == 'text':

						mail_content = part.get_payload(decode=True).strip()

			elif maintype == 'text':

				mail_content = e.get_payload(decode=True).strip()        

			

			mail_content = mail_content.decode('utf-8')  # decode the message
			
			# NOTE: YOU NEED TO PRINT THE RECEIVED MESSAGE TO MANUALLY FIND WHERE THE EMAIL BODY IS
			
			dir1 = re.search('<div>',mail_content).span()[1]    # locate the first <div>

			dir2 = re.search('</div>',mail_content).span()[0]   # locate the first </div>

			mail_body = mail_content[dir1:dir2]  # print content between the first div tags

	

	c.add_flags(result, br'\Seen')	# mark emails as read

	c.logout()      		# logout

	

	try:

		return str(mail_from), str(mail_body), str(subject)

	except:

		return "","",""		# otherwise an error occurs when no new emails are found



if __name__ == "__main__":

	# usage: python3 imap_receiver_module.py

	# input: none

	# output: 3 strings: mail sender address, mail body, mail subject

	print(imap_receive())

	sys.exit(0)
