# -*- encoding: UTF-8 -*-

# Popis cviku: Nao pohybuje vystretymi rukami hore a dole
import motion
from naoqi import ALProxy


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def armsUpAndDown(robotIP):
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

    #####################
    ## Arms User Motion
    #####################
    # Arms motion from user have always the priority than walk arms motion
    JointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll"]
    Arm1 = [-65,  30, 0, -40]
    Arm1 = [ x * motion.TO_RAD for x in Arm1]

    Arm2 = [-65,  70, 0, -80]
    Arm2 = [ x * motion.TO_RAD for x in Arm2]

    Arm3 = [-65, 0, 0, -5]
    Arm3 = [ x* motion.TO_RAD for x in Arm3]

    pFractionMaxSpeed = 0.8

    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm3, pFractionMaxSpeed)

    #####################
    ## Arms User Motion
    #####################
    # Arms motion from user have always the priority than walk arms motion
    JointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"]
    Arm1 = [-65,  -30, 0, 40]
    Arm1 = [ x * motion.TO_RAD for x in Arm1]

    Arm2 = [-65,  -70, 0, 80]
    Arm2 = [ x * motion.TO_RAD for x in Arm2]

    Arm3 = [-65, 0, 0, 5]
    Arm3 = [ x* motion.TO_RAD for x in Arm3]

    pFractionMaxSpeed = 0.8

    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm3, pFractionMaxSpeed)
