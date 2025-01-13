from utilities import (
    clear_terminal, display_text
)

def game_instructions():
   done = False
   while not done:
        clear_terminal()
        print("\n\n\tInstructions")
        print("_-______________________________-_\n")
        print("This game is an rpg styled text adventure, where you fight, "
              "have an inventory, and purchase items through a shop.\n")
        print("Items can be gathered by exploring the through out the story, "
              "while fights will occur in times of conflict.\n")
        print("Also, everytime an arrow (->) appears in the terminal, that "
              "means you have to click in order to continue the storyline.\n")
        print("If you want to skip the dialogue or expedition at any part of "
              "the story, you may do so by typing in s in the terminal")
        print("Have fun!\n")
        print("Instructions Menu")
        print("X - Exit")
        choice = input("Choice: ").upper()
        if choice == "X":
            print("Exiting Instructions Menu")
            clear_terminal()
            break
        else:
            print("Invalid, try again!")

