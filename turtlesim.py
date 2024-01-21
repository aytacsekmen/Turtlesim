#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("pose_pub",anonymous=True)

odev1=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1000)

pose=Twist()
length_square=int(input("What is the length of edge of square?"))


r=rospy.Rate(2)
if __name__=="__main__":
    r.sleep()
    pose.linear.x=length_square
    pose.linear.y=0
    odev1.publish(pose)
    r.sleep()
    pose.linear.x=0
    pose.linear.y=length_square
    odev1.publish(pose)
    r.sleep()
    pose.linear.x=length_square*(-1)
    pose.linear.y=0
    odev1.publish(pose)
    r.sleep()
    pose.linear.x=0
    pose.linear.y=length_square*(-1)/2
    odev1.publish(pose)
    


    

