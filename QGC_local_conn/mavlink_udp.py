

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from dronekit.mavlink import *
from pymavlink import mavlink
from array import array
MAV = mavlink.MAVLink(0)


def start_qgc_connection(udp = '127.0.0.1:10000'):

    udp_conn = mavutil.mavlink_connection('udpout:' + udp, source_system=1)
    return udp_conn


def forward_to_QGC(MAVlink_msg_list, conn):

    '''
    send messages the mavlink message to QGC
    '''
    for msg in MAVlink_msg_list:
        conn.mav.send(msg)

    
def receive_from_QGC(udp_conn):

    '''
    receive mavlink messages from QGC through conn connection
    '''

    qgc_msg = udp_conn.recv_msg()

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

    return data 


def convert_to_MAVLink(data):

    '''
    convert message that is in a dict format
    to a mavlink command
    the actual command is in a dict key
    '''

    rejection_counter = 0
    MAVlink_msg_list = []

    MavArray = array('B',data)

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

