
## $VERSION == 2.1.0
## LAST_UPDATE = 10/6/2025

import smtplib
from email.message import EmailMessage
import mimetypes
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

###############################################################################
## Sends an email using a gmail account, but the account must be set up 
##
## Parameters:
##   - user (string): the username of the gmail account to send from
##   - password (string): the password of the gmail account
##   - sendto (string): the email address to send the message to
##   - body (string): the text of the message
##   - subject (string): the subject title
##   - args (dict):
##       - reply-to (string): the default reply-to address if it is different
##           from the sending address
##       - attachment (string): the location of a file to attach to the message
##

def sendmail(user, password, sendto='', body='', subject='', args=None):

    msg = EmailMessage()
 
    msg['from'] = user
    msg['to'] = sendto
    msg['subject'] = subject
    
    msg.set_content(body)

    if args != None:

        if 'reply-to' in args.keys():
            msg['reply-to'] = args['reply-to']

        if 'attachment' in args.keys():
            filename = os.path.basename(args['attachment'])
            mime_type, encoding = mimetypes.guess_type(args['attachment'])
            mime_type, mime_subtype = mime_type.split('/', 1)

            with open(args['attachment'], 'rb') as file:
                msg.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=filename)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()
