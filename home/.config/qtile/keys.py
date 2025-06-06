from libqtile.config import EzKey as Key, EzDrag as Drag, EzClick as Click
from libqtile.lazy import lazy

from datetime import datetime as time
import subprocess, os


# BSP resizing taken from https://github.com/qtile/qtile/issues/1402
def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    resize(qtile, "left")


@lazy.function
def resize_right(qtile):
    resize(qtile, "right")


@lazy.function
def resize_up(qtile):
    resize(qtile, "up")


@lazy.function
def resize_down(qtile):
    resize(qtile, "down")


@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.bring_to_front()


def screenshot(to_clip=False, rect_select=False):
    def f(qtile):
        command = []

        if to_clip:
            # Requires to write one-line script `maim2clip` and have it in $PATH
            command += ["maim2clip"]
        else:
            command += [
                "maim",
                f"{os.path.expanduser('~/Pictures')}/{time.now().isoformat()}.png",
            ]

        if rect_select:
            command += ["-s", "-u"]

        subprocess.run(command)

    return f


keys = [
    # Layout change
    Key("M-<Tab>", lazy.next_layout()),
    ## BSP Layout
    # Change focus
    Key("M-j", lazy.layout.down()),
    Key("M-k", lazy.layout.up()),
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    Key("M-n", lazy.to_screen(1)),
    Key("M-b", lazy.to_screen(2)),
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
    Key("M-C-j", resize_down),
    Key("M-C-k", resize_up),
    Key("M-C-h", resize_left),
    Key("M-C-l", resize_right),
    # Reset
    Key("M-S-n", lazy.layout.normalize()),
    # Toggle split
    Key("M-<space>", lazy.layout.toggle_split()),
    # Programs shortcuts
    Key("M-<Return>", lazy.spawn("kitty")),
    Key(
        "M-e",
        lazy.spawn(
            "kitty --title='ranger' zsh -c 'unset LINES; unset COLUMNS; ranger'"
        ),
    ),
    Key("M-S-e", lazy.spawn("nautilus")),
    Key("M-u", lazy.spawn("kitty zsh -c 'yay -Syu && qtile cmd-obj -o widget checkupdates -f force_update'")),
    Key("M-r", lazy.spawn("rofi -show drun")),
    Key("A-<Tab>", lazy.spawn("rofi -modi windowcd -show windowcd")),
    Key("M-f", lazy.spawn("firefox")),
    Key("M-S-f", lazy.spawn("firefox --private-window")),
    Key("M-v", lazy.spawn("kitty --name=nvim zsh -c nvim")),
    # Screen capture (Shift => selection, Ctrl => to clipboard)
    Key("<F12>", lazy.function(screenshot())),
    Key("C-<F12>", lazy.function(screenshot(to_clip=True))),
    Key("S-<F12>", lazy.function(screenshot(rect_select=True))),
    Key("C-S-<F12>", lazy.function(screenshot(to_clip=True, rect_select=True))),
    Key("M-w", lazy.window.kill()),
    Key("M-C-r", lazy.restart()),
    Key("M-C-q", lazy.shutdown()),
    Key("M-S-C-q", lazy.spawn("shutdown 0")),
    Key("M-S-C-r", lazy.spawn("reboot")),
    Key("M-S-C-l", lazy.spawn("xscreensaver-command -lock")),
    Key("M-t", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key("M-p", lazy.group["scratchpad"].dropdown_toggle("python")),
    Key("M-C-S-p", lazy.spawn("toggle-display")),
    # Volume (hold ctrl for lighter adjustments, shift for large jumps)
    Key("<XF86AudioLowerVolume>", lazy.spawn("amixer -D default -q set Master 5%-")),
    Key("C-<XF86AudioLowerVolume>", lazy.spawn("amixer -D default -q set Master 1%-")),
    Key("S-<XF86AudioLowerVolume>", lazy.spawn("amixer -D default -q set Master 20%-")),
    Key("<XF86AudioRaiseVolume>", lazy.spawn("amixer -D default -q set Master 5%+")),
    Key("C-<XF86AudioRaiseVolume>", lazy.spawn("amixer -D default -q set Master 1%+")),
    Key("S-<XF86AudioRaiseVolume>", lazy.spawn("amixer -D default -q set Master 20%+")),
    Key("<XF86AudioMute>", lazy.spawn("amixer -D default set Master 1+ toggle")),
    # Brightness (hold shift for lighter adjustments)
    Key("<XF86MonBrightnessUp>", lazy.spawn("light -A 5")),
    Key("C-<XF86MonBrightnessUp>", lazy.spawn("light -A 1")),
    Key("S-<XF86MonBrightnessUp>", lazy.spawn("light -A 20")),
    Key("<XF86MonBrightnessDown>", lazy.spawn("light -U 5")),
    Key("C-<XF86MonBrightnessDown>", lazy.spawn("light -U 1")),
    Key("S-<XF86MonBrightnessDown>", lazy.spawn("light -U 20")),
]

mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front()),
    Click("M-S-1", lazy.window.toggle_floating()),
    Click("9", lazy.layout.shuffle_left()),
]
