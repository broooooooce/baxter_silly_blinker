#!/usr/bin/env python

# Baxter Silly Face Blinker

# Bruce Stracener - University of Arkansas for Medical Sciences
# started 01/23/18

import rospy
import cv2
import cv_bridge
import random

from sensor_msgs.msg import Image

def blink():
    img = cv2.imread("SillyBlinkGray.jpg")
    msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="passthrough")
    pub.publish(msg)
    rospy.sleep(0.075)

if __name__ == '__main__':

    rospy.init_node('silly_face_blinker', anonymous=True)
    pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)

    images = ["SillySEGray.jpg", "SillySWGray.jpg", "SillyNWGray.jpg", "SillyNEGray.jpg"] 

    while not rospy.is_shutdown():

        x = random.randint(1,10)
        if x == 7:
            y = random.randint(1,4)            
            if y == 1:
                img = cv2.imread("SillyNEGray.jpg")
            if y == 2:    
                img = cv2.imread("SillyNWGray.jpg")
            if y == 3:
                img = cv2.imread("SillySEGray.jpg")
            msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="passthrough")
            pub.publish(msg)
            rospy.sleep(random.uniform(1.5,5.5))
            blink()            
        img = cv2.imread("SillySWGray.jpg")
        msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="passthrough")
        pub.publish(msg)
        rospy.sleep(random.uniform(1.5,5.5))
        blink()

