

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
        
        code = convert_msg_to_hexcode(qgc_msg)

        return code

def convert_msg_to_hexcode(msg):

    '''
    LEGACY
    takes msg from QGC in dict format 
    {'mavpackettype': 'TERRAIN_DATA', 'lat': -353747690, 'lon': 1491554539, 'grid_spacing': 100, 'gridbit': 0, 'data': [635, 627, 626, 626, 630, 623, 621, 622, 623, ...]}
    return msg that can be sent to rockblock
    '''

    # LEGACY
    # dict_msg = msg.to_dict()
    # data = str(dict_msg)
    # code = data.encode().hex()

    '''
    receive msg from QGC in mavlink 
    get msgbuf (byte array)
    send values
    '''

    try:
        Buffer = msg._msgbuf
        # MAVmsglist = MAV.parse_buffer(msg._msgbuf)
        # MAVmsglist is an python array.array('B',[10,2,5,...])
    except:
        pass

    msgList = list(Buffer)
    data = str(msgList)
    code = data.encode().hex()

    return code


def convert_to_MAVLink(msgDICT):

    '''
    convert message that is in a dict format
    to a mavlink command
    the actual command is in a dict key
    '''

    rejection_counter = 0
    MAVlink_msg_list = []

    MavList = msgDICT['data']
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
def filter_QGC_msgs(qgc_msg):

    if qgc_msg.get_type() == 'MANUAL_CONTROL':

        print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
        print("Message: %s" % qgc_msg)
        print("\nAs dictionary: %s" % qgc_msg.to_dict())

    if qgc_msg.get_type() == 'HEARTBEAT':

        print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
        print("Message: %s" % qgc_msg)
        print("\nAs dictionary: %s" % qgc_msg.to_dict())

    if qgc_msg.get_type() == 'MANUAL_CONTROL':

        print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
        print("Message: %s" % qgc_msg)
        print("\nAs dictionary: %s" % qgc_msg.to_dict())

    if qgc_msg.get_type() == 'MANUAL_CONTROL':

        print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
        print("Message: %s" % qgc_msg)
        print("\nAs dictionary: %s" % qgc_msg.to_dict())

        # + other things that depend on the actual filter
        # make a function per filter
