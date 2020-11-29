from collections import namedtuple

ColorTheme = namedtuple(
    'ColorTheme',
    [
        'bg0',
        'bg1',
        'bg2',
        'bg3',
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
    '2E3440',
    '3B4252',
    '434C5E',
    '4C566A',
    'D8DEE9',
    'E5E9F0',
    'ECEFF4',
    '8FBCBB',
    '88C0D0',
    '81A1C1',
    '5E81AC',
    'BF616A',
    'D08770',
    'EBCB8B',
    'A3BE8C',
    'B48EAD',
)