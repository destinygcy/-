#!/usr/bin/env python
#-*- conding:utf-8 -*-

import rospy
from dobot.srv import SetHOMECmd
from dobot.srv import SetPTPCmd
from dobot.srv import SetEndEffectorSuctionCup

if __name__ == "__main__":
    rospy.init_node('testDobot')
    rospy.wait_for_service('DobotServer/SetPTPCmd')
    rospy.wait_for_service('DobotServer/SetHOMECmd')
    rospy.wait_for_service('DobotServer/SetEndEffectorSuctionCup')
    try:
        clienta = rospy.ServiceProxy('DobotServer/SetHOMECmd',SetHOMECmd)
        client = rospy.ServiceProxy('DobotServer/SetPTPCmd',SetPTPCmd)
        clients = rospy.ServiceProxy('DobotServer/SetEndEffectorSuctionCup',SetEndEffectorSuctionCup)
        response = clienta()
        response = client(0,-2.2,258,-45,-10)
        response = clients(1,1,True)
        response = client(0,-2.2,258,-10,-10)
        response = client(0,250,20,-45,-10)
        response = clients(0,1,True)
        response = client(0,250,20,-10,-10)
        response = client(0,-2.2,200,-55,-10)
        response = clients(1,1,True)
        response = client(0,-2.2,200,-10,-10)
        response = client(0,200,20,-55,-10)
        response = clients(0,1,True)
        response = client(0,200,20,10,-10)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
