

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

while 1:
    
    qgc_msg = udp_conn.master.recv_msg()

    # check if message is not None
    if qgc_msg == None:
        pass

    elif qgc_msg.get_type() == 'MANUAL_CONTROL':
        print("\n\n*****Got message: %s*****" % qgc_msg.get_type())
        print("Message: %s" % qgc_msg)
        print("\nAs dictionary: %s" % qgc_msg.to_dict())
        # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
        # print("\nSystem status: %s" % qgc_msg.system_status)



    
    
    






