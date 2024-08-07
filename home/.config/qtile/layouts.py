from libqtile import layout
from libqtile.config import Match

from color_themes import gruvbox_theme as theme


layout_defaults = dict(
    margin=12,
    border_width=0,
    border_normal=theme.bg0,
    border_focus=theme.highlight0,
    grow_amount=1,
)

max_layout_defaults = layout_defaults.copy()
max_layout_defaults.update(border_width=0, margin=0)

max = layout.Max(**max_layout_defaults)
bsp = layout.Bsp(name="bsp", **layout_defaults)
col = layout.Columns(**layout_defaults)
# layout.Stack(num_stacks=2)
# layout.Columns()
# layout.Matrix()
# layout.MonadTall()
# layout.MonadWide()
# layout.RatioTile()
# layout.Tile()
# layout.TreeTab()
# layout.Zoomy()

default_layouts = [bsp, max]
chat_layouts = [col, max]

layouts = [bsp, col, max]


floating_layout_defaults = layout_defaults.copy()
# floating_layout_defaults.update(border_width=3)

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(func=lambda c: bool(c.is_transient_for())),
    ],
    **floating_layout_defaults,
)
