import motion
import time
from naoqi import ALProxy

# Nao dvihne ruku zohnutu v lakti a a pohybuje laktom smerom ku a od hlavy

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def exerciseThree(robotIP, neutral):
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

    JointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"]
    # Hands down at sides bent in elbow
    Arm1 = [-15, 65, 70, -80, -15, -65, -70, 80]
    Arm1 = [x * motion.TO_RAD for x in Arm1]

    # Hands up at sides bent in elbow
    Arm2 = [-15, 65, -70, -80, -15, -65, 70, 80]
    Arm2 = [x * motion.TO_RAD for x in Arm2]

    # Hands up at the front bent in elbow
    Arm3 = [-15, 10, -70, -80, -15, -10, 70, 80]
    Arm3 = [x * motion.TO_RAD for x in Arm3]

    # Both hands down, neutral position
    Arm4 = [85, 30, 0, -40, 85, -30, 0, 40]
    Arm4 = [ x * motion.TO_RAD for x in Arm4]

    pFractionMaxSpeed = 0.4

    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    time.sleep(1.0)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)
    time.sleep(1.0)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm3, pFractionMaxSpeed)

    if neutral == True:
        time.sleep(1.0)
        motionProxy.angleInterpolationWithSpeed(JointNames, Arm4, pFractionMaxSpeed)