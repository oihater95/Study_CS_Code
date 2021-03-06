#!/usr/bin/env python
# Begin All
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Begin Keymap
key_mapping = { 'w':[0,1], 'x':[0,-1], 'a':[-1,0], 
                'd':[1,0], 's':[0,0] }   # velocity
# init -> stop -> start
g_last_twist = None

def keys_cb(msg, twist_pub):
    global g_last_twist
    if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
        return # unknown key
    vels = key_mapping[msg.data[0]]
    g_last_twist.angular.z = vels[0] # a d s
    g_last_twist.linear.x = vels[1]  # w x s
    twist_pub.publish(g_last_twist)

if __name__ == '__main__':
    rospy.init_node('keys_to_twist')
    twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('keys', String, keys_cb, twist_pub)
    # Begin Rate
    rate = rospy.Rate(10)
    g_last_twist = Twist() # initializes to zero
    while not rospy.is_shutdown():
        twist_pub.publish(g_last_twist)
        rate.sleep()
    # End Rate
# End all