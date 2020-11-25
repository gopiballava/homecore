#!/bin/sh

# How to make it auto start:
# sudo vi /etc/xdg/lxsession/LXDE-pi/autostart

# File contents:
# @/home/automation/homecore/deployment/scripts/rv/pi_reversing.sh
# chromium-browser --kiosk http://localhost:8080

# Don't forget to pip3 install cherrypy


touch /tmp/pi_reversing_startup_checkpoint
cd /home/automation/homecore/python/ajax
screen -d -m python3 daemon.py

