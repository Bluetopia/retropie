'''
    shift.py - Script to control LED buttons connected via 74HCT595 shift registers

    Usage:
        shift.py <system> <ROM path>

    Configuration Instructions:
        - create "runcommand-onstart.sh" script at /opt/retropie/configs/all
        - Add command calling this script:
            python <path/to/shift.py> "$1" "$3"

        - optionally, create a similar "runcommand-onend.sh" script to revert buttons
          when an emulator is closed

    Command line parameters provided by emulation station
        - $1 - system (atari2600, nes, etc)
        - $2 - emulator being called (lr-stella, lr-picodrive, etc)
        - $3 - full path to ROM file
        - $4 - full command line to launch emulator

'''

import RPi.GPIO as GPIO
import time
import sys
from emulators import emulators
from roms import roms

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

p1 = None
p2 = None

if len(sys.argv) >= 2:
    if sys.argv[1] is None or sys.argv[1] not in emulators:
        exit(1)

    p1 = emulators[sys.argv[1]][0]
    p2 = emulators[sys.argv[1]][1]

if len(sys.argv) == 3:
    rom = sys.argv[2].split("/")[-1]
    print(rom)
    if rom in roms:
        p1 = roms[rom][0]
        p2 = roms[rom][1]

GPIO.output(PIN_OE, 0)

if p2 is not None:
    shiftout(p2)

if p1 is not None:
    shiftout(p1)

