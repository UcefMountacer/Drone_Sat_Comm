

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from dronekit.mavlink import *
from pymavlink import mavlink
from array import array
MAV = mavlink.MAVLink(0)

def connect_to_relay_vehicle(address = '127.0.0.1:5760'):

    '''
    vehicle SITL instance to communicate with QGC locally
    Nothing less, nothing more

    address : str : ip address and port of SITL drone
            default : 127.0.0.1:5760
    '''

    vehicle = connect('tcp:' + address, wait_ready=True)
    return vehicle

def start_connection(relay_vehicle, udp = '127.0.0.1:10000'):

    '''
    start local connection between dummy vehicle
    and QGC
    '''

    udp_conn = MAVConnection('udpin:' + udp, source_system=1)
    udp_conn.master.mav.srcComponent = 1
    relay_vehicle._handler.pipe(udp_conn)
    udp_conn.start()

    return udp_conn

def forward_to_QGC(MAVlink_msg_list, relay_vehicle):

    '''
    send messages the mavlink message to QGC
    '''
    for msg in MAVlink_msg_list:
        relay_vehicle.send_mavlink(msg)

def receive_from_QGC(udp_conn):

    '''
    receive mavlink messages from QGC through conn connection
    '''

    qgc_msg = udp_conn.master.recv_msg()

    if qgc_msg != None:
        
        code = convert_msg(qgc_msg)

        return code

def convert_msg(msg):

    '''
    receive msg from QGC in mavlink 
    get msgbuf (byte array)
    send values
    '''

    try:
        Buffer = msg._msgbuf   # get buffer data (which construct the mavlink message)
        
    except:
        pass

    msgList = list(Buffer)         # get data list as a list of integers
    data = str(msgList)            # get string of list
    # code = data.encode().hex()     # encode as hex

    return data # send as string


def convert_to_MAVLink(data):

    '''
    convert message that is in a dict format
    to a mavlink command
    the actual command is in a dict key
    '''

    rejection_counter = 0
    MAVlink_msg_list = []

    MavList = data #msgDICT['data']
    MavArray = array('B',MavList)

    try:
        MavCommandList = MAV.parse_buffer(MavArray)
    except:
        pass

    try:
        if MavCommandList is not None:
            for msg in MavCommandList:
                if (msg.get_msgId() == 69):
                    rejection_counter += 1

                    if rejection_counter == 100:
                        rejection_counter = 0
                        print('Blocking MANUAL_CONTROL message')
                MAVlink_msg_list.append(msg)
    except:
        pass

    return MAVlink_msg_list


    
'''
LEGACY
'''
# def filter_QGC_msgs(qgc_msg):

#     if qgc_msg.get_type() == 'MANUAL_CONTROL':

#         print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
#         print("Message: %s" % qgc_msg)
#         print("\nAs dictionary: %s" % qgc_msg.to_dict())

#     if qgc_msg.get_type() == 'HEARTBEAT':

#         print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
#         print("Message: %s" % qgc_msg)
#         print("\nAs dictionary: %s" % qgc_msg.to_dict())

#     if qgc_msg.get_type() == 'MANUAL_CONTROL':

#         print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
#         print("Message: %s" % qgc_msg)
#         print("\nAs dictionary: %s" % qgc_msg.to_dict())

#     if qgc_msg.get_type() == 'MANUAL_CONTROL':

#         print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
#         print("Message: %s" % qgc_msg)
#         print("\nAs dictionary: %s" % qgc_msg.to_dict())

#         # + other things that depend on the actual filter
#         # make a function per filter
