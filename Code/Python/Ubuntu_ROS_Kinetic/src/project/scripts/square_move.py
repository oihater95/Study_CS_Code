#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('state')


go_state = Twist()
go_state.linear.x = 0.2
stop_state = Twist()
turn_state = Twist()
turn_state.angular.z = 1.52


driving_state = 0 
light_change_time = rospy.Time.now() 
rate = rospy.Rate(10) 

while not rospy.is_shutdown(): 
    if driving_state==1: 
        cmd_vel_pub.publish(go_state) 
    elif driving_state==2: 
        cmd_vel_pub.publish(stop_state) 
    elif driving_state==3: 
        cmd_vel_pub.publish(turn_state)

    if light_change_time < rospy.Time.now():
        driving_state +=1
        if driving_state>3:
            driving_state = 1
        light_change_time = rospy.Time.now() + rospy.Duration(1) 
    rate.sleep() 