# Initialization Functions
def create_powers_dict():
    return {
        "hydra sword": {
            "damage": 300,
            "type": "melee",
            "information": "a ... sword",
            "rarity": "Very rare",
        },
        "bow": {
            "damage": 15,
            "type": "ranged",
            "information": "a ... bow",
            "rarity": "not rare",
        },
        "dagger": {
            "damage": 12,
            "type": "melee",
            "information": "a ... dagger",
            "rarity": "rare",
        },
        "stick": {
            "damage": 5,
            "type": "melee",
            "information": "a ... stick",
            "rarity": "uncommon",
        },
        "fist": {
            "damage": 15,
            "type": "melee",
            "information": "your hands",
            "rarity": "default",
        },
        "rock": {
            "damage": 20,
            "type": "throwable",
            "information": "a ... rock",
            "rarity": "everywhere",
        },
        "venom": {
            "damage": 20,
            "type": "melee",
            "information": "a ... poisonous bite",
            "rarity": "rare",
        },
        "sting": {
            "damage": 15,
            "type": "melee",
            "information": "a ... harmful sting",
            "rarity": "common",
        },
    }


def create_items_undiscovered_dict():
    return {
        "Apple": {"heal": 50, "quantity": 50},
        "Bread": {"heal": 10, "quantity": 2},
        "Health Potion": {"heal": 50, "quantity": 5},
        "Mana Potion": {"heal": 50, "quantity": 3},
        "Elixir": {"heal": 100, "quantity": 20},
        "Cooked Fish": {"heal": 10, "quantity": 20},
    }


def create_shop_items_dict():
    return {
        "Apple": {
            "heal": 5,
            "quantity": 20,
            "price": 25,
            "info": "A juicy red apple that restores health.",
            "rarity": "Common",
        },
        "Bread": {
            "heal": 90,
            "quantity": 2,
            "price": 100,
            "info": "A loaf of bread to regain energy and stamina.",
            "rarity": "Uncommon",
        },
        "Health Potion": {
            "heal": 50,
            "quantity": 5,
            "price": 300,
            "info": "A potion that restores a significant amount of health.",
            "rarity": "Rare",
        },
        "Elixir": {
            "heal": 100,
            "quantity": 1,
            "price": 1000,
            "info": "A legendary elixir that restores full health and mana.",
            "rarity": "Legendary",
        },
        "Crystal Shard": {
            "heal": 25,
            "quantity": 10,
            "price": 200,
            "info": "A shard of crystal that has minor restorative abilities.",
            "rarity": "Rare",
        },
        "Golden Apple": {
            "heal": 50,
            "quantity": 2,
            "price": 2000,
            "info": "An enchanted apple that bestows immense vitality.",
            "rarity": "Epic",
        },
    }
