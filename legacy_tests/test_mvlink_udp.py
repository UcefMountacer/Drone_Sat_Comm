
'''
to add : 

send_capabilties_request
play_tune
send_calibrate_gyro
send_calibrate_magnetometer

'''

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
from dronekit.mavlink import *

# just a way to communicate to qgc, have no importance
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

# start udp mavlink connection
udp_conn = MAVConnection('udpin:127.0.0.1:10000', source_system=1)

# same, for QGC
udp_conn.master.mav.srcComponent = 1

# connect vehicle to udp
vehicle._handler.pipe(udp_conn)

# start it
udp_conn.start()

#tested ,didn't work
#master = mavutil.mavlink_connection('udpout:127.0.0.1:10000', source_system=1)

while (True):

    #tested ,didn't work
    # master.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE,"QGC will read this".encode())

    # receive msg from qgc (the other part of the connection)
    qgc_msg = udp_conn.master.recv_msg()

    # check if message is not None
    if qgc_msg == None:
        pass

    else:
        print(qgc_msg)
        msg = vehicle.message_factory.command_long_encode(0,1,mavutil.mavlink)
        vehicle.send_mavlink(msg)

    
    
    







    # msg = mav.recv_match(blocking=True)
    # print(msg)
    # mav.mav.ping_send(int(time.time() * 1000), 0, 200, 1)

# mav = mavutil.mavlink_connection('udpin:127.0.0.1:10000')
# vehicle = mavutil.mavlink_connection('tcp:127.0.0.1:5760')

# gcs_conn.wait_heartbeat()
# print("Heartbeat from system (system %u component %u)" % (gcs_conn.target_system, gcs_conn.target_system))

# vehicle.wait_heartbeat() # recieving heartbeat from the vehicle
# print("Heartbeat from system (system %u component %u)" % (vehicle.target_system, vehicle.target_system))

# while True:
#             gcs_msg = gcs_conn.recv_match()
#             if gcs_msg == None:
#                 pass
#             else:
#                 vehicle.mav.send(gcs_msg)
#                 print(gcs_msg)

#             vcl_msg = vehicle.recv_match()
#             if vcl_msg == None:
#                 pass
#             else:
#                 gcs_conn.mav.send(vcl_msg)
#                 print(vcl_msg)