from naoqi import ALProxy
import sys
import subprocess
from MoveArms import armsUpAndDown
from StretchArms import stretchArms
from ExerciseThree import exerciseThree
from ExerciseFour import exerciseFour

def get_IP():
    result = subprocess.check_output('ifconfig en0 |grep -w inet', shell=True)
    # result = None
    ip = ''
    if result:
        strs = result.split('\n')
        for line in strs:
            # remove \t, space...
            line = line.strip()
            if line.startswith('inet '):
                a = line.find(' ')
                ipStart = a+1
                ipEnd = line.find(' ', ipStart)
                if a != -1 and ipEnd != -1:
                    ip = line[ipStart:ipEnd]
                    break
    return ip

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

def tcp_comm(IP, PORT):
    import socket

    TCP_IP = IP
    TCP_PORT = PORT
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "received data:", data

def eyeLEDs(IP, PORT):
    ledProxy = ALProxy("ALLeds", IP, PORT)
    try:
        proxy = ALProxy("ALLeds", IP, PORT)
    except Exception, e:
        print "Could not create proxy to ALLeds"
        print "Error was: ", e
        sys.exit(1)

    # Example showing how to fade the ears group to mid-intensity
    name = 'EarLeds'
    intensity = 1.0
    duration = 5.0
    proxy.fade(name, intensity, duration)


def main():
    IP = "192.168.0.101"
    PORT = 9559
    #stand_init(IP,PORT)
    #sit(IP, PORT)
    #talk(IP,PORT)
    #armsUpAndDown(IP, True)
    #strechArms(IP, False)
    #exerciseThree(IP, True)
    #exerciseFour(IP, True)
    #eyeLEDs(IP, PORT)
    #tcp_comm(IP,PORT)
    #get_IP()

if __name__ == "__main__":
    main()