from naoqi import ALProxy;

def talk(IP, PORT):
    speechProxy = ALProxy("ALTextToSpeech", IP, PORT)
    speechProxy.say("Hi")

    print "finished"

def first_exercise(IP, PORT):
    postureProxy = ALProxy("ALRobotPosture", IP, PORT);
    postureProxy.goToPosture("Sit",0.5);

def main():
    IP = "192.168.0.108"
    PORT = 9559
    first_exercise(IP, PORT)

if __name__ == "__main__":
    main()