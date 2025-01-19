# # Initializations
# import copy
# import math
# import os
# import random
# import time
#
# from colorama import Fore, Style, init
#
# init()
#
#
# class Character:  # this is the character class with most of the initialization
#     def __init__(
#         self,
#         name: str,
#         damage: int = None,
#         money_value: float = None,
#         max_inventory_space: int = None,
#         bars_num: int = None,
#         powers: dict = None,
#         items: dict = None,
#         health: str = "",
#         max_bars_num: int = None,
#         original_bars_num: str = None,
#         heal_tag: str = None,
#         quantity_tag: str = None,
#         price_tag: str = None,
#         info_tag: str = None,
#         rarity_tag: str = None,
#         type_tag: str = None,
#         damage_tag: str = None,
#         shop_items_dict: dict = None,
#         powers_dict: dict = None,
#         items_undiscovered_dict: dict = None,
#     ) -> None:
#
#         if True:
#             # BASIC BATTLE INIT
#             self.name = name  # NAME
#             self.damage = damage or 5  # DMG TAKEN
#             self.powers = powers or {}  # WEAPONS/POWERS
#             self.health = health  # FINAL HEALTH
#
#         if True:
#             # just tags based on dictionaries that would be used
#             self.heal_tag = heal_tag or "heal"
#             self.price_tag = price_tag or "price"
#             self.quantity_tag = quantity_tag or "quantity"
#             self.info_tag = info_tag or "info"
#             self.rarity_tag = rarity_tag or "rarity"
#             self.type_tag = type_tag or "type"
#             self.damage_tag = damage_tag or "damage"
#
#         if True:
#             # best to put dictionaries here for most efficiency
#             self.shop_items_dict = shop_items_dict or {
#                 "Apple": {
#                     "heal": 5,
#                     "quantity": 20,
#                     "price": 25,
#                     "info": "A juicy red apple that quenches hunger and restores health.",
#                     "rarity": "Common",
#                 },
#                 "Bread": {
#                     "heal": 90,
#                     "quantity": 2,
#                     "price": 100,
#                     "info": "A loaf of bread to regain energy and stamina.",
#                     "rarity": "Uncommon",
#                 },
#                 "Health Potion": {
#                     "heal": 50,
#                     "quantity": 5,
#                     "price": 300,
#                     "info": "A potion that restores a significant amount of health.",
#                     "rarity": "Rare",
#                 },
#                 "Elixir": {
#                     "heal": 100,
#                     "quantity": 1,
#                     "price": 1000,
#                     "info": "A legendary elixir that restores full health and mana.",
#                     "rarity": "Legendary",
#                 },
#                 "Crystal Shard": {
#                     "heal": 25,
#                     "quantity": 10,
#                     "price": 200,
#                     "info": "A rare shard of crystal that has minor restorative abilities.",
#                     "rarity": "Rare",
#                 },
#                 "Golden Apple": {
#                     "heal": 50,
#                     "quantity": 2,
#                     "price": 2000,
#                     "info": "An enchanted apple that bestows immense vitality.",
#                     "rarity": "Epic",
#                 },
#             }
#             self.powers_dict = powers_dict or {
#                 "sword": {
#                     "damage": 20,  # Removed unnecessary round()
#                     "type": "melee",
#                     "information": "a sharp, versatile weapon",
#                     "rarity": "Rare",
#                 },
#                 "bow": {
#                     "damage": 15,
#                     "type": "ranged",
#                     "information": "a weapon for long-distance combat",
#                     "rarity": "Common",
#                 },
#                 "dagger": {
#                     "damage": 12,
#                     "type": "melee",
#                     "info": "a small, agile weapon for close-quarters combat",
#                     "rarity": "Uncommon",
#                 },
#                 "stick": {
#                     "damage": 10,
#                     "type": "melee",
#                     "info": "a simple, improvised weapon",
#                     "rarity": "Common",
#                 },
#                 "rock": {
#                     "damage": 5,
#                     "type": "throwable",
#                     "info": "a basic projectile",
#                     "rarity": "Very Common",
#                 },
#                 "sling": {
#                     "damage": 10,
#                     "type": "ranged",
#                     "information": "a weapon for hurling projectiles with greater force",
#                     "rarity": "Uncommon",
#                 },
#             }
#             self.items_undiscovered_dict = items_undiscovered_dict or {
#                 "Apple": {"heal": 10, "quantity": 50},
#                 "Bread": {"heal": 15, "quantity": 3},
#                 # Increased heal and quantity
#                 "Health Potion": {"heal": 50, "quantity": 5},
#                 "Mana Potion": {"heal": 50, "quantity": 3},
#                 "Elixir": {"heal": 100, "quantity": 1},
#                 "Bandage": {
#                     "heal": 20,
#                     "quantity": 10,
#                     "info": "A cloth used to bind wounds.",
#                 },
#                 # Added a new item
#                 "Antivenom": {
#                     "effect": "Cures Poison",
#                     "quantity": 2,
#                     "info": "Neutralizes venomous effects.",
#                 },
#                 # Added a new item
#             }
#
#         if True:
#             self.bars_num = bars_num or 100  # CURRENT HEALTH IN INT (ie 23)
#             self.max_bars_num = max_bars_num or round(
#                 self.bars_num * 1.25
#             )  # MAX HEALTH IN INT (ie 30)
#             if self.bars_num > self.max_bars_num:
#                 self.bars_num = (
#                     self.max_bars_num
#                 )  # limits bar_num to be below max_bars_num
#             self.original_bars_num = original_bars_num  # ORIGINAL BARS
#             self.original_bars_num = self.bars_num
#             self.health = "=" * int(
#                 round(self.bars_num)
#             )  # OVERALL HEALTH as BARS NOTATION
#             # note: bars = num of bars - int - ie 5
#             # note: health = amount of health - string - ie '======'
#
#         if True:
#             # INVENTORY CLASS METHODS
#             # SHOP CLASS METHODS
#             self.items = (
#                 items or {}
#             )  # ITEMS (ie apple, banana, cheeseburger, bicycle)
#
#             total_items = sum(
#                 item[self.quantity_tag] for item in self.items.values()
#             )
#             self.max_inventory_space = max_inventory_space or round(
#                 total_items * 1.25
#             )  # MAX NUM OF ITEMS (Combined Quantities) ALLOWED
#
#             # removal of items if it hits max_inventory_space / deletes oldest items first
#             total_items = sum(
#                 item[self.quantity_tag] for item in self.items.values()
#             )
#             while total_items > self.max_inventory_space:
#                 for item_name in list(self.items.keys()):
#                     if self.items[item_name]["quantity"] > 0:
#                         self.items[item_name]["quantity"] -= 1
#                         if self.items[item_name]["quantity"] == 0:
#                             del self.items[item_name]
#                         break
#                 total_items = sum(
#                     item[self.quantity_tag] for item in self.items.values()
#                 )
#
#         if True:
#             # SHOP CLASS METHODS
#             # MONEY CLASS METHODS
#             self.money_value = money_value or 250  # MONEY
#
#     if True:
#
#         def display_name(self):
#             print(
#                 f"{Fore.GREEN}🌟 Name: {Style.BRIGHT}{self.name}{Style.RESET_ALL}"
#             )
#             return self.name
#
#         def display_damage(self):
#             print(
#                 f"{Fore.RED}⚔️  Damage: {Style.BRIGHT}{self.damage}{Style.RESET_ALL}"
#             )
#             return self.damage
#
#         def display_powers(self):
#             _ = ""
#             if not self.powers:
#                 print(
#                     f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}"
#                 )
#             else:
#                 print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
#                 for power, power_type in self.powers.items():
#                     for attribute, information in power_type.items():
#                         if _ != power:
#                             print(
#                                 f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}"
#                             )
#                         print(
#                             f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
#                         )
#                         _ = power
#             return self.powers
#
#         def display_health(self):
#             print(
#                 f"{Fore.GREEN}❤️  Health: {Style.BRIGHT}{self.health}{Style.RESET_ALL} : {Fore.MAGENTA}{self.bars_num}hp{Style.RESET_ALL}"
#             )
#             return self.health, self.bars_num
#
#         def display_max_health(self):
#             print(
#                 f"{Fore.MAGENTA}💪 Max Health Possible: {Style.BRIGHT}{self.max_bars_num}{Style.RESET_ALL}"
#             )
#             return self.max_bars_num
#
#         def display_items(self):
#             _ = ""
#             if not self.items:
#                 print(
#                     f"{Fore.YELLOW}🎒 Items: {Style.BRIGHT}No Items Available{Style.RESET_ALL}"
#                 )
#             else:
#                 print(f"{Fore.YELLOW}🎒 Items: {Style.RESET_ALL}")
#                 for item, item_type in self.items.items():
#                     for attribute, information in item_type.items():
#                         if _ != item:
#                             print(
#                                 f"\t{Fore.CYAN}• {Style.BRIGHT}{item}{Style.RESET_ALL}"
#                             )
#                         print(
#                             f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
#                         )
#                         _ = item
#
#                 total_items = sum(
#                     item[self.quantity_tag] for item in self.items.values()
#                 )
#                 print(
#                     f"{Fore.CYAN}📦 Total Items: {Style.BRIGHT}{total_items} / {self.max_inventory_space}{Style.RESET_ALL}"
#                 )
#
#             return self.items
#
#         def display_max_inventory_space(self):
#             print(
#                 f"{Fore.MAGENTA}📚 Max Inventory Space: {Style.BRIGHT}{self.max_inventory_space}{Style.RESET_ALL}"
#             )
#             return self.max_inventory_space
#
#         def display_money(self):
#             print(
#                 f"{Fore.YELLOW}💰 Money: {Style.BRIGHT}{self.money_value}{Style.RESET_ALL}"
#             )
#             return self.money_value
#
#         def character_stats(self):  # Shows the overall stats
#             os.system("cls" if os.name == "nt" else "clear")
#             print(
#                 f"\n\t\t{Fore.CYAN}🌟 Stats for {Style.BRIGHT}{self.name}{Style.RESET_ALL}"
#             )
#             print(
#                 f"{Fore.GREEN}~~!﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏!~~{Style.RESET_ALL}"
#             )
#             self.display_name()
#             self.display_damage()
#             self.display_powers()
#             self.display_health()
#             self.display_max_health()
#             self.display_items()
#             self.display_max_inventory_space()
#             self.display_money()
#             print(
#                 f"{Fore.RED}-------------------------------------------------{Style.RESET_ALL}\n"
#             )
#
#         def simple_display_stats(self):
#             print(f"{Fore.GREEN}🌟 Name: {self.name}")
#             print(f"{Fore.RED}❤️ HP: {self.bars_num}")
#             print(f"{Fore.YELLOW}💰 Money: {self.money_value}")
#             print(f"{Fore.BLUE}🎒 Inventory: {self.items}")
#             print(f"{Fore.MAGENTA}🌀 Powers: {self.powers}{Style.RESET_ALL}")
#
#             return (
#                 self.name,
#                 self.bars_num,
#                 self.money_value,
#                 self.items,
#                 self.powers,
#             )
#
#         def update_health_by(self, delta):
#             self.bars_num = min(
#                 max(0, self.bars_num + delta), self.max_bars_num
#             )
#             if self.bars_num >= self.max_bars_num:
#                 self.bars_num = self.max_bars_num
#
#             self.health = "=" * int(
#                 round(self.bars_num)
#             )  # OVERALL HEALTH as BARS NOTATION
#
#             return self.bars_num
#
#         def update_health_to(self, delta):
#             self.bars_num = min(max(0, delta), self.max_bars_num)
#             if self.bars_num >= self.max_bars_num:
#                 self.bars_num = self.max_bars_num
#
#             self.health = "=" * int(
#                 round(self.bars_num)
#             )  # OVERALL HEALTH as BARS NOTATION
#
#             return self.bars_num
#
#
# class Avatar(Character):
#     def __init__(self, character: Character):
#         if True:
#             # DELEGATE RESPONSIBILITIES TO RESPECTIVE CLASSES
#
#             self.character = character
#
#             super().__init__(**vars(self.character))
#
#             self.character = Character(**vars(self.character))
#
#             self.item_utility = ItemUtilityMixin(character=self.character)
#
#             self.character.item_utility = self.item_utility
#
#             self.inventory = Inventory(
#                 character=self.character,
#                 item_utility=self.character.item_utility,
#                 items_undiscovered_dict=self.character.items_undiscovered_dict,
#             )
#
#             self.shop = Shop(
#                 character=self.character,
#                 item_utility=self.character.item_utility,
#                 shop_items_dict=self.character.shop_items_dict,
#             )
#
#             self.money = Money(
#                 character=self.character,
#                 item_utility=self.character.item_utility,
#             )
#
#             self.battle = Battle(
#                 character=self.character,
#                 item_utility=self.character.item_utility,
#                 powers_dict=self.character.powers_dict,
#             )
#
#             self.character.inventory = self.inventory
#             self.character.shop = self.shop
#             self.character.money = self.money
#             self.character.battle = self.battle
#
#
# class ItemUtilityMixin:
#     """Provides utility methods for managing and displaying items."""
#
#     def __init__(self, character: Character):
#         if True:
#             self.character = character
#
#     if True:
#
#         def get_items(self) -> dict:
#             """Returns the current items."""
#             return self.character.items
#
#         def get_item_unique_count(self) -> int:
#             """Returns the total UNIQUE item count."""
#             return len(self.character.items)
#
#         def get_item_full_count(self) -> int:
#             """Returns the total item count."""
#             return sum(
#                 item[self.character.quantity_tag]
#                 for item in self.character.items.values()
#             )
#
#         def display_items(self):
#             _ = ""
#             if not self.character.items:
#                 print(
#                     f"{Fore.YELLOW}🎒 {self.character.name} Items: {Style.BRIGHT}No Items Available{Style.RESET_ALL}"
#                 )
#             else:
#                 print(
#                     f"{Fore.YELLOW}🎒 {self.character.name} Items: {Style.RESET_ALL}"
#                 )
#                 for item, item_type in self.character.items.items():
#                     for attribute, information in item_type.items():
#                         if _ != item:
#                             print(
#                                 f"\t{Fore.CYAN}• {Style.BRIGHT}{item}{Style.RESET_ALL}"
#                             )
#                         print(
#                             f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
#                         )
#                         _ = item
#
#                 total_items = sum(
#                     item["quantity"] for item in self.character.items.values()
#                 )
#                 print(
#                     f"{Fore.CYAN}📦 Total Items: {Style.BRIGHT}{total_items} / {self.character.max_inventory_space}{Style.RESET_ALL}"
#                 )
#
#             return self.character.items
#
#         # some other categories that would potentially be useful in item utility
#         def display_powers(self):
#
#             _ = ""
#             if not self.character.powers:
#                 print(
#                     f"{Fore.YELLOW}🌀 {self.character.name} Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}"
#                 )
#             else:
#                 print(
#                     f"{Fore.YELLOW}🌀 {self.character.name} Powers: {Style.RESET_ALL}"
#                 )
#                 for power, power_type in self.character.powers.items():
#                     for attribute, information in power_type.items():
#                         if _ != power:
#                             print(
#                                 f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}"
#                             )
#                         print(
#                             f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
#                         )
#                         _ = power
#
#             return self.character.powers
#
#         def display_money(self):
#             print(
#                 f"{Fore.YELLOW}💰 {self.character.name} Money: {Style.BRIGHT}{self.character.money_value}{Style.RESET_ALL}"
#             )
#             return self.character.money_value
#
#
# class Battle:
#     def __init__(
#         self, character, item_utility, powers_dict, consequences=None
#     ):
#         self.character = character  # Store character object
#         self.item_utility = item_utility  # Store item utility
#         self.powers_dict = powers_dict  # Store powers dictionary
#         self.consequences = consequences  # Optional
#
#         if consequences is None:
#             self.consequences = [
#                 "fainted",
#                 "died",
#                 "injured",
#                 "lost",
#                 "killed",
#             ]  # specific consequences when battle ends
#
#     def set_health(
#         self, health
#     ):  # sets the health to an integer value in relation to the character
#         self.character.bars_num = health
#         if self.character.bars_num > self.character.max_bars_num:
#             self.character.bars_num = self.character.max_bars_num
#
#         return self.character.bars_num
#
#     # note the * allows the function to take as many positional arguments
#     def grant_powers(
#         self, *chosen_power
#     ):  # grants powers in respective to the character
#         for weapon_name, weapon_info in self.powers_dict.items():
#             if weapon_name in chosen_power:
#                 self.character.powers[weapon_name] = (
#                     weapon_info  # Use self.character
#                 )
#         return self.character.powers
#
#     def delete_powers(self, *chosen_power):
#         for weapon_name in self.powers_dict:
#             if (
#                 weapon_name in chosen_power
#                 and weapon_name in self.character.powers
#             ):  # Use self.character
#                 del self.character.powers[weapon_name]
#         return self.character.powers
#
#     # __ at beginning means name manging, internal use, private members (not recommended to use method outside classes folder)
#     def __is_dead(
#         self, character2, netPlayerHP: int, netOpponentHP: int
#     ):  # use to check if someone is dead (health <= 0)
#         if (self.character.bars_num <= 0) or (
#             character2.character.bars_num <= 0
#         ):  # Use self.character
#             if (self.character.bars_num <= 0) and (
#                 character2.character.bars_num <= 0
#             ):
#                 self.character.bars_num = 1
#                 print(
#                     "You have managed to use every ounce of strength for this final HP"
#                 )  # a bonus advantage for player
#
#             if self.character.bars_num <= 0:  # OPPONENT WINS
#                 self.character.bars_num = 0
#                 self.display_battle_info(
#                     character2, netPlayerHP, netOpponentHP
#                 )
#
#                 print()
#                 print("----DEATH----")
#                 print()
#
#                 print(f"You have {self.consequences[0]}")
#                 print(f"{character2.character.name} has won!")
#             else:  # PLAYER WINS
#                 character2.character.bars_num = 0
#                 self.display_battle_info(
#                     character2, netPlayerHP, netOpponentHP
#                 )
#
#                 print()
#                 print("----DEATH----")
#                 print()
#
#                 print(
#                     f"{character2.character.name} has {self.consequences[0]}"
#                 )
#                 print("You have won!")
#             print()
#             return True  # death has occurred, game stops
#
#         else:
#             return False  # death has NOT occurred; game continues
#
#     def display_powers(self):
#         _ = ""
#         if not self.character.powers:  # Use self.character
#             print(
#                 f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}"
#             )
#         else:
#             print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
#             for (
#                 power,
#                 power_type,
#             ) in self.character.powers.items():  # Use self.character
#                 for attribute, information in power_type.items():
#                     if _ != power:
#                         print(
#                             f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}"
#                         )
#                     print(
#                         f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
#                     )
#                     _ = power
#
#     def health_limit_check(
#         self,
#     ):  # checks the limits of health that can be reached
#         if (
#             self.character.bars_num >= self.character.max_bars_num
#         ):  # Use self.character
#             print("Max Health Reached.")
#         elif self.character.bars_num <= 0:  # Use self.character
#             print("Lowest Health Reached")
#
#     def display_attack_dmg(
#         self,
#     ):  # checks how much initial damage you do (like the bare minimum excluding all other aspects)
#         print(
#             f"Attack Potency: {Fore.GREEN}{round(self.character.damage, 2)}{Fore.RESET}"
#         )  # Use self.character
#
#     def display_health_information(self, netPlayerHP):
#         if netPlayerHP > 0:  # positive net Health = HEAL / GAIN HEALTH
#             print(
#                 f"Health: {Fore.BLUE}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET} | {Fore.GREEN}You Gained: {netPlayerHP}HP{Fore.RESET}"
#             )  # Use self.character
#         elif netPlayerHP < 0:  # negative net Health = LOSE HEALTH
#             print(
#                 f"Health: {Fore.BLUE}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET} | {Fore.RED}You Lost: {netPlayerHP}HP{Fore.RESET}"
#             )  # Use self.character
#         else:
#             print(
#                 f"Health: {Fore.BLUE}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET}"
#             )  # Use self.character
#
#     # __ at beginning means name manging, internal use, private members (not recommended to use method outside classes folder)
#     def __display_power_for_opponent(self, character2):
#         _ = ""
#         if not character2.character.powers:  # Use self.character
#             print(
#                 f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}"
#             )
#         else:
#             print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
#             for (
#                 power,
#                 power_type,
#             ) in character2.character.powers.items():  # Use self.character
#                 for attribute, information in power_type.items():
#                     if _ != power:
#                         print(
#                             f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}"
#                         )
#                     print(
#                         f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
#                     )
#                     _ = power
#
#     def __health_limit_check_for_opponent(self, character2):
#         if (
#             character2.character.bars_num >= character2.character.max_bars_num
#         ):  # Use self.character
#             print("Max Health Reached.")
#         elif character2.character.bars_num <= 0:  # Use self.character
#             print("Lowest Health Reached")
#
#     def __display_attack_dmg_for_opponent(self, character2):
#         print(
#             f"Attack Potency: {Fore.GREEN}{round(character2.character.damage, 2)}{Fore.RESET}"
#         )  # Use self.character
#
#     def __display_health_information_for_opponent(
#         self, character2, netOpponentHP
#     ):
#         if netOpponentHP > 0:  # positive net Health = HEAL / GAIN HEALTH
#             print(
#                 f"Health: {Fore.BLUE}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET} | {Fore.GREEN}{character2.character.name} Gained: {netOpponentHP}HP{Fore.RESET}"
#             )  # Use self.character
#         elif netOpponentHP < 0:  # negative net Health = LOSE HEALTH
#             print(
#                 f"Health: {Fore.BLUE}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET} | {Fore.RED}{character2.character.name} Lost: {netOpponentHP}HP{Fore.RESET}"
#             )  # Use self.character
#         else:
#             print(
#                 f"Health: {Fore.BLUE}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET}"
#             )  # Use self.character
#
#     def display_battle_info(
#         self, character2, netPlayerHP: int, netOpponentHP: int
#     ):  # Information shown through the display battle class for each character
#         print(
#             f"{Style.BRIGHT}{Fore.CYAN}*-*-*-* Battle Stats *-*-*-*{Style.RESET_ALL}"
#         )
#
#         # PLAYER DETAILS
#         print(
#             f"{Fore.MAGENTA}\n{self.character.name} (YOU){Fore.RESET}"
#         )  # Use self.character
#         self.display_powers()
#         self.display_attack_dmg()
#         self.display_health_information(netPlayerHP)
#         self.health_limit_check()
#
#         # OPPONENT DETAILS
#         print(
#             f"{Fore.RED}\n{character2.character.name} (OPPONENT){Fore.RESET}"
#         )  # Use self.character
#         self.__display_power_for_opponent(character2)
#         self.__display_attack_dmg_for_opponent(character2)
#         self.__display_health_information_for_opponent(
#             character2, netOpponentHP
#         )
#         self.__health_limit_check_for_opponent(character2)
#
#     def choose_weapon(self):  # Character chooses a weapon/power/superpower
#
#         while True:
#             print(
#                 "Available powers:", list(self.character.powers.keys())
#             )  # Use self.character
#             player_power_choice = (
#                 input("Choose a weapon (or power) from the list above: ")
#                 .strip()
#                 .lower()
#             )
#
#             if player_power_choice in (
#                 key.strip().lower() for key in self.character.powers.keys()
#             ):  # Use self.character
#                 print("You have chosen:", player_power_choice)
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
#
#         return player_power_choice
#
#     @staticmethod  # very static - no .self - local; not global
#     def determine_critical_chance(
#         chance: float = 0.30, multiplier: float = 1.25
#     ) -> float:  # Character imposes a critical hit dmg when lucky
#
#         base_multiplier = 1.00
#         return multiplier if random.random() <= chance else base_multiplier
#
#     def adjust_health(
#         self, character2, c1: bool = True, c2: bool = True
#     ):  # Adjusts the overall health method for both characters
#         if c1:
#             if (
#                 self.character.bars_num >= self.character.max_bars_num
#             ):  # A defined max health limit for player # Use self.character
#                 self.character.bars_num = (
#                     self.character.max_bars_num
#                 )  # Use self.character
#             self.character.health = "=" * int(
#                 round(self.character.bars_num)
#             )  # Use self.character
#
#         if c2:
#             if (
#                 character2.character.bars_num
#                 >= character2.character.max_bars_num
#             ):  # A defined max health limit for opponent # Use self.character
#                 character2.character.bars_num = (
#                     character2.character.max_bars_num
#                 )  # Use self.character
#             character2.character.health = "=" * int(
#                 round(character2.character.bars_num)
#             )  # Use self.character
#
#     @staticmethod  # static - no. self - local; not global
#     # _ at beginning means internal use only (not recommended to use method outside classes folder)
#     def _initialize_fight():  # initializes the fight scene
#
#         print("Do you want to fight?")  # Want to fight?
#         while True:
#             attack_result = input("Y/N: ").upper().strip()
#             if attack_result == "N" or attack_result == "Y":
#                 break
#         print()
#
#         # convert from t/f (true/false) to y/n (yes/no)
#         if attack_result == "Y":
#             attack_result = True
#         else:
#             attack_result = False
#
#         return attack_result
#
#     def fight(self, character2):
#         if (
#             self.character.powers or character2.character.powers
#         ):  # NEEDS A POWER before fighting # Use self.character
#             netPlayerHP = 0  # local variables to calculate NET HP for opponent *relative to each attack
#             netOpponentHP = 0  # local variables to calculate NET HP for player *relative to each attack
#             self.adjust_health(character2, True, True)
#
#             while True:
#                 self.display_battle_info(
#                     character2, netPlayerHP, netOpponentHP
#                 )
#
#                 netOpponentHP = 0  # reset
#                 netPlayerHP = 0  # reset
#
#                 print()
#                 attack_result = self._initialize_fight()
#                 print("----CHOICE SCENE----")
#                 print()
#
#                 # PLAYER ATTACK!
#                 if attack_result:
#                     player_power_choice = (
#                         self.choose_weapon()
#                     )  # What powers/weapon does the player want to choose?
#                     print()
#                     print("----FIGHTING SCENE----")
#                     print()
#
#                     # OVERALL DAMAGE AFFECT FOR PLAYER
#                     player_critical_dmg = self.determine_critical_chance()
#
#                     player_dmg = round(
#                         self.character.powers[player_power_choice][
#                             self.character.damage_tag
#                         ]
#                         + self.character.damage
#                     )  # Use self.character
#                     overall_player_dmg = round(
#                         player_dmg * player_critical_dmg
#                     )
#
#                     if player_critical_dmg != 1.00:
#                         print("CRITICAL DAMAGE!")
#                         print(
#                             f"({player_dmg}) to ({overall_player_dmg}) by {(player_critical_dmg - 1.00) * 100}%"
#                         )
#
#                     print(
#                         f"You have used '{player_power_choice}' with attack_dmg of {overall_player_dmg}"
#                     )
#                     character2.character.bars_num -= overall_player_dmg
#                     netOpponentHP -= overall_player_dmg
#
#                 else:
#                     # OVERALL HEALTH AFFECT FOR PLAYER
#                     print(
#                         f"You have skipped a turn"
#                     )  # Healing affect takes place for player
#                     try:
#                         health_ratio = (
#                             self.character.bars_num
#                             / character2.character.bars_num
#                         )  # Use self.character
#                     except ZeroDivisionError:
#                         health_ratio = 0
#
#                     damage_impact = (
#                         self.character.damage * 0.5
#                     )  # Use self.character
#                     player_relative_increase = math.ceil(
#                         damage_impact * health_ratio
#                     )
#                     self.character.bars_num += (
#                         player_relative_increase  # Use self.character
#                     )
#                     netPlayerHP += player_relative_increase
#
#                     if player_relative_increase:
#                         print(
#                             f"You have gained {player_relative_increase} health"
#                         )
#
#                 print()
#
#                 # OPPONENT ATTACK!
#                 random_number = random.randint(1, 10)
#                 if random_number < 7:
#                     opponent_power_choice = random.choice(
#                         list(character2.character.powers.keys())
#                     )  # Use self.character
#
#                     # OVERALL DAMAGE AFFECT FOR OPPONENT
#                     opponent_critical_dmg = self.determine_critical_chance()
#                     opponent_dmg = round(
#                         character2.character.powers[opponent_power_choice][
#                             self.character.damage_tag
#                         ]
#                         + character2.character.damage
#                     )  # Use self.character
#                     overall_opponent_dmg = round(
#                         opponent_dmg * opponent_critical_dmg
#                     )
#
#                     if opponent_critical_dmg != 1.00:
#                         print("CRITICAL DAMAGE!")
#                         print(
#                             f"({opponent_dmg}) to ({overall_opponent_dmg}) by {(opponent_critical_dmg - 1.00) * 100}%"
#                         )
#                     print(
#                         f"{character2.character.name} has used '{opponent_power_choice}' with attack_dmg of {overall_opponent_dmg}"
#                     )  # Use self.character
#
#                     self.character.bars_num -= (
#                         overall_opponent_dmg  # Use self.character
#                     )
#                     netPlayerHP -= overall_opponent_dmg
#
#                 else:
#                     # OVERALL HEALTH AFFECT FOR OPPONENT
#                     print(
#                         f"{character2.character.name} has skipped a turn"
#                     )  # Healing affect takes place for enemy # Use self.character
#                     try:
#                         health_ratio = (
#                             character2.character.bars_num
#                             / self.character.bars_num
#                         )  # Use self.character
#                     except ZeroDivisionError:
#                         health_ratio = 0
#
#                     damage_impact = (
#                         self.character.damage * 0.5
#                     )  # Use self.character
#                     opponent_relative_increase = math.ceil(
#                         damage_impact * health_ratio
#                     )
#                     character2.character.bars_num += (
#                         opponent_relative_increase  # Use self.character
#                     )
#                     netOpponentHP += opponent_relative_increase
#
#                     if opponent_relative_increase:
#                         print(
#                             f"{character2.character.name} has gained {opponent_relative_increase} health"
#                         )
#                 # Adjusts new health for both characters
#                 self.adjust_health(character2, True, True)
#
#                 print()
#
#                 # use to check if someone gets defeated
#                 if self.__is_dead(character2, netPlayerHP, netOpponentHP):
#                     break  # breaks loop if someone dies when health <= 0
#
#
# class Tutorial:
#     if True:
#
#         @staticmethod
#         def tutorial():
#             Tutorial = """
#            Welcome to the Tutorial
#            """
#             print(Tutorial)
#
#
# class Shop:
#
#     def __init__(
#         self,
#         character: Character,
#         item_utility: ItemUtilityMixin,
#         shop_items_dict: dict,
#     ):
#         if True:
#             self.character = character
#             self.shop_items_dict = shop_items_dict
#             self.item_utility = item_utility
#
#     if True:
#
#         def has_inventory_space(self, add_quantity: int) -> bool:
#             total_items = sum(
#                 item[self.character.quantity_tag]
#                 for item in self.character.items.values()
#             )
#             return (
#                 total_items + add_quantity
#                 <= self.character.max_inventory_space
#             )
#
#         def buy_item(self, new_items: str, quantity: int):
#             checked = False
#             for item_name, item_data in self.shop_items_dict.items():
#                 if new_items in item_name:
#                     if quantity > 0:
#                         if (
#                             quantity
#                             <= self.shop_items_dict[item_name][
#                                 self.character.quantity_tag
#                             ]
#                         ):
#                             total_price = (
#                                 self.shop_items_dict[item_name][
#                                     self.character.price_tag
#                                 ]
#                                 * quantity
#                             )
#                             if self.character.money_value >= total_price:
#                                 if self.has_inventory_space(quantity):
#
#                                     self.character.money_value -= total_price
#
#                                     if item_name in self.character.items:
#                                         self.character.items[item_name][
#                                             self.character.quantity_tag
#                                         ] += quantity
#
#                                     else:
#                                         self.character.items[item_name] = (
#                                             copy.deepcopy(item_data)
#                                         )
#                                         self.character.items[item_name][
#                                             self.character.quantity_tag
#                                         ] = quantity
#
#                                     self.shop_items_dict[item_name][
#                                         self.character.quantity_tag
#                                     ] -= quantity
#
#                                     checked = True
#                                     if (
#                                         self.shop_items_dict[item_name][
#                                             self.character.quantity_tag
#                                         ]
#                                         == 0
#                                     ):
#                                         del self.shop_items_dict[item_name]
#
#                                     return self.character.items
#
#                                 else:
#                                     return (
#                                         "You need more room in your inventory."
#                                     )
#                             else:
#                                 return "You do not have enough money."
#                         else:
#                             return (
#                                 "Enter a quantity that is readily available."
#                             )
#                     else:
#                         return "Enter a positive quantity. Item quantity cannot be negative."
#
#             if not checked:
#                 return "Enter a valid item."
#
#         def currently_buying_items(self):
#             self.character.character_stats()
#
#             # Loop to allow the user to continue buying items until they choose to stop
#             continue_shopping = True
#             while continue_shopping:
#                 print("Items available in the shop:")
#                 self.show_items_for_sale()  # Assuming there’s a method to display available shop items
#
#                 # Prompt the user to enter the item they want to buy
#                 item_name = input(
#                     "Enter the name of the item you want to buy (or type 'exit' to stop): "
#                 ).strip()
#
#                 if item_name.lower() == "exit":
#                     print("Exiting the shop. Thank you for visiting!")
#                     break  # Exit the loop if the user types 'exit'
#
#                 quantity = int(
#                     input(f"How many '{item_name}' would you like to buy? ")
#                 )
#
#                 # Validate if the item exists in the shop
#                 if self.checker(
#                     item_name, quantity
#                 ):  # Assuming `checker` validates item existence
#                     print()
#                     self.buy_item(item_name, quantity)
#                     self.item_utility.display_items()
#                     self.item_utility.display_money()
#
#                 # Ask if the user wants to continue
#                 while True:
#                     continue_shopping = (
#                         input(
#                             "Would you like to buy something else? (yes/no): "
#                         )
#                         .strip()
#                         .lower()
#                     )
#                     if continue_shopping == "no":
#                         print("Thank you for shopping! Goodbye!")
#                         continue_shopping = False
#                         break
#                     elif continue_shopping == "yes":
#                         break
#                     else:
#                         continue
#
#         def show_items_for_sale(
#             self,
#         ):  # The store is displayed as well as its items
#             print()
#             print("Store: ")
#             for item_name, item_info in self.shop_items_dict.items():
#                 print(f"{item_name}: {item_info}")
#                 print()
#
#         def checker(self, chosen_item: str, quantity: int):
#             # Validate if the chosen item exists in the shop
#             if chosen_item not in self.shop_items_dict:
#                 print(f"Sorry, {chosen_item} is not available in the shop.")
#                 return False
#
#             # Validate if the quantity is valid
#             if quantity <= 0:
#                 print("Invalid quantity. Please enter a positive number.")
#                 return False
#
#             # Check if the shop has enough stock
#             if (
#                 quantity
#                 > self.shop_items_dict[chosen_item][
#                     self.character.quantity_tag
#                 ]
#             ):
#                 print(
#                     f"Sorry, we only have {self.shop_items_dict[chosen_item][self.character.quantity_tag]} "
#                     f"{chosen_item}(s) left in stock."
#                 )
#
#                 return False
#
#             # Calculate the total price of the purchase
#             total_price_of_purchase = (
#                 quantity
#                 * self.shop_items_dict[chosen_item][self.character.price_tag]
#             )
#
#             # Check if the user can afford the purchase
#             if total_price_of_purchase > self.character.money_value:
#                 print("You can't afford this!")
#                 return False
#
#             # Check if the user has enough inventory space for the purchase
#             if not self.has_inventory_space(quantity):
#                 print("Not enough inventory space to buy these items.")
#                 return False
#
#             return True
#             # # If all conditions pass, process the purchase
#             # self.shop_items_dict[chosen_item]["quantity"] -= quantity
#             # self.money_value -= total_price_of_purchase
#             # self.buy_item(chosen_item, quantity)
#             #
#             # # Remove the item from the shop if its stock is now 0
#             # if self.shop_items_dict[chosen_item]["quantity"] == 0:
#             #     del self.shop_items_dict[chosen_item]
#             #
#             # # Return success message
#             # return (f"You successfully bought {quantity} {chosen_item}(s) ")
#
#
# class Inventory:
#     def __init__(
#         self,
#         character: Character,
#         item_utility: ItemUtilityMixin,
#         items_undiscovered_dict: dict,
#     ):
#         if True:
#             self.character = character
#             self.item_utility = item_utility  # ItemUtilityMixin instance
#             self.items_undiscovered_dict = items_undiscovered_dict
#
#     if True:
#
#         def has_inventory_space(self, add_quantity: int) -> bool:
#             total_items = sum(
#                 item[self.character.quantity_tag]
#                 for item in self.character.items.values()
#             )
#             return (
#                 total_items + add_quantity
#                 <= self.character.max_inventory_space
#             )
#
#         def add_items(self, new_items: str, quantity: int):
#             checked = False
#             for item_name, item_data in self.items_undiscovered_dict.items():
#                 if new_items in item_name:
#                     if quantity > 0:
#                         if (
#                             quantity
#                             <= self.items_undiscovered_dict[item_name][
#                                 self.character.quantity_tag
#                             ]
#                         ):
#                             if self.has_inventory_space(quantity):
#
#                                 if item_name in self.character.items:
#                                     self.character.items[item_name][
#                                         self.character.quantity_tag
#                                     ] += quantity
#                                 else:
#                                     self.character.items[item_name] = (
#                                         copy.deepcopy(item_data)
#                                     )
#                                     self.character.items[item_name][
#                                         self.character.quantity_tag
#                                     ] = quantity
#
#                                 self.items_undiscovered_dict[item_name][
#                                     self.character.quantity_tag
#                                 ] -= quantity
#
#                                 checked = True
#                                 if (
#                                     self.items_undiscovered_dict[item_name][
#                                         self.character.quantity_tag
#                                     ]
#                                     == 0
#                                 ):
#                                     del self.items_undiscovered_dict[item_name]
#
#                                 input(
#                                     f"{Fore.YELLOW}|{new_items} is now in your inventory with a quantity of {quantity}!|\n\n\n{Fore.RESET}"
#                                 )
#                                 return self.character.items
#
#                             else:
#                                 return "You need more room in your inventory."
#                         else:
#                             return (
#                                 "Enter a quantity that is readily available."
#                             )
#                     else:
#                         return "Enter a positive quantity. Item quantity cannot be negative."
#
#             if not checked:
#                 return "Enter a valid item."
#
#         def remove_items(self, items_to_remove: str, quantity: int):
#
#             if items_to_remove in self.character.items:
#                 if quantity > 0:
#                     if (
#                         quantity
#                         <= self.character.items[items_to_remove][
#                             self.character.quantity_tag
#                         ]
#                     ):
#                         if (
#                             self.character.items[items_to_remove][
#                                 self.character.quantity_tag
#                             ]
#                             > quantity
#                         ):
#                             self.character.items[items_to_remove][
#                                 self.character.quantity_tag
#                             ] -= quantity
#                         else:
#                             del self.character.items[
#                                 items_to_remove
#                             ]  # Remove item completely
#
#                     else:
#                         return "Enter a quantity that is readily available."
#                 else:
#                     return "Enter a positive quantity. Item quantity cannot be negative."
#
#             else:
#                 return "Enter a valid item."
#
#             return self.character.items
#
#         def use_items(self, item_use, quantity):
#             # Check if the item exists in the player's inventory
#             if item_use not in self.character.items:
#                 return f"Item '{item_use}' does not exist in the inventory!"
#
#             # Check if there is enough quantity of the item
#             if (
#                 self.character.items[item_use][self.character.quantity_tag]
#                 < quantity
#             ):
#                 return f"Not enough quantity of '{item_use}' to use {quantity} units!"
#
#             # Calculate the healing effect of the item
#             heal_amount = (
#                 self.character.items[item_use][self.character.heal_tag]
#                 * quantity
#             )
#
#             # Update the player's health using the heal amount
#             self.character.update_health_by(heal_amount)
#
#             # Reduce the item's quantity
#             self.character.items[item_use][
#                 self.character.quantity_tag
#             ] -= quantity
#
#             # If the quantity reaches 0, remove the item from the inventory
#             if (
#                 self.character.items[item_use][self.character.quantity_tag]
#                 <= 0
#             ):
#                 del self.character.items[item_use]
#
#             # Return the player's updated health (bars_num)
#             return self.character.bars_num
#
#
# class Money:
#     def __init__(self, character: Character, item_utility: ItemUtilityMixin):
#         if True:
#             self.character = character
#             self.item_utility = item_utility  # Store item utility
#
#     if True:
#
#         def money_get(self, money_earned: float):
#             self.character.money_value += money_earned
#             return self.character.money_value
#
#         def money_lose(self, money_lost: float):
#             self.character.money_value -= money_lost
#             return self.character.money_value
#
#         def money_initialize_to(self, initially: float = 2):  # default
#             self.character.money_value = initially
#             return self.character.money_value
#
#         def money_reset_to(self, reset_money: float = 2):  # default
#             self.character.money_value = reset_money
#             return self.character.money_value
#
#         def money_multiply(self, multiplier: float = 1.2):  # default
#             self.character.money_value *= multiplier
#             return self.character.money_value
#
#         def money_divide(self, divider: float = 1.2):  # default
#             self.character.money_value /= divider
#             return self.character.money_value
#
#         def become_rich(self, unlimited: float = 1000):  # default
#             self.character.money_value = unlimited
#             return self.character.money_value
#
#         def become_poor(self, limited: float = 0):  # default
#             self.character.money_value = limited
#             return self.character.money_value
#
#         def become_middle_class(self, normal: float = 100):
#             self.character.money_value = normal
#             return self.character.money_value
#
#         def generate_income(self, income: float = 8, week: int = 5):  # default
#             for _ in range(week):
#                 self.character.money_value += income
#             return self.character.money_value
#
#         def reduction_in_money(
#             self, reduction: float = 2, week: int = 5
#         ):  # default
#             for _ in range(week):
#                 self.character.money_value -= reduction
#             return self.character.money_value
#
#         def display_money(self):
#             print(
#                 f"{Fore.YELLOW}💰 Money: {Style.BRIGHT}{self.character.money_value}{Style.RESET_ALL}"
#             )
#
#
# def print_fonts(
#     text: str,
#     font_type: str = "default",
#     color: tuple = (255, 255, 255),
#     delay: float = 0.0,
# ):
#     """
#     Args:
#         text (str): The text to print.
#         font_type (str): The font type ("bold", "italic", etc., or "default").
#         color (tuple): RGB values for coloring the text (e.g., (255, 0, 0) for red).
#         delay (float): Time delay (in seconds) between printing each character.
#     """
#
#     # ANSI escape codes for font styles
#     styles = {
#         "default": "0",
#         "bold": "1",
#         "italics": "3",
#         "underline": "4",
#     }
#
#     # Get the style code
#     style_code = styles.get(font_type.lower(), "0")
#
#     # Convert RGB color to ANSI escape sequence
#     red, green, blue = color
#     color_code = f"\033[38;2;{red};{green};{blue}m"
#
#     # Combine style and color codes
#     start_code = f"\033[{style_code};{color_code[2:]}"
#     reset_code = "\033[0m"
#
#     # Print the text with delay
#     for char in text:
#         print(f"{start_code}{char}{reset_code}", end="", flush=True)
#         time.sleep(delay)
#     print()  # Line break after finishing text
#
#
# # End of Code
