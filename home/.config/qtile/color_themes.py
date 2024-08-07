from typing import NamedTuple


class ColorTheme(NamedTuple):
    bg0: str
    bg1: str
    bg2: str
    bg3: str
    bg4: str
    txt0: str
    txt1: str
    txt2: str
    highlight0: str
    highlight1: str
    highlight2: str
    highlight3: str
    alert0: str
    alert1: str
    alert2: str
    alert3: str
    alert4: str


gruvbox_theme = ColorTheme(
    bg0="282828",
    bg1="3c3836",
    bg2="504945",
    bg3="665c54",
    bg4="7c6f64",
    txt0="d5c4a1",
    txt1="ebdbb2",
    txt2="fbf1c7",
    highlight0="689d6a",  # aqua
    highlight1="458588",  # blue
    highlight2="d79921",  # yellow
    highlight3="98971a",  # green
    alert0="cc241d",  # red
    alert1="b16286",  # purple
    alert2="fe8019",  # orange
    alert3="fabd2f",  # yellow
    alert4="d3869b",  # purple
)
