#!/bin/bash

# Compton for transparency
#compton --config /home/pierre/.compton &
compton &

# Runs elecshot for screen capture
# /usr/local/lib/nodejs/bin/npm start --prefix /home/pierre/elecshot &

# Gnome screensaver allows to lock the screen at any time
# gnome-screensaver &

# Network applet
nm-applet &

# Cheap fix for unity hub
~/Applications/UnityHub*.AppImage
