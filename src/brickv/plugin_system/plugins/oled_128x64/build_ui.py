#!/usr/bin/env python3

import os

def system(command):
    if os.system(command) != 0:
        exit(1)

system("pyuic5 -o ui_oled_128x64.py ui/oled_128x64.ui")
