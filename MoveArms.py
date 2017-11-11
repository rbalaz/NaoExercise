# -*- encoding: UTF-8 -*-

# Popis cviku: Nao pohybuje vystretymi rukami hore a dole
import motion
import time
from naoqi import ALProxy


def stiffness_on(proxy):
    # We use the "Body" name to signify the collection of all joints
    p_names = "Body"
    p_stiffness_lists = 1.0
    p_time_lists = 1.0
    proxy.stiffnessInterpolation(p_names, p_stiffness_lists, p_time_lists)


def arms_up_and_down(robot_ip, neutral, repeats):
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

    joint_names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "RShoulderPitch",
                   "RShoulderRoll", "RElbowYaw", "RElbowRoll"]
    # Left hand up, right hand down
    arm1 = [-85, 30, 0, -40, 85, -30, 0, 40]
    arm1 = [x * motion.TO_RAD for x in arm1]

    # Right hand up, left hand down
    arm2 = [85, 30, 0, -40, -85, -30, 0, 40]
    arm2 = [x * motion.TO_RAD for x in arm2]

    # Both hands down, neutral position
    arm3 = [85, 30, 0, -40, 85, -30, 0, 40]
    arm3 = [x * motion.TO_RAD for x in arm3]

    p_fraction_max_speed = 0.4

    for i in range(0, repeats):
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm1, p_fraction_max_speed)
        time.sleep(1.0)
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm2, p_fraction_max_speed)
        time.sleep(1.0)
        if neutral and i == repeats - 1:
            motion_proxy.angleInterpolationWithSpeed(joint_names, arm3, p_fraction_max_speed)
