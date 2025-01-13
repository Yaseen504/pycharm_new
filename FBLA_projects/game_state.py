from characters import (
    create_player, create_enemy,
    initialize_characters
)
from scene1_events import (
    handle_forest_event, explore_cave, go_swimming,
    handle_battle, post_battle_dialogue
)
from utilities import (
    clear_terminal, display_text
)
from scene1_choices import handle_choices

def game_state():

    clear_terminal()
    player, mortimer = initialize_characters()
    choice_state = "scene1_choice0"

    if choice_state == "scene1_choice0":
        handle_forest_event(player)
        choice_state = handle_choices(player)

    if choice_state == "scene1_choice1":
        handle_battle(player, mortimer)
