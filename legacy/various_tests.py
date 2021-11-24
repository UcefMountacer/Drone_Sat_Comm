
from __future__ import print_function
import pymavlink.mavutil as mavutil
import sys
import time

srcSystem = 2

mav = mavutil.mavlink_connection('udpin:' + '127.0.0.1:10000', source_system=srcSystem)

mav.wait_heartbeat()

mav.mav.command_long_send(mav.target_system, mav.target_component,
                          mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1,
                          0, 0, 0, 0, 0, 0)