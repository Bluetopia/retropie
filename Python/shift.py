import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN_DATA=19
PIN_LATCH=6
PIN_CLOCK=5
PIN_OE=13

GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)
GPIO.setup(PIN_OE, GPIO.OUT)

def shiftout(byte):
	GPIO.output(PIN_LATCH, 0);
	for x in range(8):
		GPIO.output(PIN_DATA, (byte >> x) & 1)
		GPIO.output(PIN_CLOCK, 1)
		GPIO.output(PIN_CLOCK, 0)
	GPIO.output(PIN_LATCH, 1)


'''
    Player 1 (values turn OFF light):

        (128)   (64)

            (4)
    (1)     (8)     (16)
    (2)             (32)

    Player 2 (values turn OFF light)

        (128)   (64)
        
            (4)
    (16)    (8)     (1)
    (32)            (2)

'''
'''
[
    "2600" : (,)
    "NES" : (23, 53),   # A, B, Select, Start
    "SMS" : (23, 53),   # A, B, Select, Start
    "GB": (23, 53),     # A, B, Select, Start
    "GBA": (5, 20),     # A, B, L, R, Select, Start
    "GG": (151, 181),   # A, B, Start
    "SNES" : (0, 0)     # A, B, X, Y, L, R, Select, Start
]
'''

GPIO.output(PIN_OE, 0)

x = int(sys.argv[1])
y = int(sys.argv[2])

if x is not None:
    shiftout(x)

if y is not None:
    shiftout(y)

