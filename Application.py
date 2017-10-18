from naoqi import ALProxy
from MoveArms import armsUpAndDown
from StretchArms import strechArms
from ExerciseThree import exerciseThree
from ExerciseFour import exerciseFour

def talk(IP, PORT):
    speechProxy = ALProxy("ALTextToSpeech", IP, PORT)
    speechProxy.say("Hi")

    print "finished"

def stand_init(IP, PORT):
    postureProxy = ALProxy("ALRobotPosture", IP, PORT)
    postureProxy.goToPosture("StandInit", 0.5)

def sit(IP, PORT):
    postureProxy = ALProxy("ALRobotPosture", IP, PORT)
    postureProxy.goToPosture("Sit", 0.5)

def main():
    IP = "192.168.0.107"
    PORT = 9559
    #stand_init(IP,PORT)
    #sit(IP, PORT)
    #talk(IP,PORT)
    #armsUpAndDown(IP, True)
    #strechArms(IP, True)
    #exerciseThree(IP, True)
    exerciseFour(IP, True)

if __name__ == "__main__":
    main()