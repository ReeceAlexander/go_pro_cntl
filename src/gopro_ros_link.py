#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import subprocess

def callback(msg):
    if msg.linear.z == 1.0:
        subprocess.run(['bash', '-c', 'source gopro_env/bin/activate &&  /home/reece/catkin_ws/src/go_pro_cntl/src/gopro_ble_link.py'])
def main():
    rospy.init_node('ble_gopro_shutter_node')

    rospy.Subscriber('/cmd_vel', Twist, callback)

    rospy.spin()

if __name__ == "__main__":
    main()
