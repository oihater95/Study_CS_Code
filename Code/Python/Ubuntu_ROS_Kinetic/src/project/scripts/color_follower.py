#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
from sensor_msgs.msg import LaserScan

bridge = CvBridge()
g_twist = None

def img_callback(msg):
    img = bridge.compressed_imgmsg_to_cv2(msg, 'bgr8') # img load
    img_rotate = cv2.rotate(img, cv2.ROTATE_180)
    hsv = cv2.cvtColor(img_rotate, cv2.COLOR_BGR2HSV) # img convert rgb(bgr) -> hsv(hue, saturation, value)
    
    # hsv is robust in light

    lower_yellow = np.array([20,100,100]) # yellow range
    upper_yellow = np.array([30,255,255]) # yellow range
    # red -> [0,100,100] , [0,100,60]
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    h,w,d = img_rotate.shape
    search_top = 1*h/4
    search_bot = 1*h/4 +20
    # delete except for search_top ~ bot
    mask[0:search_top, 0:w] = 0
    mask[search_bot:h, 0:w] = 0

    M = cv2.moments(mask)
    if M['m00'] > 0:
        #search color_centerpoint
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(img_rotate, (cx,cy), 20, (0,0,255), -1)
        # distance color_centerpoint and center 
        err = cx - w/2
        
        if(min(g_range_ahead)<0.3):
            g_twist.angular.z = 0
            g_twist.linear.x = 0
        else:
            g_twist.angular.z = -float(err)/500 # follow color, +float(err) -> avoid color
            g_twist.linear.x = 0.03

        twist_pub.publish(g_twist)

        
        
        cv2.imshow('Line detected', img_rotate) # show processed result
        cv2.waitKey(3)

def scan_callback(msg):
    global g_range_ahead
    g_range_ahead = []
    #g_range_ahead = min(msg.ranges)
    for i in range(len(msg.ranges)/32):
        if msg.ranges[i] != 0:
            g_range_ahead.append(msg.ranges[i])
    for j in range(31*len(msg.ranges)/32, len(msg.ranges)):
        if msg.ranges[j] != 0:
            g_range_ahead.append(msg.ranges[j])
    print "range ahead: %0.2f"  % min(g_range_ahead)

    
    if(min(g_range_ahead)<0.3):
        stop = Twist()
        stop.angular.z = 0
        stop.linear.x = 0
        cmd_vel_pub.publish(stop)

g_range_ahead = 1 # anything to start
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

if __name__ == '__main__':
    img_topic= '/raspicam_node/image/compressed'
    
    rospy.init_node('line_follower')
    twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.Subscriber(img_topic, CompressedImage, img_callback)

    rate = rospy.Rate(10)
    g_twist = Twist()
    while not rospy.is_shutdown():
        twist_pub.publish(g_twist)
        rate.sleep()
    rospy.spin()