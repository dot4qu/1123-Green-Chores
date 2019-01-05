from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == '__main__':
	from_addr = '1123greenchores@gmail.com'
	email_pass = 'washyourdishes0!'
	to_addrs = ['brian.team.jr@gmail.com']
	comma_char = ','
	message = MIMEMultipart()
	message['From'] = from_addr
	message['To'] = comma_char.join(to_addrs)
	message['Subject'] = "Chores email test"
	message.attach(MIMEText('test email message from smtplib w/ mime parts', 'plain'))

	smtp = SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(from_addr, email_pass)


	smtp.sendmail(from_addr,\
		to_addrs,\
		str(message))
	smtp.quit()