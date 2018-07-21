# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
SUBJECT = '[ALERT] We detected an unfamiliar face. '
SENDER = 'iot.hackathon.2018@gmail.com'
PWD = 'uF2-3Qr-fZx-fmA'

def send(sender, recipients, imgfiles, subject=SUBJECT):
	# Create the container (outer) email message.
	msg = MIMEMultipart()
	msg['Subject'] = subject
	# sender == the sender's email address
	# recipients = the list of all recipients' email addresses
	msg['From'] = sender
	msg['To'] = COMMASPACE.join(recipients)
	msg.preamble = 'Camera captures below:'

	# Open the files in binary mode. Let the MIMEImage class automatically
    # guess the specific image type.
	for file in imgfiles:
		with open(file, 'rb') as fp:
			img = MIMEImage(fp.read())
		msg.attach(img)

	# Send the email via our own SMTP server.
	with smtplib.SMTP() as s:
		s.connect('smtp.gmail.com', '587')
		s.starttls()
		s.login(SENDER, PWD)
		s.send_message(msg)

if __name__ == '__main__':
	send('me', ['merlinyx@icloud.com'], ['cat.jpg'])
