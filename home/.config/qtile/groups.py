from libqtile.config import Group, Match, EzKey as Key, ScratchPad, DropDown
from libqtile.lazy import lazy

import re

from keys import keys
from layouts import default_layouts, chat_layouts

left_screen = 1
right_screen = 2
groups = [
    Group("A", layouts=default_layouts, screen_affinity=left_screen),
    Group("S", layouts=default_layouts, screen_affinity=left_screen),
    Group("D", layouts=default_layouts, screen_affinity=left_screen),
    Group("Y", layouts=default_layouts, screen_affinity=right_screen),
    Group("X", layouts=default_layouts, screen_affinity=right_screen),
    Group("C", layouts=default_layouts, screen_affinity=right_screen),
    Group("Z", layouts=default_layouts, screen_affinity=0)
]


def go_to_screen(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in "ASD":
            qtile.focus_screen(left_screen)
        elif name in "YXC":
            qtile.focus_screen(right_screen)
        else:
            qtile.focus_screen(0)
        qtile.groups_map[name].toscreen()

    return _inner


def go_to_screen_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        qtile.current_window.togroup(name, switch_group=False)
        if name in "ASD":
            qtile.focus_screen(left_screen)
        elif name in "YXC":
            qtile.focus_screen(right_screen)
        else:
            qtile.focus_screen(0)
        qtile.groups_map[name].toscreen()

    return _inner


for i in groups:
    keys.extend(
        [
            Key(f"M-{i.name.lower()}", lazy.function(go_to_screen(i.name))),
            Key(
                f"M-S-{i.name.lower()}",
                lazy.function(go_to_screen_and_move_window(i.name)),
            ),
        ]
    )

dropdown_defaults = {
    "x": -0.001,
    "y": 0.65,
    "opacity": 0.9,
    "width": 1.002,
    "on_focus_lost_hide": True,
}

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown("python", "/usr/bin/kitty python", **dropdown_defaults),
        ],
    )
)
