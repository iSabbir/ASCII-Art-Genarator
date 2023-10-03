import pyfiglet

word = input("Enter a word: ")

font_styles = [
    "banner",
    "big",
    "block",
    "bubble",
    "digital",
    "ivrit",
    "mini",
    "script",
    "shadow",
    "slant",
    "small",
    "smscript",
    "smshadow",
    "smslant",
    "standard"
]

for font_style in font_styles:
    ascii_art = pyfiglet.figlet_format(word, font=font_style)
    print(f"\nFont style: {font_style}")
    print(ascii_art)
