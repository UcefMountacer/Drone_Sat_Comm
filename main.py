

'''
                  (DRONE)
(pixhawk) <==> (jetson Nano) <==> (rockblock) <*********> [Rock7]
                                                            ||
                                                            ||
                                                            ||
                            [Ground Station] <*******> [ThingSpeak]
                                   ||
                                   ||
                                   ||
                  (dummy vehicle) <==> (QGroundControl)               

'''


from QGC_local_conn.mavlink_udp import *
from WEB_conn.GET import *
from WEB_conn.POST import *


if __name__ == "__main__":

    print('starting connection, make sure sitl vehicle is ready')

    v = connect_to_relay_vehicle()
    conn = start_connection(v)

    # inititating communication between 2 parties
    print('posting a Hello Drone message to the drone')
    post_to_rock7('Hello Drone')
    print('awaiting response from drone')  # a hello back message 
                                           # to be programmed on the other board
    message = get_from_TS()
    print(message)

    # starting communication from drone to QGC

    while 1:

        ROCK_msg = get_from_TS()

        MAVlink_msg_list = convert_to_MAVLink(ROCK_msg)

        forward_to_QGC(MAVlink_msg_list, v)

        QGC_msg_HexCode = receive_from_QGC(conn)   # mavlink message
        
        post_to_rock7(QGC_msg_HexCode)

        # repeat


        





