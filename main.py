

from QGC_local_conn.mavlink_udp import *
from WEB_conn.GET import *
from WEB_conn.POST import *



if __name__ == "__main__":

    counter = 0
    print('starting connection to QGC \n')

    conn = start_qgc_connection(udp = '127.0.0.1:10000')

    while 1:

        ROCK_msg_list = get_from_gmail()

        MAVlink_msg_list = convert_to_MAVLink(ROCK_msg_list)

        sending_to_QGC = forward_to_QGC(MAVlink_msg_list, conn)

        QGC_msg = receive_from_QGC(conn)   

        posting_to_rock7 = post_to_rock7(QGC_msg)

        # print status
        print('step                          : ', counter)
        print('forwarding to QGC status      : ', bool(sending_to_QGC))
        print('sending to rockblock status   : ', bool(posting_to_rock7) , '\n')

        # delay 15 sec
        # time.sleep(15)
        counter = counter + 1

        





