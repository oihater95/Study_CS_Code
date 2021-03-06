#!/usr/bin/env python
# Begin All
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Begin Keymap
key_mapping = { 'w':[0,1], 'x':[0,-1], 'a':[-1,0], 
                'd':[1,0], 's':[0,0] }   # velocity
# move gradually
g_twist_pub = None
g_target_twist = None
g_last_twist = None
g_last_send_time = None
g_vel_scales = [0.1, 0.1] # default to very slow
g_vel_ramps = [1,1] # units: meters per second^2

# Begin Ramp
def ramped_vel(v_prev, V_target, t_prev, t_now, ramp_rate):
    # compute maximum velocity step -> move gradually
    step = ramp_rate * (t_now - t_prev).to_sec()
    sign = 1.0 if (V_target > )v_prev else -1.0
    error = math.fabs(V_target - v_prev)
    if error < step: # we can get there within this timestep. we're done
        return V_target
    else:
        return v_prev + sign * step # take a step towards the target
# End Ramp

def ramped_twist(prev, target, t_prev, t_now, ramps):
    tw = Twist()
    tw.angular.z = ramped_vel(prev.angular.z, target.angular.z, t_prev, t_now, ramps[0])
    tw.linear.x = ramped_vel(prev.linear.x, target.linear.x, t_prev, t_now, ramps[1])
    return tw

def send_twist():
    global g_last_twist_send_time, g_target_twist, g_last_twist, g_vel_scales, g_vel_ramps, g_twist_pub
    t_now = rospy.Time.now()
    g_last_twist = ramped_twist(g_last_twist, g_target_twist, g_last_twist_send_time,t_now,g_vel_ramps)
    g_last_twist_send_time = t_now
    g_twist_pub.publish(g_last_twist)

def keys_cb(msg):
    global g_target_twist, g_last_twist, g_vel_scales