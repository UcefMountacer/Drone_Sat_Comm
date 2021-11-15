
'''
connection approach

connect to vehicle (simulated for now)
start a UDP connection to 127.0.0.1:10000 (qgc)

then :

start a listener on vehicle side
make a ping msg
send ping
# '''

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
from dronekit.mavlink import *


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

    # receive messages
    qgc_msg = udp_conn.master.recv_msg()

    # check if message is not None
    if qgc_msg == None:
        pass

    else:
        #msg received, send response to QGC
        print(qgc_msg)
        ping = vehicle.message_factory.ping_encode(1000,1,255,1) # prepare a PING to QGC
        vehicle.send_mavlink(ping)

