import motion
import time
from naoqi import ALProxy

# Nao v sede vystiera jednu z noh


def stiffness_on(proxy):
    # We use the "Body" name to signify the collection of all joints
    p_names = "Body"
    p_stiffness_lists = 1.0
    p_time_lists = 1.0
    proxy.stiffnessInterpolation(p_names, p_stiffness_lists, p_time_lists)


def exercise_four(robot_ip, neutral, repeats, left):
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
    posture_proxy.goToPosture("Sit", 0.5)

    # Stretching right leg
    joint_names1 = ["LShoulderRoll", "RShoulderRoll"]
    arm1 = [60, -50]
    arm1 = [x * motion.TO_RAD for x in arm1]
    joint_names2 = ["LElbowRoll", "LShoulderPitch", "RElbowRoll", "RShoulderPitch"]
    arm2 = [-10, 110, 10, 110]
    arm2 = [x * motion.TO_RAD for x in arm2]
    joint_names3 = ["LShoulderRoll", "RShoulderRoll"]
    arm3 = [25, -25]
    arm3 = [x * motion.TO_RAD for x in arm3]
    joint_names4 = ["RKneePitch"]
    leg1 = [0]
    leg1 = [x * motion.TO_RAD for x in leg1]
    leg2 = [40]
    leg2 = [x * motion.TO_RAD for x in leg2]
    leg3 = [75]
    leg3 = [x * motion.TO_RAD for x in leg3]
    joint_names5 = ["LKneePitch"]

    p_fraction_max_speed_legs = 0.4
    p_fraction_max_speed_arms = 0.2

    motion_proxy.angleInterpolationWithSpeed(joint_names1, arm1, p_fraction_max_speed_arms)
    motion_proxy.angleInterpolationWithSpeed(joint_names2, arm2, p_fraction_max_speed_arms)
    motion_proxy.angleInterpolationWithSpeed(joint_names3, arm3, p_fraction_max_speed_arms)
    for i in range(0, repeats):
        if not left:
            motion_proxy.angleInterpolationWithSpeed(joint_names4, leg1, p_fraction_max_speed_legs)
            time.sleep(1.0)
            motion_proxy.angleInterpolationWithSpeed(joint_names4, leg2, p_fraction_max_speed_legs)
            time.sleep(1.0)
            motion_proxy.angleInterpolationWithSpeed(joint_names4, leg3, p_fraction_max_speed_legs)
            time.sleep(1.0)
        else:
            motion_proxy.angleInterpolationWithSpeed(joint_names5, leg1, p_fraction_max_speed_legs)
            time.sleep(1.0)
            motion_proxy.angleInterpolationWithSpeed(joint_names5, leg2, p_fraction_max_speed_legs)
            time.sleep(1.0)
            motion_proxy.angleInterpolationWithSpeed(joint_names5, leg3, p_fraction_max_speed_legs)
            time.sleep(1.0)

        if neutral and i == repeats - 1:
            motion_proxy.angleInterpolationWithSpeed(joint_names3, arm3, p_fraction_max_speed_arms)
            motion_proxy.angleInterpolationWithSpeed(joint_names2, arm2, p_fraction_max_speed_arms)
            motion_proxy.angleInterpolationWithSpeed(joint_names1, arm1, p_fraction_max_speed_arms)
            posture_proxy.goToPosture("Sit", 1)
