from libqtile import hook
import subprocess, os

@hook.subscribe.startup_once
def autostart():
    path = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([path])

# Always display launcher in current group
@hook.subscribe.client_new
def albert_open(window):
    if window.name == "Albert":
        window.cmd_toscreen()

@hook.subscribe.client_focus
def focus_floating(window):
    if window.floating:
        window.cmd_bring_to_front()

# Prevent Albert from losing focus on mouse out
@hook.subscribe.client_focus
def albert_holds_focus(window):
    
    previous_focus = albert_holds_focus.current_focus
    albert_holds_focus.current_focus = window

    if (
        previous_focus
        and
        previous_focus.name == "Albert"
    ):
        previous_focus.cmd_focus()

albert_holds_focus.current_focus = None

@hook.subscribe.client_killed
def albert_dies(window):
    if window.name == "Albert":
        albert_holds_focus.current_focus = None

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
