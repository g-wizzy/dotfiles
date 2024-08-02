from libqtile.config import Group, Match, EzKey as Key, ScratchPad, DropDown
from libqtile.lazy import lazy

import re

from keys import keys
from layouts import default_layouts, chat_layouts


groups = [
    Group(
        'a',
        matches=[Match(wm_class=re.compile(r"^(firefox)$"))],
        label=u'\uf269',
        layouts=default_layouts
    ),
    Group(
        's',
        matches=[Match(wm_class=re.compile(r"^(vscodium)$"))],
        label=u'\ue5fb',
        layouts=default_layouts
    ),
    Group(
        'd',
        label=u'\uf120',
        layouts=default_layouts
    ),
    Group(
        'y',
        label=u'\uf120',
        layouts=default_layouts
    ),
    Group(
        'x',
        matches=[Match(wm_class=re.compile(r"^(microsoft\ teams\ \-\ preview|prospect\ mail)$"))],
        label=u'\U000f02bb',
        layouts=default_layouts
    ),
    Group(
        'c',
        matches=[Match(wm_class=re.compile(r"^(telegram\-desktop|discord|threema)$"))],
        label=u'\U000f0365',
        layout="columns",
        layouts=chat_layouts
    ),
]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key(f"M-{i.name}", lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key(f"M-S-{i.name}", lazy.window.togroup(i.name, switch_group=True)),
    ])

dropdown_defaults = {
    "x": -0.001,
    "y": 0.65,
    "opacity": 0.9,
    "width": 1.002,
    "on_focus_lost_hide": True,
}

groups.append(
    ScratchPad(
        "scratchpad", [
            DropDown(
                "term", 
                "/usr/bin/kitty",
                **dropdown_defaults
            ),
            DropDown(
                "python", 
                "/usr/bin/kitty python",
                **dropdown_defaults
            ),
            DropDown(
                "update", 
                "/usr/bin/kitty yay -Syu",
                **dropdown_defaults
            ),
        ]
    )
)
