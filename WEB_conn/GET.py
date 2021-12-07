

import imaplib
import email

USER = 'youssef.05.ex'
PASS = 'ex5556'

def get_from_gmail():

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    user = USER
    password = PASS
    mail.login(user+'@gmail.com', password)
    mail.list()

    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.
    result, data = mail.search(None, "ALL")
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
    # fetch the email body (RFC822) for the given ID
    result, data = mail.fetch(latest_email_id, "(RFC822)") 
    raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # including headers and alternate payloads
    email_message = email.message_from_string(str(raw_email))
    
    string = email_message.items()[0][1]
    l = string.split('\\n')
    Data = l[78][6:-2]

    return process(Data)


def process(data):

    '''
    convert hex to string of list then list
    '''
    stringList = bytes.fromhex(data).decode("ASCII")
    list = eval(stringList)

    return list