#!/bin/bash

# Disable HDMI output
xrandr --output HDMI-0 --off

# Picom for transparency
picom -b

# xscreensaver (so that it can be called with xscreensaver-command -l)
xscreensaver --no-splash &

# Udiskie (no notifications, tray icon)
udiskie -N -t &

# Network applet
nm-applet &

# KDEConnect applet
kdeconnect-indicator &

# Redshift
redshift-gtk &
