from libqtile.config import Screen
from libqtile import qtile, widget, bar, hook

from color_themes import gruvbox_theme as theme

from itertools import cycle

from pathlib import Path
from os.path import expanduser
from random import choice


# Separator-related functions and variables
class SeparatorWriter:
    def __init__(self, colors: tuple[str, str]):
        self.colors = cycle(colors)
        self.background = next(self.colors)

    def next(self, right_looking: bool = True):
        left_color, right_color = self.background, next(self.colors)
        self.background = right_color

        arrow_char, background, foreground = (
            ("\ue0b4", right_color, left_color)
            if right_looking
            else ("\ue0b6", left_color, right_color)
        )

        return widget.TextBox(
            arrow_char,
            **separator_defaults,
            background=background,
            foreground=foreground,
        )


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
    padding=6,
)

icon_defaults = widget_defaults.copy()
icon_defaults["fontsize"] = 24

group_box_widget_defaults = icon_defaults | dict(
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

main_screen_groupbox = widget.GroupBox(
    visible_groups=["Z"],
    background=separators.background,
    **group_box_widget_defaults,
)


@hook.subscribe.startup
async def _():
    if len(qtile.screens) == 1:
        main_screen_groupbox.visible_groups = ["A", "S", "D", "Y", "X", "C", "Z"]
    else:
        main_screen_groupbox.visible_groups = ["Z"]

    if hasattr(main_screen_groupbox, "bar"):
        main_screen_groupbox.bar.draw()


bar_widgets = [
    widget.Spacer(length=18, background=separators.background),
    main_screen_groupbox,
    separators.next(right_looking=True),
    widget.Spacer(
        # length=16,
        background=separators.background,
    ),
    # widget.WindowName(
    #     **widget_defaults, background=separators.background, format="{name}"
    # ),
    widget.CheckUpdates(
        **icon_defaults,
        background=separators.background,
        display_format="\U000f06c3",
        distro="Arch_checkupdates",
        execute="kitty yay -Syu",
        colour_have_updates=theme.alert1,
    ),
    widget.Spacer(length=16, background=separators.background),
    separators.next(right_looking=False),
    widget.Clock(
        **widget_defaults,
        background=separators.background,
        format="%H:%M:%S %a %d.%m.%Y",
    ),
    separators.next(right_looking=False),
    widget.Systray(
        icon_size=24,
        **widget_defaults,
        background=separators.background,
    ),
    widget.Spacer(
        length=16,
        background=separators.background,
    ),
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
        backlight_name="intel_backlight",
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
    separators.next(right_looking=False),
    widget.CPUGraph(
        **widget_defaults,
        background=separators.background,
        frequency=0.5,
        samples=50,
        border_width=0,
        line_width=0,
        fill_color=theme.highlight3,
        margin_x=12,
    ),
]


def external_screen_widgets(visible_groups: str):
    return [
        widget.Spacer(length=18, background=separators.background),
        widget.GroupBox(
            visible_groups=list(visible_groups),
            background=separators.background,
            **group_box_widget_defaults,
        ),
        separators.next(right_looking=True),
        widget.Spacer(
            length=16,
            background=separators.background,
        ),
        widget.WindowName(
            **widget_defaults, background=separators.background, format="{name}"
        ),
        widget.CheckUpdates(
            **icon_defaults,
            background=separators.background,
            display_format="\U000f06c3",
            distro="Arch_checkupdates",
            execute="kitty yay -Syu",
            colour_have_updates=theme.alert1,
        ),
        widget.Spacer(length=16, background=separators.background),
        separators.next(right_looking=False),
        widget.Clock(
            **widget_defaults,
            background=separators.background,
            format="%H:%M:%S",
        ),
        widget.Spacer(length=18, background=separators.background),
    ]


wallpapers = Path(expanduser("~/wallpapers/"))
wallpaper = choice(list(wallpapers.iterdir()))

screens = [
    Screen(
        top=bar.Bar(
            bar_widgets,
            36,
            margin=12,
        ),
        wallpaper=str(wallpaper.absolute()),
        wallpaper_mode="fill",
    ),
    Screen(
        top=bar.Bar(
            external_screen_widgets("XYC"),
            36,
            margin=12,
        ),
        wallpaper=str(wallpaper.absolute()),
        wallpaper_mode="fill",
    ),
    Screen(
        top=bar.Bar(
            external_screen_widgets("ASD"),
            36,
            margin=12,
        ),
        wallpaper=str(wallpaper.absolute()),
        wallpaper_mode="fill",
    ),
]
