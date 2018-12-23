#!/usr/bin/env python

import imaplib
import email
import mysql.connector


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

def extract (start, end, string):
   s =  ((string.split(start))[1].split(end)[0])
   return s; 

#Extract fields from email
email_client = (msg.get('from'))
subject = (msg.get('subject'))
client = (extract('<', '>', email_client))

email_request = (msg.get('subject'))
request = (extract('-', ':', email_request))

email_device = (msg.get('subject'))
device = (extract(':', ':', email_device))

#Connect to mysql and insert values from the client message
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="$1Vennecy$1",
  database="wone_automationdb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO input (client, device, request) VALUES (%s, %s, %s)"
val = (client, device, request)

mycursor.execute(sql, val)                     
mydb.commit()
mydb.close()











