#!/usr/bin/env python
#coding=utf-8
import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String

import sys, select, termios, tty

def vels(target_linear_vel, target_angular_vel):
    return "currently:\tlinear vel %s\t angular vel %s " % (target_linear_vel,target_angular_vel)
def talker():
    #Publisher 函数第一个参数是话题名称，第二个参数 数据类型，现在就是我们定义的msg 最后一个是缓冲区的大小
    #queue_size: None（不建议）  #这将设置为阻塞式同步收发模式！
    #queue_size: 0（不建议）#这将设置为无限缓冲区模式，很危险！
    #queue_size: 10 or more  #一般情况下，设为10 。queue_size太大了会导致数据延迟不同步。
    
    #更新频率是1hz
    rospy.init_node('robot1', anonymous=True)
    pub = rospy.Publisher('robot1/cmd_vel', Twist, queue_size=5)
    rate = rospy.Rate(1) 
    status = 0
    t = 0
    target_linear_vel = 0
    target_angular_vel = 0
    control_linear_vel = 0
    control_angular_vel = 0
   
    try:
        while(1):
            while t <= 5:
                control_linear_vel = control_linear_vel
                t += 1
                time.sleep(1)
                target_linear_vel= 0.1
                target_angular_vel = 0
                twist = Twist()
                twist.linear.x = target_linear_vel
                twist.linear.y = 0
                twist.linear.z = 0
                twist.angular.x = 0
                twist.angular.y = 0
                twist.angular.z = target_angular_vel
                pub.publish(twist)
            while t <= 7:
                control_linear_vel = control_linear_vel
                t += 1
                time.sleep(1)
                target_linear_vel= 0.05
                target_angular_vel = 0 
                twist = Twist()
                twist.linear.x = target_linear_vel
                twist.linear.y = 0
                twist.linear.z = 0
                twist.angular.x = 0
                twist.angular.y = 0
                twist.angular.z = target_angular_vel
                pub.publish(twist)
            while t <= 9:
                control_linear_vel = control_linear_vel
                t += 1
                time.sleep(1)
                target_linear_vel= 0
                target_angular_vel = 0
                twist = Twist()
                twist.linear.x = target_linear_vel
                twist.linear.y = 0
                twist.linear.z = 0
                twist.angular.x = 0
                twist.angular.y = 0
                twist.angular.z = target_angular_vel
                pub.publish(twist)
            twist = Twist()
            twist.linear.x = target_linear_vel
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = target_angular_vel
            pub.publish(twist)
    finally:
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    twist = Twist()
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    pub.publish(twist)

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    talker()
    
