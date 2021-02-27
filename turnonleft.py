#!/usr/bin/env python3

import RPi.GPIO as GPIO

LEFT_TIRE = 17
RIGHT_TIRE = 18

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT_TIRE, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RIGHT_TIRE, GPIO.OUT, initial=GPIO.LOW)

def main():
    setup()
    GPIO.output(LEFT_TIRE, GPIO.LOW)
    GPIO.output(RIGHT_TIRE, GPIO.HIGH)

def end():
    GPIO.output(LEFT_TIRE, GPIO.LOW)
    GPIO.output(RIGHT_TIRE, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end()

        
