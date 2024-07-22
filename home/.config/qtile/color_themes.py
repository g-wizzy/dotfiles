from collections import namedtuple

ColorTheme = namedtuple(
    'ColorTheme',
    [
        'bg0',
        'bg1',
        'bg2',
        'bg3',
        'bg4',
        'txt0',
        'txt1',
        'txt2',
        'highlight0',
        'highlight1',
        'highlight2',
        'highlight3',
        'alert0',
        'alert1',
        'alert2',
        'alert3',
        'alert4'
    ]
)

nord_theme = ColorTheme(
    bg0='2E3440',
    bg1='3B4252',
    bg2='434C5E',
    bg3='4C566A',
    bg4=None,
    txt0='D8DEE9',
    txt1='E5E9F0',
    txt2='ECEFF4',
    highlight0='8FBCBB',
    highlight1='88C0D0',
    highlight2='81A1C1',
    highlight3='5E81AC',
    alert0='BF616A',
    alert1='D08770',
    alert2='EBCB8B',
    alert3='A3BE8C',
    alert4='B48EAD',
)

gruvbox_theme = ColorTheme(
    bg0='282828',
    bg1='3c3836',
    bg2='504945',
    bg3='665c54',
    bg4='7c6f64',
    txt0='d5c4a1',
    txt1='ebdbb2',
    txt2='fbf1c7',
    highlight0='689d6a',  # aqua
    highlight1='458588',  # blue
    highlight2='d79921',  # yellow
    highlight3='98971a',  # green
    alert0='cc241d', # red
    alert1='b16286', # purple
    alert2='fe8019',  # orange
    alert3='fabd2f',  # yellow
    alert4='d3869b',  # purple
)
