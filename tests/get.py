
'''
data from rockblock
must be sent in this format:
datetime,field1,field2,field3,field4,field5,field6,field7,field8,latitude,longitude,elevation

field i can be anything you want

Rock7 sends test messages in a different way

in this code : the channel is
https://api.thingspeak.com/channels/1564907/feeds.json?api_key=8BLZ5AGLP8AL9H2L&results=2
'''

import requests

Thingspeak_Channel = 'https://api.thingspeak.com/channels/1564907/feeds.json?api_key=8BLZ5AGLP8AL9H2L&results=2'

status_channel = 'https://api.thingspeak.com/channels/1564907/status.json?api_key=8BLZ5AGLP8AL9H2L'

r = requests.get(Thingspeak_Channel)

if r.status_code == 200:
    print('success')
    print(r)