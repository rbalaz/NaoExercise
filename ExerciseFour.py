import motion
import time
from naoqi import ALProxy

# Nao v sede vystiera jednu z noh

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def exerciseFour(robotIP, neutral, repeats, left):
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
    JointNames1 = ["LShoulderRoll", "RShoulderRoll"]
    Arm1 = [60, -50]
    Arm1 = [x * motion.TO_RAD for x in Arm1]
    JointNames2 =["LElbowRoll", "LShoulderPitch", "RElbowRoll", "RShoulderPitch"]
    Arm2 = [-10, 110, 10, 110]
    Arm2 = [x * motion.TO_RAD for x in Arm2]
    JointNames3 = ["LShoulderRoll", "RShoulderRoll"]
    Arm3 = [25, -25]
    Arm3 = [x * motion.TO_RAD for x in Arm3]
    JointNames4 = ["RKneePitch"]
    Leg1 = [0]
    Leg1 = [x * motion.TO_RAD for x in Leg1]
    Leg2 = [40]
    Leg2 = [x * motion.TO_RAD for x in Leg2]
    Leg3 = [75]
    Leg3 = [x * motion.TO_RAD for x in Leg3]
    JointNames5 = ["LKneePitch"]

    pFractionMaxSpeedLegs = 0.4
    pFractionMaxSpeedArms = 0.2

    motionProxy.angleInterpolationWithSpeed(JointNames1, Arm1, pFractionMaxSpeedArms)
    motionProxy.angleInterpolationWithSpeed(JointNames2, Arm2, pFractionMaxSpeedArms)
    motionProxy.angleInterpolationWithSpeed(JointNames3, Arm3, pFractionMaxSpeedArms)
    for i in range(0, repeats):
        if not left:
            motionProxy.angleInterpolationWithSpeed(JointNames4, Leg1, pFractionMaxSpeedLegs)
            time.sleep(1.0)
            motionProxy.angleInterpolationWithSpeed(JointNames4, Leg2, pFractionMaxSpeedLegs)
            time.sleep(1.0)
            motionProxy.angleInterpolationWithSpeed(JointNames4, Leg3, pFractionMaxSpeedLegs)
            time.sleep(1.0)
        else:
            motionProxy.angleInterpolationWithSpeed(JointNames5, Leg1, pFractionMaxSpeedLegs)
            time.sleep(1.0)
            motionProxy.angleInterpolationWithSpeed(JointNames5, Leg2, pFractionMaxSpeedLegs)
            time.sleep(1.0)
            motionProxy.angleInterpolationWithSpeed(JointNames5, Leg3, pFractionMaxSpeedLegs)
            time.sleep(1.0)

        if neutral and i == repeats - 1:
            motionProxy.angleInterpolationWithSpeed(JointNames3, Arm3, pFractionMaxSpeedArms)
            motionProxy.angleInterpolationWithSpeed(JointNames2, Arm2, pFractionMaxSpeedArms)
            motionProxy.angleInterpolationWithSpeed(JointNames1, Arm1, pFractionMaxSpeedArms)
            postureProxy.goToPosture("Sit", 1)