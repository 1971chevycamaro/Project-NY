#!/usr/bin/python
# -*- coding: utf-8 -*-
'''a module designed to control an RC car's steering with PWM signals corresponding to servo
angles'''

import json
import os

import pigpio

SCRIPT_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(SCRIPT_DIR, '../../settings.json')
DATA = json.load(open(FILE_PATH))

STRG = DATA['STRG']
PIN = (17 if not STRG['PIN'] else STRG['PIN'])
LEFT = (1800 if not STRG['LEFT'] else STRG['LEFT'])
RIGHT = (1200 if not STRG['RIGHT'] else STRG['RIGHT'])
CENTER = (1500 if not STRG['CENTER'] else STRG['CENTER'])

PI = pigpio.pi()


def set_steering(direction=CENTER, report_errors=True):
    '''sets steering to desired angle according to servo PWM'''

    if direction in range(1000, 2001):
        pwm = direction
        PI.set_servo_pulsewidth(PIN, pwm)
    else:

        # Error Handler

        if report_errors:
            print('direction is invalid or incorrect type %s' \
                % type(direction))


def get_steering():
    '''gets current steering angle in servo PWM'''

    return PI.get_servo_pulsewidth(PIN)
