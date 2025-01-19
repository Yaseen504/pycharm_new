# scene2_events.py

from utilities import clear_terminal, display_text, press_enter_arrow
from class_font import print_fonts
import textwrap


def handle_choices2(player):
    """Handles the player's choices in Scene 2."""

    choice_string = """
    1 - Apologize to them
    2 - Complain about their rudeness
    stop - Leave story\n"""

    choice_string = textwrap.dedent(choice_string).strip()

    while True:
        clear_terminal()
        print_fonts(
            text=choice_string,  # List the stores text
            font_type="italic",  # Style: "italics"
            color=(255, 255, 255),  # Color: light blue
            delay=0.02,  # 0.05-second delay between characters
        )
        choice = input('Choice: ').strip()
        clear_terminal()

        if choice == "1":
            scene2_apologize(player)
            return scene2_apologize_nested(player)
        elif choice == "2":
            scene2_complain(player)
            return "scene3"
        elif choice.lower() == "stop":
            print("Exiting the story.")
            press_enter_arrow()
            break
        else:
            print("Invalid choice. Try again.")
            press_enter_arrow()


def handle_scene2(player):
    """Handles the dialogue present in Scene 2."""

    clear_terminal()
    print("|Scene 2: Jerry goes to school|")
    print("-------------------------------")

    dialogue = """
    Jerry: Oh here it goes again, another day.
    During lunch time you see a group of students chattering and you decide
    to approach them.
    Jerry: Hello guys, how are your days going?
    Group: I wouldn’t want to talk to you, after all, you are known as the
    weird kid who sits alone all the time.
    You feel yourself sinking even deeper into this world, into this inescapable
    sea of suffering. The saddest part is your starting to contemplate whether
    even your family cares about you."""

    display_text(
        text=dialogue,  # List the stores text
        lines_per_chunk=3,  # Display 2 lines at a time
        font_type="default",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    return handle_choices2(player)


def scene2_apologize(player):
    """Handles the dialogue present in Scene 2."""

    dialogue = """
    Jerry: Ok, sorry for bothering, you. I'll leave now.
    """

    display_text(
        text=dialogue,  # List the stores text
        lines_per_chunk=1,  # Display 2 lines at a time
        font_type="default",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )


def scene2_apologize_nested(player):
    """Handles the dialogue present in Scene 2."""

    dialogue = """
    Group: You know what, you may not be that bad, so what do you do at home?'
    1 Watch T.V all day
    2 Hang out with others and play sports
    """

    print_fonts(
        text=dialogue,  # List the stores text
        font_type="italic",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    one = """
    Group: Never mind, you're a loser and hopeless.
    We'd never want to hang out with you
    Jerry: ...
    You run out the cafeteria crying...
    """

    two = """
    Group: What a liar! Hahaha,
    there's no way you'd be capable of having life!
    Jerry: ...
    You run out the cafeteria crying...
    """

    nested_choice = input('Choice: ').strip()
    clear_terminal()
    if nested_choice == "1":
        display_text(
            text=one,  # List the stores text
            lines_per_chunk=2,  # Display 2 lines at a time
            font_type="default",  # Style: "italics"
            color=(255, 255, 255),  # Color: light blue
            delay=0.02,  # 0.05-second delay between characters
        )
    elif nested_choice == "2":
        display_text(
            text=two,  # List the stores text
            lines_per_chunk=2,  # Display 2 lines at a time
            font_type="default",  # Style: "italics"
            color=(255, 255, 255),  # Color: light blue
            delay=0.02,  # 0.05-second delay between characters
        )
    else:
        print("Invalid choice. Try again.")
        press_enter_arrow()


def scene2_complain(player):
    """Handles the dialogue present in Scene 2."""

    dialogue = """
    Jerry: Could you please stop being so mean to me?
    Group: There's a reason why no one wants to talk to you.
    You're just a loathsome brat who's the king of boredom.
    Go back to where you came from.
    Despite you knowing that they barely even know you, the insults still
    inflict an unwavering scar onto you. You storm out the lunch room in fury.
    You go outside, skipping the rest of school to travel to an isolated field
    near school.
    Jerry: Why does this have to happen to me!
    You stupid bullies, what have I even done to you?
    What do you gain from this?
    How could you be happy with making other suffer?
    Why can't it just be over, this awful school.
    Why?
    Why?
    Why?
    Does anybody even care about me?
    My family?, do they care about me?
    I feel horrible, absolutely horrible!
    You pass out on the ground, after being so exhausted from your ranting session.
    """

    display_text(
        text=dialogue,  # List the stores text
        lines_per_chunk=2,  # Display 3 lines at a time
        font_type="default",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )