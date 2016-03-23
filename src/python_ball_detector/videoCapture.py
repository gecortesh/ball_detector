#!/usr/bin/env python

import numpy as np
import cv2

def video_capture(msg):
    bridge = CvBridge()
    try:	
        cv_image = bridge.imgmsg_to_cv2(msg, msg.encoding)
	cv2.waitKey(0)
    except CvBridgeError as e:
	print (e)
	cv2.waitKey(0)
        cv2.destroyAllWindows()
    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60:
	cv2.circle(cv_image, (50,50), 10,255)
    cv2.imshow('Image window',cv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
