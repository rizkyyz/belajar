import os
from pyfiglet import Figlet

def print_cool(text):
# ngepet
    cool_text = Figlet(font="slant")
# terminal windows
    os.system("cls")

    os.system('mode con: cols=75 lines=30')
    return str(cool_text.renderText(text))

if__name__ == "__main__":
  print(print_cool("python_geniud"))
