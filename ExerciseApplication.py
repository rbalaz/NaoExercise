import time
from naoqi import ALProxy
from MoveArms import arms_up_and_down
from StretchArms import stretch_arms
from ExerciseThree import exercise_three
from ExerciseFour import exercise_four


def main(ip, port):
    speech_proxy = ALProxy("ALTextToSpeech", ip, port)
    introduction_part1 = "Hello, I'm Chris and I'm your personal coach."
    introduction_part2 = "I will show you several exercises to help you stretch your hands, legs and body in general."
    introduction_part3 = "Before every exercise, I will describe it and demonstrate how to do it. You will only " \
                         "need to repeat my movements."
    first_exercise = "Lets start with the first exercise. It is very simple. You will be moving your hands up" \
                     " and down simultaneously. Watch how I do it."
    exercise_prompt = "Now try it yourself."

    confirmation_message5 = "Very good. Now repeat it five times."
    confirmation_message3 = "Very good. Now repeat it three times."
    denial_message = "Take a closer look how to perform the exercise."

    second_exercise = "Lets move on to second exercise. You will be simultaneously moving both of your" \
                      "hands at the front of your body and to the sides"

    third_exercise = "Lets move on to third exercise. Move your hands up and bent your hands in the " \
                     "elbow. After that, keep moving your hands from the side of your body to the front" \
                     "and vice versa."
    fourth_exercise_part1 = "For this exercise, I will need you to sit down. Now, straighten your right leg in the " \
                            "knee and then bent it back."
    fourth_exercise_part2 = "Now repeat it with your left leg"

    # Introduction
    speech_proxy.say(introduction_part1)
    speech_proxy.say(introduction_part2)
    speech_proxy.say(introduction_part3)
    # Exercising
    # First exercise
    stand_init(ip, port)
    exercise_finished = False
    subject_successfully_repeats = False
    while not exercise_finished:
        speech_proxy.say(first_exercise)
        while not subject_successfully_repeats:
            arms_up_and_down(ip, True, 1)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinect_confirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        arms_up_and_down(ip, True, 5)
        exercise_finished = True

    # Second exercise
    exercise_finished = False
    subject_successfully_repeats = False
    while not exercise_finished:
        speech_proxy.say(second_exercise)
        while not subject_successfully_repeats:
            stretch_arms(ip, True, 1)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinect_confirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        stretch_arms(ip, True, 5)
        exercise_finished = True

    # Third exercise
    exercise_finished = False
    subject_successfully_repeats = False
    while not exercise_finished:
        speech_proxy.say(third_exercise)
        while not subject_successfully_repeats:
            exercise_three(ip, True, 1)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinect_confirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message3)
        exercise_three(ip, True, 3)
        exercise_finished = True

    # Fourth exercise
    sit(ip, port)
    exercise_finished = False
    subject_successfully_repeats = False
    while not exercise_finished:
        speech_proxy.say(fourth_exercise_part1)
        while not subject_successfully_repeats:
            exercise_four(ip, True, 1, False)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinect_confirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        exercise_four(ip, True, 5, False)
        subject_successfully_repeats = False
        speech_proxy.say(fourth_exercise_part2)
        while not subject_successfully_repeats:
            exercise_four(ip, True, 1, True)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinect_confirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        exercise_four(ip, True, 5, True)
        exercise_finished = True


def kinect_confirmation():
    time.sleep(1.0)
    return True


def stand_init(ip, port):
    posture_proxy = ALProxy("ALRobotPosture", ip, port)
    posture_proxy.goToPosture("StandInit", 0.75)


def sit(ip, port):
    posture_proxy = ALProxy("ALRobotPosture", ip, port)
    posture_proxy.goToPosture("Sit", 0.5)


if __name__ == "__main__":
    robot_ip = "192.168.0.101"
    com_port = 9559
    main(robot_ip, com_port)
