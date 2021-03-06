

import imaplib
import email

USER = 'heimdallrock7'
PASS = 'thisisamomentarypass'

def process(data):

    '''
    convert hexstring to string of list then to list
    '''

    stringList = bytes.fromhex(data).decode("ASCII")
    list = eval(stringList)

    return list

def get_from_gmail():

    '''
    get email body
    get the Data field
    process the data into list
    '''

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
    
    if any("Data" in s for s in l):

        i = [idx for idx, s in enumerate(l) if 'Data' in s][0]
        Data = l[i][6:-2]

        # if no payload
        try:

            Data = process(Data)
            return Data

        except ValueError:
            return 'No payload'

    else:
        return 'No recent rockblock msg'

