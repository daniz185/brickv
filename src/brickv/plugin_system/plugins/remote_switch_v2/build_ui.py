#!/usr/bin/env python3

import os

def system(command):
    if os.system(command) != 0:
        exit(1)

system("pyuic5 -o ui_remote_switch_v2.py ui/remote_switch_v2.ui")
