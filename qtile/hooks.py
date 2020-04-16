from libqtile import hook
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call(["/home/pierre/.config/qtile/autostart.sh"])

@hook.subscribe.client_new
def albert_open(window):
    if window.name == "Albert":
        window.cmd_togroup()

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

@hook.subscribe.client_focus
def floating_focus(window):
    if window.floating:
        window.cmd_bring_to_front()