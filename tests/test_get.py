
import requests
import json

def decode_TS_msg(r):

    '''
    decode urllib message into data for mavlink buffer
    '''

    def decode(hexstring):

        '''
        decode a hex string into ascii string
        '''

        string = bytes.fromhex(hexstring)
        stringList = string.decode("ascii")
        List = eval(stringList)

        return List

    ''' decode the whole msg'''
    dataJson = json.loads(r.text)
    data = dataJson['feeds'][0]

    mavData = decode(data['field8'])  # the mavlink command data list
                                                   
    return mavData

Thingspeak_Channel = 'https://api.thingspeak.com/channels/1564907/feeds.json?api_key=8BLZ5AGLP8AL9H2L&results=1'

r = requests.get(Thingspeak_Channel)

status = json.loads(r.text)['channel']
data = json.loads(r.text)['feeds'][0]  # a dictionary containing the fields with their values

# print(r,'\n')
# print(status, '\n')
# print(data)

d = decode_TS_msg(r)

print(d)

