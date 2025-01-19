# Initialization Functions
def create_powers_dict():
    return {
        "hydra sword": {
            "damage": 50,
            "type": "melee",
            "information": "a ... sword",
            "rarity": "rare",
        },
        "heavenly staff": {
            "damage": 75,
            "type": "ranged",
            "information": "a powerful staff",
            "rarity": "epic",
        },
        "forest vines": {
            "damage": 60,
            "type": "melee",
            "information": "deadly vines that pack a punch",
            "rarity": "epic",
        },
        "ferocious scythe": {
            "damage": 100,
            "type": "melee",
            "information": "a ... briliant blade",
            "rarity": "mythical",
        },
        "iron gauntlets": {
            "damage": 85,
            "type": "melee",
            "information": "turns your fists into weapons",
            "rarity": "epic",
        },
        "fist": {
            "damage": 20,
            "type": "melee",
            "information": "your hands",
            "rarity": "common",
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
    """Some items will have damage properties that can used with the
        throw choice in battles."""

    return {
        "Apple": {"heal": 50, "quantity": 50},
        "Bread": {"heal": 10, "quantity": 2},
        "Health Potion": {"heal": 50, "quantity": 5},
        "Mana Potion": {"heal": 50, "quantity": 3},
        "Elixir": {"heal": 70, "quantity": 20},
        "Cooked Fish": {"heal": 10, "quantity": 20},
        "Divine Bread": {"heal": 100, "quantity": 20},
        "Scarlet Dragonfruit": {"heal": 90, "quantity": 20},

        "Elixir": {
            "heal": 80,
            "quantity": 10,
            "info": "A delicious and sharp bottle.",
            "damage": 40
        },
        "Cooked Fish": {
            "heal": 20,
            "quantity": 2,
            "info": "Burnt fish that may or may not taste good.",
            "damage": 10
        }
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
            "rarity": "Common",
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
            "rarity": "Epic",
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