import motion
from naoqi import ALProxy

# Nao v sede vystiera jednu z noh

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
    JointNames1 = ["LShoulderRoll","RShoulderRoll"]
    Leg1 = [60,-50]
    Leg1 = [x * motion.TO_RAD for x in Leg1]
    JointNames2 =["LElbowRoll","LShoulderPitch","RElbowRoll","RShoulderPitch"]
    Leg2 = [-10,110,10,110]
    Leg2 = [x * motion.TO_RAD for x in Leg2]
    JointNames3= ["LShoulderRoll","RShoulderRoll"]
    Leg3 = [25,-25]
    Leg3 = [x * motion.TO_RAD for x in Leg3]
    JointNames4= ["RKneePitch"]
    Leg4 = [0]
    Leg4 = [x * motion.TO_RAD for x in Leg4]
    # Missing neutral position -> need to read this from

    pFractionMaxSpeed = 0.4

    motionProxy.angleInterpolationWithSpeed(JointNames1, Leg1, pFractionMaxSpeed)
    #postureProxy.goToPosture("Sit", 1)
    motionProxy.angleInterpolationWithSpeed(JointNames2, Leg2, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames3, Leg3, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames4, Leg4, pFractionMaxSpeed)

    JointNames = ["LKneePitch","LAnklePitch","LAnkleRoll"]
    Leg1 = [30, 0, 0]
    Leg2 = [10, 0, 0]
    # Missing neutral position -> need to read this from

    pFractionMaxSpeed = 0.8

    #motionProxy.angleInterpolationWithSpeed(JointNames, Leg1, pFractionMaxSpeed)
    #motionProxy.angleInterpolationWithSpeed(JointNames, Leg2, pFractionMaxSpeed)