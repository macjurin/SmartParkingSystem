import RPi.GPIO as GPIO
import time


def irsensor2(sensor):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor, GPIO.IN)
    print("IR Sensor Ready.....")
    print(" ")

    while True:
        if GPIO.input(sensor):
            flag = 0
            while GPIO.input(sensor):
                time.sleep(0.2)
                if flag == 0:
                    flag = 1
                    print("Object Detected ")
            if flag == 1:
                return


    GPIO.cleanup()