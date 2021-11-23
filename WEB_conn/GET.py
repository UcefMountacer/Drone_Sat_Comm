
import requests
import json

def get_from_TS():

    Thingspeak_Channel = 'https://api.thingspeak.com/channels/1564907/feeds.json?api_key=8BLZ5AGLP8AL9H2L&results=2'
    status_channel = 'https://api.thingspeak.com/channels/1564907/status.json?api_key=8BLZ5AGLP8AL9H2L'
    r = requests.get(Thingspeak_Channel)

    while r.status_code != 200:
        r = requests.get(Thingspeak_Channel)

    dataDict = decode_TS_msg(r)

    return dataDict



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


# LEGACY

def decode_TS_msg(r):

    '''
    decode urllib message into dictionnary containing usable data
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
    # status = dataJson['channel']
    data = dataJson['feeds'][0]

    # decode status. Example below
    # dict_keys(['id', 'name', 'latitude', 'longitude',
    # 'field1','field8', 'created_at', 'updated_at', 'last_entry_id'])

    dataDict = {}

    dataDict['id'] = data['id']
    dataDict['transmit_time'] = data['field4']
    dataDict['lat'] = data['field5']
    dataDict['lat'] = data['field6']
    dataDict['data'] = decode(data['field8'])  # the mavlink command data list
                                                   

    return dataDict
