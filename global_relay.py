from operator import pos
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
from dronekit.mavlink import *
import requests


def post_to_rock7(msg):

    iridium_url = 'https://rockblock.rock7.com/rockblock/MT'
    iridium_local_port = 45679
    imei = '300434066803090'
    username = 'nicolai.valenti@gmail.com'
    password = 'thisisamomentarypass'

    data = msg.encode().hex()

    url = iridium_url + "?imei=" + imei + "&username=" + "nicolai.valenti%40gmail.com" + "&username=" + username + "&password=" + password + "&password=" + password +"&data=" + data
    headers = {"Accept": "text/plain"}
    response = requests.request("POST", url, headers=headers)

    if response.status_code == 200:
        print('success')


def get_from_TS():

    Thingspeak_Channel = 'https://api.thingspeak.com/channels/1564907/feeds.json?api_key=8BLZ5AGLP8AL9H2L&results=2'
    status_channel = 'https://api.thingspeak.com/channels/1564907/status.json?api_key=8BLZ5AGLP8AL9H2L'
    r = requests.get(Thingspeak_Channel)

    while r.status_code != 200:
        r = requests.get(Thingspeak_Channel)

    print('success')
    return r

def start_connection_QGC():

    udp_conn = MAVConnection('udpin:127.0.0.1:10000', source_system=1)
    ground_station = connect('tcp:127.0.0.1:5760', wait_ready=True)

def forward_to_QGC(msg):


    return


def forward_from_QGC():


    return


def serialize_to_mavlink(msg):


    return msg


def relay():

    '''
    must be in a loop
    let's say data cycle starts from rockblock sending a Hi message when booting
    '''

    msg = get_from_TS()
    msg = serialize_to_mavlink(msg)
    forward_to_QGC(msg)
    msg = forward_from_QGC()
    post_to_rock7()




    return