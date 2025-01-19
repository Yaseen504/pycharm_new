from utilities import (
    clear_terminal, display_text, press_enter_arrow
)
from scene1_events import (
    handle_forest_event, explore_cave, go_swimming,
    handle_battle
)

from class_font import print_fonts

import textwrap

def handle_choices(player):

    """Handles the player's choices in Scene 1."""

    choice_string = """
    While you're outdoors, you want to explore somewhere before you
    return home:

    1 - Explore a cave
    2 - Go out swimming
    stop - Leave story\n"""
    choice_string = textwrap.dedent(choice_string).strip()


    while True:
        clear_terminal()
        print_fonts(
            text=choice_string,  # List the stores text
            font_type="italic",  # Style: "italics"
            color=(255, 255, 255),  # Color: light blue
            delay=0.02,  # 0.02-second delay between characters
        )

        choice = input('Choice: ').strip()
        clear_terminal()

        if choice == "1":
            explore_cave(player)
            return "scene1_choice1"
        elif choice == '2':
            go_swimming(player)
            return "scene1_choice1"
        elif choice.lower() == "stop":
            print("Exiting the story.")
            press_enter_arrow()
            break
        else:
            print("Invalid choice. Try again.")
            press_enter_arrow()