#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import LaserScan


def scan_callback(msg):
    range_ahead = msg.ranges[len(msg.ranges)/2] # sensor pi/2 sensing
    #range_ahead = msg.ranges[0] -> 0 degree sensing
    # closet range = min(msg.ranges)
    print "range ahead: %0.1f" % range_ahead

# main
rospy.init_node('range_ahead') # node name definition
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
rospy.spin() # wait for next msg