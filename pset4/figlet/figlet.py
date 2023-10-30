from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) < 2:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
text = input("Input: ")
print("Output: ", figlet.renderText(text))
