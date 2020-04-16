from libqtile.config import Screen
from libqtile import widget, bar

from Xlib import display as xdisplay

widget_defaults = dict(
    font='Victor Mono', #old = 'sans'
    fontsize=12,
    padding=6,
)
extension_defaults = widget_defaults.copy()

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

bar_widgets = [
    widget.CurrentLayoutIcon(**widget_defaults),
    widget.GroupBox(**widget_defaults),
    widget.WindowName(**widget_defaults),

    widget.Clock(**widget_defaults, format='%H:%M:%S %a %d.%m.%Y'),
    widget.Spacer(length=128),

    widget.Systray(**widget_defaults, icon_size=24),
    widget.Spacer(length=24),

    widget.TextBox(u'\ue8ef', **icon_defaults),
    widget.Volume(**widget_defaults, device = "sysdefault", format='[{percent:2.0%}]  '), 
    
    widget.TextBox(u'\ue8cf', **icon_defaults),
    widget.Backlight(**widget_defaults, backlight_name='intel_backlight', format='[{percent:2.0%}]  '),
    
    widget.TextBox(u'\ue832', **icon_defaults), 
    widget.Battery(**widget_defaults, **battery_widget_defaults, battery=0),
    
    widget.TextBox(u'\ue832', **icon_defaults),
    widget.Battery(**widget_defaults, **battery_widget_defaults, battery=1),
    
    widget.CPUGraph(**widget_defaults, margin_x=12),
]

second_bar_widgets = [
    widget.CurrentLayoutIcon(**widget_defaults),
    widget.GroupBox(**widget_defaults),
    widget.WindowName(**widget_defaults),
    widget.CurrentScreen(**widget_defaults, active_text = "active", inactive_text = "inactive"),
]

screens = [
    Screen(
        bottom=bar.Bar(
            bar_widgets,
            24,
            opacity=0.8,
        ),
    ),
]

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

if get_num_monitors() > 1:
    screens.append(
            Screen(
                 top=bar.Bar(
                 second_bar_widgets,
                 24,
                 opacity=0.8,
            ),
        )
    )