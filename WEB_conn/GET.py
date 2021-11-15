
import requests


def get_from_TS():

    Thingspeak_Channel = 'https://api.thingspeak.com/channels/1564907/feeds.json?api_key=8BLZ5AGLP8AL9H2L&results=2'
    status_channel = 'https://api.thingspeak.com/channels/1564907/status.json?api_key=8BLZ5AGLP8AL9H2L'
    r = requests.get(Thingspeak_Channel)

    while r.status_code != 200:
        r = requests.get(Thingspeak_Channel)

    return r