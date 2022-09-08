import RPi.GPIO as GPIO
import time


def irsensor1(sensor):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor, GPIO.IN)

    print("IR Sensor Ready.....")
    print(" ")
    try:
        if GPIO.input(sensor):
            print("Object Detected")
            return 1
        else:
            print("Object Not Detected")
            return 0
    except KeyboardInterrupt:
        GPIO.cleanup()


