import motion
import time
from naoqi import ALProxy

# Nao striedavo rozpazuje a predpazuje obe ruky sucasne


def stiffness_on(proxy):
    # We use the "Body" name to signify the collection of all joints
    p_names = "Body"
    p_stiffness_lists = 1.0
    p_time_lists = 1.0
    proxy.stiffnessInterpolation(p_names, p_stiffness_lists, p_time_lists)


def stretch_arms(robot_ip, neutral, repeats):
    # Init proxies.
    try:
        motion_proxy = ALProxy("ALMotion", robot_ip, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
        return

    try:
        posture_proxy = ALProxy("ALRobotPosture", robot_ip, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
        return

    # Set NAO in Stiffness On
    stiffness_on(motion_proxy)

    # Send NAO to Pose Init
    posture_proxy.goToPosture("StandInit", 0.5)

    # Move with left hand
    joint_names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "RShoulderPitch",
                   "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    # Predpazenie
    arm1 = [-10,  0, 0, -10, 0, -10,  0, 0, 10, 0]
    arm1 = [x * motion.TO_RAD for x in arm1]
    # Rozpazenie
    arm2 = [-70,  70, -45, -10, -35, -70, -70, 45, 10, 35]
    arm2 = [x * motion.TO_RAD for x in arm2]
    # Both hands down
    arm3 = [85, 30, 0, -40, 0, 85, -30, 0, 40, 0]
    arm3 = [x * motion.TO_RAD for x in arm3]

    p_fraction_max_speed = 0.2

    for i in range(0, repeats):
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm1, p_fraction_max_speed)
        time.sleep(1.0)
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm2, p_fraction_max_speed)
        time.sleep(1.0)
        if neutral and i == repeats - 1:
            motion_proxy.angleInterpolationWithSpeed(joint_names, arm3, p_fraction_max_speed)
