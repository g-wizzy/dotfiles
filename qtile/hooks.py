from libqtile import hook, qtile

import subprocess, os

@hook.subscribe.startup_once
def autostart():
    path = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([path])

@hook.subscribe.client_focus
def focus_floating(window):
    if window.floating:
        window.bring_to_front()

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

# Steam dialog windows aren't detected as such
@hook.subscribe.client_new
def floating_steam(window):
    if window.name.startswith('Steam '):
        window.floating = True

# All groups default to Max Layout, but auto switch to BSP when a second window is added
@hook.subscribe.group_window_add
def handle_layout(group, window):
    if window.floating:
        return
    if group.name != "c":  # Exclude chat group
        if len(group.windows) == 0:
            group.layout = "max"
        else:
            group.layout = "bsp"

@hook.subscribe.client_killed
def handle_window_killed(window):
    if window.floating:
        return
    if window.group.name != "c":  # Exclude chat group
        if len(window.group.windows) <= 1:
            window.group.layout = "max"
        else:
            window.group.layout = "bsp"

@hook.subscribe.client_killed
def handle_slippi_closing(window):
    if window.name == "Faster Melee - Slippi (3.1.0)":
        subprocess.call(["xrandr", "--output", "DP-4", "--auto"])
