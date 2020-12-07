#!/bin/bash

# Compton for transparency
picom &

# Gnome Screensaver (so that it can be called with gnome-screensaver-command -l)
gnome-screensaver &

# Udiskie (no notifications, tray icon)
udiskie -N &

# Network applet
nm-applet &

# KDEConnect applet
kdeconnect-indicator &

# Albert launcher
albert &

# Wallpaper
# feh --bg-scale $HOME/Pictures/Wallpapers/eraserhead.png &
