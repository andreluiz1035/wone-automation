#!/usr/bin/env python

import imaplib
import email
import re


# Connect to imap server
username = 'andre.souza@vennecy.com.br'
password = '&qpoka11Py56@'
mail = imaplib.IMAP4_SSL('outlook.office365.com')
mail.login(username, password)

# retrieve a list of the mailboxes and select one
result, mailboxes = mail.list()
mail.select("inbox")

# retrieve a list of the UIDs for all of the messages in the select mailbox
result, numbers = mail.uid('search', None, 'ALL')
uids = numbers[0].split()

# retrieve the headers (without setting the 'seen' flag) of the last 10 messages
# in the list of UIDs
result, messages = mail.uid('fetch', ','.join(uids[-10:]), '(BODY.PEEK[HEADER])')

# Convert the messages into email message object and print out the sender and
# the subject.
for _, message in messages[::2]:
    msg = email.message_from_string(message)
#print('{}: {}'.format(msg.get('from'), msg.get('subject')))

#Extract from and subject fields
start = '<'
end = '>'
s = str(msg.get('from'))
print((s.split(start))[1].split(end)[0])
print(msg.get('subject'))





