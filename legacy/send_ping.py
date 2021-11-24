
# from __future__ import print_function
# import pymavlink.mavutil as mavutil
# import sys
# import time



# mav = mavutil.mavlink_connection('udpin:' + '127.0.0.1:10000', source_system=20, source_component=10)

# mav.wait_heartbeat()

# while True:
#     mav.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_QUADROTOR,
#                            mavutil.mavlink.MAV_AUTOPILOT_INVALID,
#                            0, 0, 0)
#     print(".", end="")
#     sys.stdout.flush()
#     time.sleep(1)

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
from dronekit.mavlink import *

vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

udp_conn = MAVConnection('udpin:127.0.0.1:10000', source_system=1)

vehicle._handler.pipe(udp_conn)

udp_conn.master.mav.srcComponent = 1  # needed to make QGroundControl work!

udp_conn.start()

# vehicle.add_message_listener('PING', 2)   # qgc id = 2

msg1 = vehicle.message_factory.ping_encode(1000,1,255,1) # prepare a PING to QGC

vehicle.send_mavlink(msg1)    # send the PING to QGC