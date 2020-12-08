from libqtile.config import Screen
from libqtile import widget, bar

from custom_battery_widget import CustomBattery
from color_themes import nord_theme as theme

from Xlib import display as xdisplay



color_schemes = [
    dict(
        background = theme.bg0,
        arrow_color = theme.bg1,
        foreground = theme.txt2
    ),
    dict(
        background = theme.bg1,
        arrow_color = theme.bg0,
        foreground = theme.txt2
    )
]

# Separator-related functions and variables

def separator(right_looking = True):
    global color_scheme
    if right_looking:
        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return widget.TextBox(
            u'\ue0b0', 
            **separator_defaults,
            background = color_scheme["background"],
            foreground = color_scheme["arrow_color"]
        )
    else:
        ret = widget.TextBox(
            u'\ue0b2', 
            **separator_defaults,
            background = color_scheme["background"],
            foreground = color_scheme["arrow_color"]
        )

        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return ret

# Determines the color scheme on the leftmost widget
color_scheme = color_schemes[0]
separator.current_scheme = 0

separator_defaults = dict(
    font='Victor Mono',
    fontsize=24,
    padding=0,
)


widget_defaults = dict(
    font='Victor Mono Semibold',
    fontsize=12,
    padding=6,
)
extension_defaults = widget_defaults.copy()

icon_defaults = widget_defaults.copy()
icon_defaults["fontsize"] = 32

group_box_widget_defaults = dict(
    # Text colors
    active=theme.txt0,
    inactive=theme.bg2,
    # Current screen colors
    highlight_method='line',
    highlight_color=theme.highlight3,
    this_current_screen_border=theme.alert3,
    # Urgent colors
    urgent_alert_method="block",
    urgent_border=theme.alert2
)

battery_text_widget_defaults = dict(
    format='{percent:2.0%}',
    low_percentage=0.2,
    update_interval=5,
    show_short_text=False
)

bar_widgets = [

    widget.CurrentLayoutIcon(
        **widget_defaults,
        **color_scheme,
        scale=0.8,
    ),

    separator(),

    widget.GroupBox(
        **widget_defaults,
        **color_scheme,
        **group_box_widget_defaults
    ),

    separator(),

    widget.Spacer(
        length = 16,
        **color_scheme,
    ),

    widget.WindowName(
        **widget_defaults,
        **color_scheme,
        show_state=False
    ),

    # Note: requires to change the default Ubuntu command in libqtile.widget.CheckUpdates
    # from `aptitude search ~U`
    # into `apt list --upgradable`
    # and change the number of lines to substract from 0 to 1
    widget.CheckUpdates(
        **widget_defaults,
        **color_scheme,
        distro="Arch",
        colour_no_updates=color_scheme["foreground"],
        colour_have_updates=theme.alert1,
    ),

    separator(right_looking = False),

    widget.Clock(
        **widget_defaults,
        **color_scheme,
        format='%H:%M:%S %a %d.%m.%Y',
    ),

    separator(right_looking = False),

    widget.Systray(
        icon_size=24,
        **widget_defaults,
        **color_scheme,
    ),

    widget.Spacer(
        length = 16,
        **color_scheme,
    ),

    separator(right_looking = False),

    # Volume icon and widget
    widget.TextBox(
        u'\ufa7d',
        **icon_defaults,
        **color_scheme,
    ),
    widget.Volume(
        **widget_defaults,
        **color_scheme,
        device = "default",
    ),

    separator(right_looking = False),
    
    # Brightness icon and widget
    # widget.TextBox(
    #     u'\uf5dd',
    #     **icon_defaults,
    #     **color_scheme,
    # ),
    # widget.Backlight(
    #     **widget_defaults,
    #     **color_scheme,
    #     backlight_name='intel_backlight',
    #     format='{percent:2.0%}'
    # ),

    # separator(right_looking = False),
    
    # CustomBattery(
    #     **icon_defaults,
    #     **battery_text_widget_defaults,
    #     **color_scheme,
    #     battery=0
    # ),
    # widget.Battery(
    #     **widget_defaults,
    #     **battery_text_widget_defaults,
    #     **color_scheme,
    #     battery=0
    # ),

    # separator(right_looking = False),

    # CustomBattery(
    #     **icon_defaults,
    #     **battery_text_widget_defaults,
    #     **color_scheme,
    #     battery=1
    # ),
    # widget.Battery(
    #     **widget_defaults,
    #     **battery_text_widget_defaults,
    #     **color_scheme,
    #     battery=1
    # ),

    # separator(right_looking = False),
    
    widget.CPUGraph(
        **widget_defaults,
        **color_scheme,
        frequency=0.33,
        samples=300,
        border_width=0,
        line_width=0,
        fill_color=theme.highlight1,
        margin_x=12
    ),
]

# reset colors
separator()

# Second screen bar
second_bar_widgets = [
    widget.GroupBox(
        **widget_defaults,
        **color_scheme,
        **group_box_widget_defaults
    ),

    separator(),

    widget.Spacer(
        length = 16,
        **color_scheme,
    ),

    widget.WindowName(
        **widget_defaults,
        **color_scheme,
    ),
]

screens = [
    Screen(
        top=bar.Bar(
            bar_widgets,
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            second_bar_widgets,
            24,
        ),
    ),
]
