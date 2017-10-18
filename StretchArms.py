import motion
from naoqi import ALProxy

# Nao striedavo rozpazuje a predpazuje obe ruky sucasne

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def strechArms(robotIP):
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

    # Move with left hand
    JointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
    # Predpazenie
    Arm1 = [-10,  0, 0, -10, 0]
    Arm1 = [ x * motion.TO_RAD for x in Arm1]
    # Rozpazenie
    Arm2 = [-70,  70, -45, -10, -75]
    Arm2 = [ x * motion.TO_RAD for x in Arm1]

    pFractionMaxSpeed = 0.5

    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)

    # Move with right hand
    JointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    # Predpazenie
    Arm1 = [-10,  0, 0, 10, 0]
    Arm1 = [ x * motion.TO_RAD for x in Arm1]
    # Rozpazenie
    Arm2 = [-10,  70, 45, 10, 75]
    Arm2 = [ x * motion.TO_RAD for x in Arm2]

    pFractionMaxSpeed = 0.5

    motionProxy.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
    motionProxy.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)
