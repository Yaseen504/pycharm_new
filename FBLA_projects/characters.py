from class_avatar import Avatar
from class_character import Character

from dictionaries import (
    create_powers_dict,
    create_shop_items_dict,
    create_items_undiscovered_dict,
)


def create_player():
    return Avatar(
        Character(
            name="Jerry",
            damage=15,
            money_value=0,
            bars_num=100,
            max_bars_num=150,
            max_inventory_space=25,
            shop_items_dict=create_shop_items_dict(),
            powers_dict=create_powers_dict(),
            items_undiscovered_dict=create_items_undiscovered_dict(),
        )
    )


def create_enemy():
    return Avatar(
        Character(
            name="Mortimer",
            damage=20,
            money_value=0,
            bars_num=100,
            max_bars_num=150,
            max_inventory_space=0,
            shop_items_dict=create_shop_items_dict(),
            powers_dict=create_powers_dict(),
            items_undiscovered_dict=create_items_undiscovered_dict(),
        )
    )


# Character Initialization
def initialize_characters():

    player = create_player()
    mortimer = create_enemy()

    # Powers are weapons characters use to attack
    player.character.battle.grant_powers("fist")
    mortimer.character.battle.grant_powers("venom", "sting")

    return player, mortimer
