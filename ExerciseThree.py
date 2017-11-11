import motion
import time
from naoqi import ALProxy

# Nao dvihne ruku zohnutu v lakti a a pohybuje laktom smerom ku a od hlavy


def stiffness_on(proxy):
    # We use the "Body" name to signify the collection of all joints
    p_names = "Body"
    p_stiffness_lists = 1.0
    p_time_lists = 1.0
    proxy.stiffnessInterpolation(p_names, p_stiffness_lists, p_time_lists)


def exercise_three(robot_ip, neutral, repeats):
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
    # Hands down at sides bent in elbow
    arm1 = [-15, 65, 70, -80, -15, -65, -70, 80]
    arm1 = [x * motion.TO_RAD for x in arm1]

    # Hands up at sides bent in elbow
    arm2 = [-15, 65, -70, -80, -15, -65, 70, 80]
    arm2 = [x * motion.TO_RAD for x in arm2]

    # Hands up at the front bent in elbow
    arm3 = [-15, 10, -70, -80, -15, -10, 70, 80]
    arm3 = [x * motion.TO_RAD for x in arm3]

    # Both hands down, neutral position
    arm4 = [85, 30, 0, -40, 85, -30, 0, 40]
    arm4 = [x * motion.TO_RAD for x in arm4]

    p_fraction_max_speed = 0.4

    for i in range(0, repeats):
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm1, p_fraction_max_speed)
        time.sleep(1.0)
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm2, p_fraction_max_speed)
        time.sleep(1.0)
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm3, p_fraction_max_speed)
        time.sleep(1.0)
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm2, p_fraction_max_speed)
        time.sleep(1.0)
        motion_proxy.angleInterpolationWithSpeed(joint_names, arm1, p_fraction_max_speed)
        time.sleep(1.0)
        if neutral and i == repeats - 1:
            motion_proxy.angleInterpolationWithSpeed(joint_names, arm4, p_fraction_max_speed)
