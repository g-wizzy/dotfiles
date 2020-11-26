from libqtile import hook
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call(["$HOME/.config/qtile/autostart.sh"])

# Always display launcher in current group
@hook.subscribe.client_new
def albert_open(window):
    if window.name == "Albert":
        window.cmd_togroup()

@hook.subscribe.client_focus
def focus_floating(window):
    if window.floating:
        window.cmd_bring_to_front()

# Prevent Albert from losing focus on mouse out
@hook.subscribe.client_focus
def albert_holds_focus(window):
    if (albert_holds_focus.last_focused and
        albert_holds_focus.last_focused.name == "Albert"):
        albert_holds_focus.last_focused.cmd_focus()
    else:
        albert_holds_focus.last_focused = window

albert_holds_focus.last_focused = None

@hook.subscribe.client_killed
def albert_dies(window):
    if window.name == "Albert":
        albert_holds_focus.last_focused = None

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
