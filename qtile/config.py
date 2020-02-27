# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import EzKey as Key, Screen, Group, EzDrag as Drag, EzClick as Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

mod = "mod4"

keys = [
    # Layout change
    Key("M-<Tab>", lazy.next_layout()),
    
    ## BSP Layout
    # Change focus
    Key("M-j", lazy.layout.down()),
    Key("M-k", lazy.layout.up()),
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    # Move window
    Key("M-S-j", lazy.layout.shuffle_down()),
    Key("M-S-k", lazy.layout.shuffle_up()),
    Key("M-S-h", lazy.layout.shuffle_left()),
    Key("M-S-l", lazy.layout.shuffle_right()),
    # Move window
    Key("M-A-j", lazy.layout.flip_down()),
    Key("M-A-k", lazy.layout.flip_up()),
    Key("M-A-h", lazy.layout.flip_left()),
    Key("M-A-l", lazy.layout.flip_right()),
    # Resize window
    Key("M-C-j", lazy.layout.grow_down()),
    Key("M-C-k", lazy.layout.grow_up()),
    Key("M-C-h", lazy.layout.grow_left()),
    Key("M-C-l", lazy.layout.grow_right()),
    # Reset
    Key("M-S-n", lazy.layout.normalize()),
    # Toggle split
    Key("M-<space>", lazy.layout.toggle_split()),
    
    # Programs shortcuts
    Key("M-<Return>", lazy.spawn("gnome-terminal")),
    Key("M-r", lazy.spawn("ulauncher")),
    Key("M-e", lazy.spawn("nautilus")),
    Key("M-f", lazy.spawn("firefox")),
    Key("M-S-f", lazy.spawn("firefox --private-window")),

    Key("M-w", lazy.window.kill()),
    Key("M-C-r", lazy.restart()),
    Key("M-C-q", lazy.shutdown()),
    Key("M-S-C-q", lazy.spawn("shutdown 0")),
    Key("M-S-C-l", lazy.spawn("gnome-screensaver-command -l")),

    # GNOME-related shortcuts
    # Key('M-S-C-l', lazy.spawn('gnome-screensaver-command -l')),
    # Key('M-C-q', lazy.spawn('gnome-session-quit --logout --no-prompt')),
    # Key('M-S-C-q', lazy.spawn('gnome-session-quit --power-off')),

    # Volume
    Key("<XF86AudioLowerVolume>", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key("S-<XF86AudioLowerVolume>", lazy.spawn("amixer -c 0 -q set Master 1dB-")),
    Key("<XF86AudioRaiseVolume>", lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key("S-<XF86AudioRaiseVolume>", lazy.spawn("amixer -c 0 -q set Master 1dB+")),
    Key("<XF86AudioMute>", lazy.spawn("amixer -D pulse set Master 1+ toggle")),

    # Brightness
    Key("<XF86MonBrightnessUp>", lazy.spawn("light -A 5")),
    Key("S-<XF86MonBrightnessUp>", lazy.spawn("light -A 1")),
    Key("<XF86MonBrightnessDown>", lazy.spawn("light -U 5")),
    Key("S-<XF86MonBrightnessDown>", lazy.spawn("light -U 1")),
]

groups = [Group(i) for i in "asdyxc"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key(f"M-{i.name}", lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key(f"M-S-{i.name}", lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layout_defaults = dict(
    margin = 5,
    border_width=2,
    border_focus="#FFFFFF",
    )

floating_layout_defaults = layout_defaults.copy()
floating_layout_defaults["border_width"] = 0

layouts = [
    layout.Bsp(name="bsp", **layout_defaults),
    layout.Max(**layout_defaults),

    # layout.Stack(num_stacks=2),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=6,
)
icon_defaults = dict(
    font='feather',
    fontsize = 18,
    padding = 6,
)
battery_widget_defaults = dict(
    format='{char}[{percent:2.0%}]  ',
    low_percentage=0.2,
    update_interval=15,
    show_short_text=False
)
extension_defaults = widget_defaults.copy()

bar_widgets = [
    widget.CurrentLayoutIcon(**widget_defaults),
    widget.GroupBox(**widget_defaults),
    widget.WindowName(**widget_defaults),

    widget.Clock(**widget_defaults, format='%Y-%m-%d %a %H:%M:%S'),
    widget.Spacer(length=128),

    widget.Systray(**widget_defaults, icon_size=24),
    widget.Spacer(length=24),

    widget.TextBox(u'\ue8ef', **icon_defaults),
    widget.Volume(**widget_defaults, device = "sysdefault"), 
    widget.TextBox(u'\ue8cf', **icon_defaults),
    widget.Backlight(**widget_defaults, backlight_name='intel_backlight', format='[{percent:2.0%}]  '),
    widget.TextBox(u'\ue832', **icon_defaults), 
    widget.Battery(**widget_defaults, **battery_widget_defaults, battery=0),
    widget.TextBox(u'\ue832', **icon_defaults),
    widget.Battery(**widget_defaults, **battery_widget_defaults, battery=1),
    widget.CPUGraph(**widget_defaults, margin_x=12),
]

screens = [
    Screen(
        bottom=bar.Bar(
            bar_widgets,
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag("M-1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front()),
    Click("M-S-1", lazy.window.toggle_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(auto_float_typesR=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **floating_layout_defaults)

auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Wallpaper
import subprocess
from libqtile import hook

wallpaper_path = "/home/pierre/Pictures/Wallpapers/glitch.png"
subprocess.call(["feh", "--bg-fill", wallpaper_path]) 

@hook.subscribe.startup_once
def autostart():
    subprocess.call(["/home/pierre/.config/qtile/autostart.sh"])


# Gnome integration
import os

@hook.subscribe.startup
def dbus_register():
    id = os.environ.get("DESKTOP_AUTOSTART_ID")
    if not id:
        return
    subprocess.Popen(['dbus-send',
                      '--session',
                      '--print-reply',
                      '--dest=org.gnome.SessionManager',
                      '/org/gnome/SessionManager',
                      'org.gnome.SessionManager.RegisterClient',
                      'string:qtile',
                      'string:' + id])
