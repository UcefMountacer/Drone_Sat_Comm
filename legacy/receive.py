

from __future__ import print_function
import pymavlink.mavutil as mavutil
import sys
import time

srcSystem = 200

mav = mavutil.mavlink_connection('udpin:' + '127.0.0.1:10000', source_system=srcSystem)

msg = mav.recv_match(blocking=True)

print("Message from %d: %s" % (msg.get_srcSystem(), msg))