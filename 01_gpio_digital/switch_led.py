import RPi.GPIO as GPIO
import time

LED_PIN = 4
SWITCH_PIN = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up-down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN,val)

finally:
    GPIO.cleanup()
    print('cleanup and exit')
