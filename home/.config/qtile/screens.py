from libqtile.config import Screen
from libqtile import widget, bar

from color_themes import gruvbox_theme_light as theme

import subprocess
from itertools import cycle

from pathlib import Path
from os.path import expanduser
from random import choice


# Separator-related functions and variables
class SeparatorWriter:
    def __init__(self, colors: tuple[str, str]):
        self._colors = colors
        self.reset()

    def next(self, right_looking: bool = True):
        left_color, right_color = self.background, next(self.colors)
        self.background = right_color

        arrow_char, background, foreground = (
            ("\ue0b4 ", right_color, left_color)
            if right_looking
            else (" \ue0b6", left_color, right_color)
        )

        return widget.TextBox(
            arrow_char,
            **separator_defaults,
            background=background,
            foreground=foreground,
        )

    def reset(self):
        self.colors = cycle(self._colors)
        self.background = next(self.colors)


separators = SeparatorWriter((theme.bg0, theme.bg1))


separator_defaults = dict(
    font="Victor Mono",
    fontsize=36,
    padding=0,
)


widget_defaults = dict(
    font="Victor Mono Semibold",
    foreground=theme.txt0,
    fontsize=18,
    padding=0,
)

icon_defaults = widget_defaults | dict(
    fontsize=24,
    width=30,
    foreground=theme.bg4,
)

group_box_widget_defaults = widget_defaults | dict(
    background=separators.background,
    fontsize=20,
    padding=12,
    margin_x=-4,
    spacing=0,
    center_aligned=True,
    # Text colors
    active=theme.txt0,
    inactive=theme.bg2,
    # Current screen colors
    highlight_method="line",
    highlight_color=theme.bg4,
    this_current_screen_border=theme.alert3,
    this_screen_border=theme.bg3,
    # Urgent colors
    urgent_alert_method="block",
    urgent_border=theme.alert0,
)

battery_text_widget_defaults = dict(
    format="{percent:2.0%}",
    low_percentage=0.2,
    low_foreground=theme.alert0,
    update_interval=5,
    show_short_text=False,
)

# Widget instanciation
separators.next()

updates = widget.CheckUpdates(
    **icon_defaults,
    background=separators.background,
    display_format="\U000f06c3",
    distro="Debian",
    execute="sudo apt upgrade",
    colour_have_updates=theme.alert1
)


