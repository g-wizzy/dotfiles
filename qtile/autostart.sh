#!/bin/bash

# Compton for transparency
# compton --config /home/pierre/.compton &
compton &

# Network applet
nm-applet &

# Albert launcher
albert &

# Wallpaper
feh --bg-scale /home/pierre/Pictures/Wallpapers/glitch.png &
