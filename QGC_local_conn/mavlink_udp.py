

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from dronekit.mavlink import *
from pymavlink import mavlink
from array import array
MAV = mavlink.MAVLink(0)


def start_qgc_connection(udp = '127.0.0.1:10000'):

    udp_conn = mavutil.mavlink_connection('udpout:' + udp, source_system=1, source_component=1)
    return udp_conn


def forward_to_QGC(MAVlink_msg_list, udp_conn):

    '''
    send the mavlink messages list to QGC through udp connection
    '''
    if MAVlink_msg_list == 'No Mavlink':

        # Nothing
        return 0

    for msg in MAVlink_msg_list:
        udp_conn.mav.send(msg)
        return 1

    
def receive_from_QGC(udp_conn):

    '''
    receive mavlink messages from QGC through udp connection
    '''

    qgc_msg = udp_conn.recv_msg()

    if qgc_msg != None:
        
        code = convert_msg(qgc_msg)

        return code


def convert_msg(msg):

    '''
    get msgbuf (byte array) of mavlink msg
    as a list
    '''

    try:
        Buffer = msg._msgbuf        # get buffer data (which construct 
                                    # the mavlink message)
    except:
        pass

    msgList = list(Buffer)          # get data list as a list of integers
    data = str(msgList)             # get string of list

    return data                     # return string of list, use eval to get list again


def convert_to_MAVLink(stringList):

    '''
    convert message that is a string of list
    to a mavlink command
    '''

    if stringList == 'No payload' or stringList == 'No recent rockblock msg':
        # exit
        return 'No Mavlink'

    rejection_counter = 0                              # rejection counter 
                                                       # for manual control
    MAVlink_msg_list = []
    MavArray = array('B',stringList)                   

    try:
        MavCommandList = MAV.parse_buffer(MavArray)    # get messgaes   
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

