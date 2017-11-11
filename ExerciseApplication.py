import time
from naoqi import ALProxy
from MoveArms import armsUpAndDown
from StretchArms import stretchArms
from ExerciseThree import exerciseThree
from ExerciseFour import exerciseFour


def main(IP, PORT):
    speech_proxy = ALProxy("ALTextToSpeech", IP, PORT)
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
    stand_init(IP, PORT)
    exercise_finished = False
    subject_successfully_repeats = False
    while exercise_finished == False:
        speech_proxy.say(first_exercise)
        while subject_successfully_repeats == False:
            armsUpAndDown(IP, True, 1)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinectConfirmation()
            if subject_successfully_repeats == False:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        armsUpAndDown(IP, True, 5)
        exercise_finished = True

    # Second exercise
    exercise_finished = False
    subject_successfully_repeats = False
    while not exercise_finished:
        speech_proxy.say(second_exercise)
        while not subject_successfully_repeats:
            stretchArms(IP, True, 1)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinectConfirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        stretchArms(IP, True, 5)
        exercise_finished = True

    # Third exercise
    exercise_finished = False
    subject_successfully_repeats = False
    while not exercise_finished:
        speech_proxy.say(third_exercise)
        while not subject_successfully_repeats:
            exerciseThree(IP, True, 1)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinectConfirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message3)
        exerciseThree(IP, True, 3)
        exercise_finished = True

    # Fourth exercise
    sit(IP, PORT)
    exercise_finished = False
    subject_successfully_repeats = False
    while not exercise_finished:
        speech_proxy.say(fourth_exercise_part1)
        while not subject_successfully_repeats:
            exerciseFour(IP, True, 1, False)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinectConfirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        exerciseFour(IP, True, 5, False)
        subject_successfully_repeats = False
        speech_proxy.say(fourth_exercise_part2)
        while not subject_successfully_repeats:
            exerciseFour(IP, True, 1, True)
            speech_proxy.say(exercise_prompt)
            subject_successfully_repeats = kinectConfirmation()
            if not subject_successfully_repeats:
                speech_proxy.say(denial_message)
        speech_proxy.say(confirmation_message5)
        exerciseFour(IP, True, 5, True)
        exercise_finished = True


def kinectConfirmation():
    time.sleep(1.0)
    return True


def stand_init(IP, PORT):
    postureProxy = ALProxy("ALRobotPosture", IP, PORT)
    postureProxy.goToPosture("StandInit", 0.75)

def sit(IP, PORT):
    postureProxy = ALProxy("ALRobotPosture", IP, PORT)
    postureProxy.goToPosture("Sit", 0.5)

if __name__ == "__main__":
    IP = "192.168.0.101"
    PORT = 9559
    main(IP, PORT)