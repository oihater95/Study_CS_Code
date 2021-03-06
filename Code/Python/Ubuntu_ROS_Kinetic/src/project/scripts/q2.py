#!/usr/bin/env python
# BEGIN ALL
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# BEGIN KEYMAP
key_mapping =      { 'w': [ 0, 0.1], 'x': [0, -0.1], 
                    'a': [ 0.3, 0], 'd': [-0.3, 0], 
                    's': [ 0, 0] }
# END KEYMAP

def scan_callback(msg):
    global g_range_ahead
    #g_range_ahead = min(msg.ranges)
    g_range_ahead = msg.ranges[0]
    print "range ahead: %0.2f" % g_range_ahead

    
    if(g_range_ahead<0.3):
        stop = Twist()
        stop.angular.z = 0
        stop.linear.x = 0
        cmd_vel_pub.publish(stop)
        

g_range_ahead = 1 # anything to start
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)





def keys_cb(msg, twist_pub):
    # BEGIN CB
    if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
            return # unknown key.
    vels = key_mapping[msg.data[0]]
    # END CB

    t = Twist()
    if(g_range_ahead<0.3):
        t.angular.z = 0
        t.linear.x = 0
    else:
        t.angular.z = vels[0]
        t.linear.x = vels[1]
    twist_pub.publish(t)



if __name__ == '__main__':
    rospy.init_node('keys_to_twist')
    twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('keys', String, keys_cb, twist_pub)
    rospy.spin()
