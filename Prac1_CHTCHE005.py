#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Cheken Chetty
Student Number: CHTCHE005
Prac: Prac 1
Date: 27/07/2019
"""

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#initializing the ports and the pull up resistors

GPIO.setup(7, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#declaring variables

p = 0
counter = 0
c = 0
index = 0

#time delays to be replaced by commented out interrupts
#creating a button controller that checks if a button is pressed and value of counter isnt 7 and prints a 3 bit binary value

def buttoncontrol():
    global counter
    if(GPIO.input(15) == 1 and counter != 7):
        counter += 1
        print bin(counter)[2:].zfill(3)
        time.sleep(1)
        #GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)
        #GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_method(),bouncetime=300)

    if(GPIO.input(15) == 1 and counter == 7):
        counter = 0
        print bin(counter)[2:].zfill(3)
        time.sleep(1)
       #GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)
        #GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_method(),bouncetime=300)

    if(GPIO.input(16) == 1 and counter != 0):
        counter -= 1
        print bin(counter)[2:].zfill(3)
        time.sleep(1)
        #GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)
        #GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_method(),bouncetime=300)

    if(GPIO.input(16) == 1 and counter == 0):
        counter = 7
        print bin(counter)[2:].zfill(3)
        time.sleep(1)
        #GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)
        #GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)

#creating a logic fuction

def logic(c):
    bstring = bin(c)[2:].zfill(3)
    for index, value in enumerate(bstring):
        if (value == '1'):
             ledOn(index)
        else:
             ledOff(index)

#cases for leds being on

def ledOn(p):
     if (p == 0):
         GPIO.output(7, GPIO.HIGH)
     if (p == 1):
         GPIO.output(11, GPIO.HIGH)
     if (p == 2):
         GPIO.output(13, GPIO.HIGH)

#cases for led being off

def ledOff(p):
     if (p == 0):
         GPIO.output(7, GPIO.LOW)
     if (p == 1):
         GPIO.output(11, GPIO.LOW)
     if (p == 2):
         GPIO.output(13, GPIO.LOW)

#main that calls the linked functions

def main():
      buttoncontrol()
      logic(counter)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")

