import time
import textwrap

"""Prints high-quality based fonts"""


def print_fonts(text: str, font_type: str = "default",
               color: tuple = (255, 255, 255), delay: float = 0.0):
   """
       text -> (str):
           The text to print.
       font_type -> (str):
           The font type ("bold", "italic" ... "default").
       color -> (tuple):
           RGB values for coloring the text (e.g., (255, 0, 0) for red).
       delay -> (float):
           Time delay (in seconds) between printing each character.
   """


   # ANSI escape codes for font styles
   styles = {
       "default": "0",
       "bold": "1",
       "italic": "3",
       "underline": "4",
   }

   # Get the style code
   style_code = styles.get(font_type.lower(), "0")


   # Convert RGB color to ANSI escape sequence
   red, green, blue = color
   color_code = f"\033[38;2;{red};{green};{blue}m"


   # Combine style and color codes
   start_code = f"\033[{style_code};{color_code[2:]}"
   reset_code = "\033[0m"

   text = textwrap.dedent(text).strip()

   # Print the text with delay
   for char in text:
       print(f"{start_code}{char}{reset_code}", end="", flush=True)
       time.sleep(delay)
   print()  # Line break after finishing text