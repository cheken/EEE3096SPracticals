#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Logic that you write
def main():
    input_state = GPIO.input(15)
    if (input_state == False):
        GPIO.output(7, GPIO.HIGH)
        time.sleep(2)
    output_state = GPIO.input(16)
    if (output_state == False):
        GPIO.output(7, GPIO.LOW)
        time.sleep(2)

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
