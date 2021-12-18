'''
    shift.py - Script to control LED buttons connected via 74HCT595 shift registers

    Usage:
        shift.py <system> <ROM path>

    Configuration Instructions:
        - create "runcommand-onstart.sh" script at /opt/retropie/configs/all
        - Add command calling this script:
            python <path/to/shift.py> -e "$1" -r "$3"

        - optionally, create a similar "runcommand-onend.sh" script to revert buttons
          when an emulator is closed

    Command line parameters provided by emulation station
        - $1 - system (atari2600, nes, etc)
        - $2 - emulator being called (lr-stella, lr-picodrive, etc)
        - $3 - full path to ROM file
        - $4 - full command line to launch emulator

Button Mappings

            128     64                  128     64

        32      16      8           32      16      8
        4       2       1           4       2       1

'''

import RPi.GPIO as GPIO
import time
import sys
import argparse
from emulators import emulators
from roms import roms

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN_DATA=17
PIN_LATCH=22
PIN_CLOCK=27

GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def shiftout(byte):
	GPIO.output(PIN_LATCH, 0);
	for x in range(8):
		GPIO.output(PIN_DATA, (byte >> x) & 1)
		GPIO.output(PIN_CLOCK, 1)
		GPIO.output(PIN_CLOCK, 0)
	GPIO.output(PIN_LATCH, 1)

p1 = None
p2 = None

# Arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument('-p1', '--player1', nargs=1, type=int)
parser.add_argument('-p2', '--player2', nargs=1, type=int)
parser.add_argument('-e', '--emulator', nargs=1, type=str)
parser.add_argument('-r', '--rom', nargs=1, type=str)
parser.add_argument('-v', '--value', nargs=1, type=int)

args = parser.parse_args();

print(args)

if args.value is not None:
    p1 = args.value[0]
    p2 = args.value[0]

if args.emulator is not None:
    p1 = emulators[args.emulator[0]][0]
    p2 = emulators[args.emulator[0]][1]    

if args.rom is not None:
    rom = args.rom[0].split("/")[-1]
    print(rom)
    if rom in roms:
        p1 = roms[rom][0]
        p2 = roms[rom][1]

if args.player1 is not None:
    p1 = args.player1[0]

if args.player2 is not None:
    p2 = args.player2[0]

print("p1: " + str(p1))
print("p2: " + str(p2))
   
if p2 is not None:
    shiftout(p2)

if p1 is not None:
    shiftout(p1)

