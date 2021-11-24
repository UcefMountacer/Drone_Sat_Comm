
'''
connection approach

connect to vehicle (simulated for now)
start a UDP connection to 127.0.0.1:10000 (qgc)

then :

start a listener on vehicle side
make a ping msg
send ping
# '''

import struct
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
from dronekit.mavlink import *
from pymavlink import mavlink
MAV = mavlink.MAVLink(0)


# connect to simulated vehicle on port 127.0.0.1:5760 
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

# start a mavlink upd 
udp_conn = MAVConnection('udpin:127.0.0.1:10000', source_system=1)

# connect the vehcile to this udp port
vehicle._handler.pipe(udp_conn)

# i don't know the reason for this but it's necessary
udp_conn.master.mav.srcComponent = 1  # needed to make QGroundControl work!

# start udp connection
udp_conn.start()

''' 
NOW we have (simulated drone) <========> UPD port 127.0.0.1:10000 <===> QGC

on QGC we connect to 127.0.0.1:10000
'''


while True:

    rejection_counter = 0
    # receive messages
    qgc_msg = udp_conn.master.recv_msg()

    # check if message is not None, or manual or hb (many of them)
    if qgc_msg == None : #or qgc_msg.get_type() == 'MANUAL_CONTROL' or qgc_msg.get_type() == 'HEARTBEAT':
        pass

    else:
        #msg received, send response to QGC
        print(qgc_msg)
        # ping = vehicle.message_factory.ping_encode(1000,1,255,1) # prepare a PING to QGC
        # vehicle.send_mavlink(ping)

        # print(qgc_msg._msgbuf)
        # MAVmsg = MAV.parse_buffer(qgc_msg._msgbuf)

        try:
            MAVmsglist = MAV.parse_buffer(qgc_msg._msgbuf)
        except:
            pass

        try:
            if MAVmsglist is not None:
                for msg in MAVmsglist:
                    if (msg.get_msgId() == 69):
                        rejection_counter += 1

                        if rejection_counter == 100:
                            rejection_counter = 0
                            print('Blocking MANUAL_CONTROL message')
                    print(msg)
                        
        except:
            pass


''' 
how to send the qgc_msg._msgbuf)
which is like array('B', [254, 11, 122, 2, 190, 69, 0, 0, 0, 0, 244, 1, 0, 0, 0, 0, 1, 12, 93])
'''
