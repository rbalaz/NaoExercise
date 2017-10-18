# -*- encoding: UTF-8 -*-

# Popis cviku: Nao pohybuje vystretymi rukami hore a dole
import motion
import time
from naoqi import ALProxy


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def armsUpAndDown(robotIP, neutral):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    JointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll","RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"]
    # Left hand up, right hand down
    Arm1 = [-85, 30, 0, -40, 85, -30, 0, 40]
    Arm1 = [ x * motion.TO_RAD for x in Arm1]

    # Right hand up, left hand down
    Arm2 = [85, 30, 0, -40, -85, -30, 0, 40]
    Arm2 = [ x * motion.TO_RAD for x in Arm2]

    # Both hands down, neutral position
    Arm3 = [85, 30, 0, -40, 85, -30, 0, 40]
    Arm3 = [ x * motion.TO_RAD for x in Arm3]

    pFractionMaxSpeed = 0.4

    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    time.sleep(1.0)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)
    if neutral == True:
        time.sleep(1.0)
        motionProxy.angleInterpolationWithSpeed(JointNames, Arm3, pFractionMaxSpeed)