def build_widgets(
    group_boxes: list,
    clock_format: str,
    show_systray: bool,
    laptop_info: bool,
    monitor_info: bool
):
    separators.reset()

    widgets = [
        *group_boxes,
        separators.next(right_looking=True),
        widget.WindowName(
            **widget_defaults,
            background=separators.background,
            format="{name}"
        ),
        updates,
        separators.next(right_looking=False),
        widget.TextBox(
            "\uf017",
            **icon_defaults,
            background=separators.background,
        ),
        widget.Clock(
            **widget_defaults,
            background=separators.background,
            format=clock_format,
        ),
    ]

    if show_systray:
        widgets += [
            separators.next(right_looking=False),
            widget.Systray(
                icon_size=24,
                **widget_defaults,
                background=separators.background,
            ),
        ]

    if laptop_info:
        widgets += [
            separators.next(right_looking=False),
            widget.TextBox(
                "\U000f057e",
                **icon_defaults,
                background=separators.background,
            ),
            widget.Volume(
                **widget_defaults,
                background=separators.background,
                card=0,
            ),
            separators.next(right_looking=False),
            widget.TextBox(
                "\U000f00de",
                **icon_defaults,
                background=separators.background,
            ),
            widget.Backlight(
                **widget_defaults,
                background=separators.background,
                backlight_name="nvidia_0",
                format="{percent:2.0%}",
            ),
            separators.next(right_looking=False),
            widget.TextBox(
                "\U000f12a3",
                **icon_defaults,
                background=separators.background,
            ),
            widget.Battery(
                **widget_defaults,
                **battery_text_widget_defaults,
                background=separators.background,
                battery=0,
            ),
        ]

    if monitor_info:
        widgets += [
            separators.next(right_looking=False),
            widget.TextBox(
                "CPU",
                **widget_defaults,
                background=separators.background,
            ),
            widget.CPUGraph(
                **widget_defaults,
                background=separators.background,
                frequency=0.5,
                samples=50,
                border_width=0,
                line_width=0,
                fill_color=theme.highlight3,
            ),
            separators.next(right_looking=False),
            widget.TextBox(
                "RAM",
                **widget_defaults,
                background=separators.background,
            ),
            widget.MemoryGraph(
                **widget_defaults,
                background=separators.background,
                frequency=0.5,
                samples=50,
                border_width=0,
                line_width=0,
                fill_color=theme.highlight2,
            ),
            separators.next(right_looking=False),
            widget.TextBox(
                "SWAP",
                **widget_defaults,
                background=separators.background,
            ),
            widget.SwapGraph(
                **widget_defaults,
                background=separators.background,
                frequency=0.5,
                samples=50,
                border_width=0,
                line_width=0,
                fill_color=theme.alert0,
            ),
            separators.next(right_looking=False),
            widget.TextBox(
                "NET",
                **widget_defaults,
                background=separators.background,
            ),
            widget.NetGraph(
                **widget_defaults,
                background=separators.background,
                frequency=0.5,
                samples=50,
                border_width=0,
                line_width=0,
                fill_color=theme.alert1,
                margin_x=12,
            ),
        ]

    # Add spacers around to make room for the rounded edges
    return [
        widget.Spacer(
            length=16,
            background=separators.background
        ),
        *widgets,
        widget.Spacer(
            length=16,
            background=separators.background
        )
    ]


wallpapers = Path(expanduser("~/wallpapers/"))
wallpaper = choice(list(wallpapers.iterdir()))


def single_screen_setup():
    group_boxes = [
        widget.GroupBox(
            visible_groups="ASD",
            **group_box_widget_defaults
        ),
        widget.GroupBox(
            visible_groups="YXC",
            **group_box_widget_defaults
        ),
    ]

    return [
        build_widgets(
            group_boxes=group_boxes,
            clock_format="%H:%M:%S %a %d.%m.%Y",
            show_systray=True,
            laptop_info=True,
            monitor_info=True,
        ),
        [],
        []
    ]


def triple_screen_setup():
    return [
        # Laptop screen, hidden
        build_widgets(
            group_boxes=[
                widget.GroupBox(
                    visible_groups="Z",
                    **group_box_widget_defaults
                )
            ],
            clock_format="%H:%M",
            show_systray=False,
            laptop_info=True,
            monitor_info=False,
        ),
        # Left screen
        build_widgets(
            group_boxes=[
                widget.GroupBox(
                    visible_groups="ASD",
                    **group_box_widget_defaults
                )
            ],
            clock_format="%H:%M",
            show_systray=True,
            laptop_info=True,
            monitor_info=False,
        ),
        # Right screen
        build_widgets(
            group_boxes=[
                widget.GroupBox(
                    visible_groups="YXC",
                    **group_box_widget_defaults
                )
            ],
            clock_format="%H:%M:%S %a %d.%m.%Y",
            show_systray=False,
            laptop_info=False,
            monitor_info=True,
        ),
    ]


def make_bar(widgets):
    return bar.Bar(widgets, 36, margin=12)


def make_screen(bar):
    return Screen(
        top=bar,
        wallpaper=str(wallpaper.absolute()),
        wallpaper_mode="fill"
    )


def select_screen_setup():
    n_screens = int(
        subprocess.run(
            "xrandr --listmonitors | awk 'NR==1 {print $NF}'",
            shell=True,
            capture_output=True
        ).stdout
    )
    if n_screens == 1:
        return single_screen_setup()
    else:
        return triple_screen_setup()
        subprocess.run("/home/pierre/.screenlayout/A209.sh")


screens = [
    make_screen(make_bar(widgets)) for widgets in select_screen_setup()
]
