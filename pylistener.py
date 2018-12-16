#!/usr/bin/env python
#coding=utf-8
import rospy


from geometry_msgs.msg import Twist
from std_msgs.msg import String
import sys, select, termios, tty

#回调函数输入的应该是msg
def callback(data):
    
    rospy.loginfo(data)
    pub2 = rospy.Publisher('robot2/cmd_vel', Twist, queue_size=5)
    pub2.publish(data)
def listener():
    rospy.init_node('robot2', anonymous=True)
    #Subscriber函数第一个参数是topic的名称，第二个参数是接受的数据类型 第三个参数是回调函数的名称
    rospy.Subscriber('robot1/cmd_vel', Twist, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()

    
