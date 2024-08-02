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
    dialog = window.window.get_wm_type() == "dialog"
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


# Steam dialog windows aren't detected as such
@hook.subscribe.client_new
def floating_steam(window):
    if window.name.startswith("Steam "):
        window.floating = True
