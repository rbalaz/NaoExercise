import motion
from naoqi import ALProxy

# Nao pohybuje pri vystretej nohe chodidlom

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def exerciseFour(robotIP):
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
    postureProxy.goToPosture("Sit", 0.5)

    # Stretching right leg
    JointNames = ["RKneePitch","RAnklePitch","RAnkleRoll"]
    Leg1 = [30, 0, -25]
    Leg2 = [10, 0, -50]
    # Missing neutral position -> need to read this from sit position

    pFractionMaxSpeed = 0.8

    motionProxy.angleInterpolationWithSpeed(JointNames, Leg1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Leg2, pFractionMaxSpeed)

    JointNames = ["LKneePitch","LAnklePitch","LAnkleRoll"]
    Leg1 = [30, 0, -25]
    Leg2 = [10, 0, -50]
    # Missing neutral position -> need to read this from sit position

    pFractionMaxSpeed = 0.8

    motionProxy.angleInterpolationWithSpeed(JointNames, Leg1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Leg2, pFractionMaxSpeed)