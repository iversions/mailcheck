import smtplib
import imaplib
import os
import pprint
import base64
import email
from email.header import decode_header
import time


luser = 'demoacc8413@gmail.com'
lpass = 'polxonghdxqwleeq'

sServer = "imap.gmail.com"
nImap = imaplib.IMAP4_SSL(sServer)
nImap.login(luser,lpass)
nImap.select('INBOX')

nImap.recent()

type,data = nImap.search(None,'(UNSEEN)' ,'(SUBJECT "email test")')
mailIds = data[0]
idList = mailIds.split()

for num in data[0].split():
    type,data = nImap.fetch(num,'(RFC822)')
    rawEmail = data[0][1]
    rawEmailString = rawEmail.decode('utf-8')
    emailMessage = email.message_from_string(rawEmailString)
    for part in emailMessage.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('/document',fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

nImap.close()
