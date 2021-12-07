

from QGC_local_conn.mavlink_udp import *
from WEB_conn.GET import *
from WEB_conn.POST import *


if __name__ == "__main__":

    print('starting connection, make sure sitl vehicle is ready')

    conn = start_qgc_connection(udp = '127.0.0.1:10000')

    # starting communication from drone to QGC

    while 1:

        ROCK_msg_list = get_from_gmail()

        MAVlink_msg_list = convert_to_MAVLink(ROCK_msg_list)

        forward_to_QGC(MAVlink_msg_list, conn)

        QGC_msg = receive_from_QGC(conn)   # mavlink message
        
        post_to_rock7(QGC_msg)

        





