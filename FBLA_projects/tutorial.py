from utilities import (
    clear_terminal, display_unindent, press_enter_arrow,
    tutorial_skip_example)

from class_font import print_fonts

from dictionaries import (create_powers_dict, create_shop_items_dict,
                          create_items_undiscovered_dict)

def tutorial():

    """The tutorial will discuss:

    what indicates that you should press enter

    how to skip scenes

    sample battle fight

    what items do and their purpose

    what fonts indicate

    what money does and its purpose"""

    #TODO YOU'RE ON GIVING AN EXAMPLE OF AN ITEM FROM THE CREATE SHOP ITEMS
    # DICT
    # shop_items_dict = create_shop_items_dict()

    done = False
    while not done:
        clear_terminal()
        print("\n\n\tTutorial")
        print("_-______________________________-_\n")

        # arrow symbol
        subtitle = "Arrow symbol"
        print_fonts(subtitle,
                    "underline",
                    (255, 255, 255),
                    0.0)

        arrow_string = """
        To begin, when an arrow (->) appears on the screen,
        that indicates that you must press enter to progress onto the 
        story. This will be used for the rest of this tutorial as 
        well as the game!
        """

        display_unindent(arrow_string)
        press_enter_arrow()


        # skip symbol
        subtitle = "Skip symbol"
        print_fonts(subtitle,
                    "underline",
                    (255, 255, 255),
                    0.0)

        skip_string = """
        Next is the <s?> symbol. This symbol
        indicates that you're allowed to skip text by pressing s.
        If you do anything but press s, the story will continue normally
        
        Lets show you some examples!
        Trying skipping on the first and not skipping on the second
        """
        display_unindent(skip_string)
        press_enter_arrow()

        example = "Example 1"
        print_fonts(example,
                    "bold",
                    (255, 255, 255),
                    0.0)


        skip_example_string = """
        This is the text that comes in line 1
        This is the text that comes in line 2
        This is the text that comes in line 3
        """
        tutorial_skip_example(skip_example_string, 1)

        example = "Example 1"
        print_fonts(example,
                    "bold",
                    (255, 255, 255),
                    0.0)

        skip_example_string2 = """
        This is the text that comes in line 1
        This is the text that comes in line 2
        This is the text that comes in line 3
        """
        tutorial_skip_example(skip_example_string2, 1)
        clear_terminal()

        subtitle = "Items"
        print_fonts(subtitle,
                    "underline",
                    (255, 255, 255),
                    0.0)


        item_string = """
        Items in this game serve the purpose of healing you during battles and
        even some of them may even have offensive capabilities.

        You gather items by progressing throughout the story and through
        purchases using money.

        Items come in 4 rarities:
        """
        display_unindent(item_string)

        rarities = """
        Common
        Rare
        Mythic
        Epic
        """
        print_fonts(rarities,
                    "bold",
                    (255, 255, 255),
                    0.0)

        press_enter_arrow()
        print("This is a work in progress")
        # print(items_undiscovered_dict[])




        # after this gives examples

        # # items
        # print("""

        """)
        #
        # # powers
        # print("""
        # Powers will be used
        # """)
        #
        # # battle choices
        # print(
        #     """
        #     In battles, you can use your powers and item to show who's boss!
        #
        #     In battles, you alternate in turns between the player and the enemy being able to attack
        #
        #     As soon as either the player or the enemy reaches zero health. The Battle ends.
        #     If you player's health reaches to zero, you will lose the game and be prompted back to menu screen.
        #
        #     In battles you can attack, throw, flee, skip, or heal.
        #
        #     attack - choose one of your weapons to attack with.
        #
        #     flee - Exits the battle without you killing the enemy or dying.
        #
        #     skip - Allows you to skip a turn
        #
        #     heal - You can use an item to heal yourself. Every time you use an item it removes it from your item inventory.
        #     You can't heal if you run out of items.
        #
        #     Throw - some items come with damage properties. If they do, you can throw the items to damage the opponent.
        #     """)
        #
        # # critical hits
        # print("""
        #       In battles, there's a chance of you landing a critical hit that will give you a damage multiplier for the weapon you used for that turn.
        #       """)
        #
        # print("""
        #     Note that some battles may not have the option for you to flee but all battles will have all the other options.
        #
        # """)
        #
        # # money system
        # print("""
        #     In this game, there's a money system that allows you to purchase items. You gain money by traversing through the story
        #     By going to shops, you can purchase items and powers are varying rarities.
        #       """)
        #
        #
        #
        #


        print("\nX - Exit")
        choice = input("Choice: ").upper()
        if choice == "X":
            print("Exiting Instructions Menu")
            clear_terminal()
            break
        else:
            print("Invalid, try again!")






