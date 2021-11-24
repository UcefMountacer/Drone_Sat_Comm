
import requests
import json


Thingspeak_Channel = 'https://api.thingspeak.com/channels/1564907/feeds.json?api_key=8BLZ5AGLP8AL9H2L&results=1'

r = requests.get(Thingspeak_Channel)

status = json.loads(r.text)['channel']
data = json.loads(r.text)['feeds'][0]  # a dictionary containing the fields with their values

print(r,'\n')
print(status, '\n')
print(data)