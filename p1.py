import RPi.GPIO as GPIO
import time

def irsensor(sensor):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor, GPIO.IN)
    print("IR Sensor Ready.....")
    print(" ")
    i = 0

    while True:
        if GPIO.input(sensor):
            flag = 0
            while GPIO.input(sensor) and i < 100:
                time.sleep(0.2)
                if flag == 0:
                    flag = 1
                    print("Object Detected ")
                    return 0
                i = i + 1
        if i >= 100:
            break

    GPIO.cleanup()




