

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
from dronekit.mavlink import *

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

    udp_conn = MAVConnection('udpin:' + udp, source_system=1)
    udp_conn.master.mav.srcComponent = 1
    relay_vehicle._handler.pipe(udp_conn)
    udp_conn.start()

    return udp_conn

def forward_to_QGC(mav_msg, relay_vehicle):


    return

def forward_from_QGC(udp_conn):

    qgc_msg = udp_conn.master.recv_msg()

    if qgc_msg != None:
        return qgc_msg

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

def convert_to_MAVLink(msg):

    return