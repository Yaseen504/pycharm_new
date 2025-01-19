from utilities import clear_terminal, display_text, press_enter_arrow
from class_font import print_fonts
from class_money import Money
import textwrap


def handle_choices3(player):
    """Handles the player's choices in Scene 3."""

    choice_string = """
    1 - Light Bringer
    2 - Ultimate Wrath
    stop - Leave story\n"""

    choice_string = textwrap.dedent(choice_string).strip()

    while True:
        clear_terminal()
        print_fonts(
            text=choice_string,  # List the stores text
            font_type="italic",  # Style: "italics"
            color=(255, 255, 255),  # Color: light blue
            delay=0.0,  # 0.05-second delay between characters
        )
        choice = input('Choice: ').strip()
        clear_terminal()

        if choice == "1":
            scene3_light_bringer(player)
            return "scene4"
        elif choice == "2":
            scene3_ultimate_wrath(player)
            return "scene4"
        elif choice.lower() == "stop":
            print("Exiting the story.")
            press_enter_arrow()
            break
        else:
            print("Invalid choice. Try again.")
            press_enter_arrow()


def handle_scene3(player):
    """Handles the dialogue present in Scene 3."""

    clear_terminal()
    print("|Scene 3: Jerry meets Gregory!|")
    print("-------------------------------")

    dialogue = """
    After the salty outcry you have, you decide to go once again to that same
    forest you went to the other day.
    But something strange happens.
    You see glowing comets and a blue orb in the vast sky.
    A magical pegasus with purple and cyan skin approaches you.
    Gregory: greetings, traveler.
    I’ve noticed you haven’t been the happiest in your life.
    Jerry: Yep, you couldn’t be any more right.
    Gregory: Would you like to sign a contract to gain to supernatural powers?
    Jerry: “Um… yes,” you said with a hint of hesitation.
    You sign the contract.
    Gregory: There are two abilities you can choose to have, Mr. Jerry.
    Ultimate wrath, which harvests anger for immense power, or
    LightBringer, which grants you powers of bringing peace.
    """

    display_text(
        text=dialogue,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="default",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )


def scene3_light_bringer(player):
    dialogue = """
    Good choice, if you think the hydra sword you have is strong, you
    won’t believe the power this will give you!
    Gregory: As a thanks to signing this contract, I will reward you 
    with 2 powers and an item you get 3 of.
    You shall also be rewarded with an abundance of money, so do with that 
    as you will.
    Jerry: Wow, being rich sounds so cool!
    Gregory: But be aware mortal, there is no going back from signing this contract.
    You might unexpected things happen to do depending on the path you chose!
    """

    display_text(
        text=dialogue,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="default",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    player.character.battle.grant_powers("heavenly staff", "forest vines")
    player.character.inventory.add_items("Divine Bread", 3)

    player.character.money.become_middle_class()
    player.character.money.money_multiply()

    player.character.character_stats()


def scene3_ultimate_wrath(player):
    dialogue = """
    Gregory: Fair enough, after all ultimate wrath does sound scary so I can’t
    blame you.
    As a thanks to signing this contract, I will reward you with 2 powers and 
    an 3 of the same item.
    You shall also be rewarded with an abundance of money, so do with that 
    as you
    will.
    Jerry: Wow, being rich sounds so cool!
    Gregory: But we aware mortal, there is no going back from signing this
    contract.
    You might unexpected things happen to do depending on the path you chose!
    """

    display_text(
        text=dialogue,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="default",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    player.character.battle.grant_powers("ferocious scythe", "iron gauntlets")
    player.character.inventory.add_items("Scarlet Dragonfruit", 3)

    player.character.money.become_rich()
    player.character.money.money_multiply()
    player.character.character_stats()