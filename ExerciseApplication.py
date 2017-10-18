from naoqi import ALProxy
from MoveArms import armsUpAndDown
from StretchArms import strechArms
from ExerciseThree import exerciseThree
from ExerciseFour import exerciseFour

def main(IP, PORT):
    speechProxy = ALProxy("ALTextToSpeech", IP, PORT)
    introductionPart1 = "Hello, I'm Nao and I'm your personal coach."
    introductionPart2 = "I will show you several exercises to help you strech your hands, legs and body in general."
    introductionPart3 = "Before every exercise, I will describe it and demonstrate how to do it. You will only " \
                        "need to repeat my movements."
    firstExercise = "Lets start with the first exercise. It is very simple. You will be moving your hands up" \
                         " and down simultaneously. Watch how I do it."
    exercisePrompt = "Now try it yourself."

    confirmationMessage = "Very good. Now repeat it three times."
    denialMessage = "Take a closer look how to perform the exercise."

    secondExercise = "Lets move on to second exercise. You will be simultaneously moving both of your" \
                          "hands at the front of your body and to the sides"

    thirdExercise = "Lets move on to third exercise. Move your hands up and bent your hands in the " \
                    "elbow. After that, keep moving your hands from the side of your body to the front" \
                    "and vice versa."
    fourthExercisePart1 = "For this exercise, I will need you to sit down. Now, straighten your right leg in the " \
                     "knee and then bent it back."
    fourthExercisePart2 = "Now repeat it with your left leg"

    # Introduction
    speechProxy.say(introductionPart1)
    speechProxy.say(introductionPart2)
    speechProxy.say(introductionPart3)
    # Exercising
    exerciseFinished = False
    subjectSuccessfullyRepeats = False
    while exerciseFinished == False:
        speechProxy.say(firstExercise)
        while subjectSuccessfullyRepeats == False:
            speechProxy.say(exercisePrompt)
            subjectSuccessfullyRepeats = kinectConfirmation()
            if subjectSuccessfullyRepeats == False:
                speechProxy.say(denialMessage)
        speechProxy.say(confirmationMessage)
    exerciseFinished = False
    subjectSuccessfullyRepeats = False
    while exerciseFinished == False:
        speechProxy.say(secondExercise)
        while subjectSuccessfullyRepeats == False:
            speechProxy.say(exercisePrompt)
            subjectSuccessfullyRepeats = kinectConfirmation()
            if subjectSuccessfullyRepeats == False:
                speechProxy.say(denialMessage)
        speechProxy.say(confirmationMessage)
    exerciseFinished = False
    subjectSuccessfullyRepeats = False
    while exerciseFinished == False:
        speechProxy.say(thirdExercise)
        while subjectSuccessfullyRepeats == False:
            speechProxy.say(exercisePrompt)
            subjectSuccessfullyRepeats = kinectConfirmation()
            if subjectSuccessfullyRepeats == False:
                speechProxy.say(denialMessage)
        speechProxy.say(confirmationMessage)
    exerciseFinished = False
    subjectSuccessfullyRepeats = False
    while exerciseFinished == False:
        speechProxy.say(fourthExercisePart1)
        while subjectSuccessfullyRepeats == False:
            speechProxy.say(exercisePrompt)
            subjectSuccessfullyRepeats = kinectConfirmation()
            if subjectSuccessfullyRepeats == False:
                speechProxy.say(denialMessage)
        speechProxy.say(fourthExercisePart2)
        while subjectSuccessfullyRepeats == False:
            speechProxy.say(exercisePrompt)
            subjectSuccessfullyRepeats = kinectConfirmation()
            if subjectSuccessfullyRepeats == False:
                speechProxy.say(denialMessage)
        speechProxy.say(confirmationMessage)


def kinectConfirmation():
    return True


if __name__ == "__main__":
    IP = "192.168.0.107"
    PORT = 9559
    main(IP, PORT)