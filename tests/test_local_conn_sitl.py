
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


while True:

    rejection_counter = 0
    # receive messages
    qgc_msg = udp_conn.master.recv_msg()

    # check if message is not None, or manual or hb (many of them)
    if qgc_msg == None : 
        pass

    else:
        #msg received, send response to QGC
        print(qgc_msg)
        ping = vehicle.message_factory.ping_encode(1000,1,255,1) # prepare a PING to QGC
        vehicle.send_mavlink(ping)

