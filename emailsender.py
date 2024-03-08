#import smtplib
#from email.message import EmailMessage
#from string import Template
#from pathlib import Path

#html = Template(Path('index.html').read_text())
#email = EmailMessage()
#email['from'] = 'Sibi Sambasivam'
#email['to'] = 'sibisambasivam2@gmail.com'
#email['subject'] = 'You are going to get hired this month.'

#email.set_content(html.substitute({'name' = 'TinTin'}), 'html')

#with smtplib.SMTP(host='smtp.gmail.com' port=587) as smtp:
#	smtp.ehlo()
#	smtp.starttls()
	#smtp.login('email id', 'password') Write your email id and password here
#	smtp.send_message(email)
#	print('All Good Boss!')