from email.message import EmailMessage
import ssl, smtplib
from credential import password

email_sender = 'edoghotugiddy@gmail.com'
email_password = password
# email_receiver = 'edoghotugiddy@gmail.com'
email_receiver = 'tebesan761@wisnick.com'


subject = "Dont forget to subscribe"
body = '''
When you watch a video, please hit subscribe
Thank you
'''

em = EmailMessage()
em['From'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
