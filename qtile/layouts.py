from libqtile import layout

from color_themes import nord_theme as theme

layout_defaults = dict(
    margin = 0,
    border_width = 3,
    border_normal=theme.bg0,
    border_focus=theme.highlight0,
    grow_amount = 3,
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

floating_layout = layout.Floating(auto_float_typesR=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'notify'},
    {'wmclass': 'popup_menu'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitkm
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **floating_layout_defaults)
