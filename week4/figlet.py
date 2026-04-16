import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

args = sys.argv[1:]

if len(args) == 0:
    figlet.setFont(font=random.choice(fonts))
elif len(args) == 2:
    if args[0] not in ("-f", "--font"):
        sys.exit("Invalid usage")
    if args[1] not in fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font=args[1])
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
