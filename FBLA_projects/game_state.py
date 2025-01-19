from characters import create_player, create_enemy, initialize_characters
from utilities import clear_terminal, display_text, press_enter_arrow
from scene1_choices import handle_choices
from scene1_events import handle_forest_event, explore_cave, go_swimming, handle_battle
from scene2_events import handle_scene2
from scene3_events import handle_scene3, handle_choices3


def game_state():

    clear_terminal()
    player, mortimer = initialize_characters()
    choice_state = "scene1_choice0"

    if choice_state == "scene1_choice0":
        handle_forest_event(player)
        choice_state = handle_choices(player)

    if choice_state == "scene1_choice1":
        choice_state = handle_battle(player, mortimer)

    if choice_state == "scene2":
        handle_scene2(player)
        choice_state = "scene3"

    if choice_state == "scene3":
        handle_scene3(player)
        choice_state = handle_choices3(player)

    if choice_state == "scene4":
        print("""
              This is a work in progress.
              Thank you for playing!
              """)
        press_enter_arrow()