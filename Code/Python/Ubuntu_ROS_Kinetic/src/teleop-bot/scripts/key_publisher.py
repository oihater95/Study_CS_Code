#!/usr/bin/env python
import sys, select, tty, termios
import rospy
from std_msgs.msg import String

if __name__=='__main__':
    key_pub = rospy.Publisher('keys', String, queue_size=1)
    rospy.init_node("keyboard_driver")
    rate = rospy.Rate(100) # 100 Hz
    # Begin Termios
    old_attr = termios.tcgetattr(sys.stdin) # input save in var
    tty.setcbreak(sys.stdin.fileno())
    # End Termios
    print "Publishing keystrokes. Press Ctrl-C to exit..." # exe
    while not rospy.is_shutdown(): # while running rospy
        # Begin Select
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            key_pub.publish(sys.stdin.read(1))
        rate.sleep() #wait
        # End Select
    # Begin Termios_end
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
    # End Termios_end