from __future__ import print_function
from threading import Thread
from time import sleep
import pymavlink.mavutil as mavutil
import sys
import time



mav = mavutil.mavlink_connection('udpout:' +  '127.0.0.1:10000')
mav.mav.ping_send(int(time.time() * 1000), 0, 200, 1)
