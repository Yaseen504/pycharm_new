from colorama import Fore, Style, init
from utilities import clear_terminal, press_enter_arrow

init()
import os

"""
Character Class - The character class takes in all the initialization values per character
created under the Avatar Class.
"""

class Character:
  def __init__(self,
               name: str,
               damage: int = None,
               money_value: float = None,
               max_inventory_space: int = None,
               bars_num: int = None,
               powers: dict = None,
               items: dict = None,
               health: str = "",
               max_bars_num: int = None,
               original_bars_num: str = None,
               heal_tag: str = None,
               quantity_tag: str = None,
               price_tag: str = None,
               info_tag: str = None,
               rarity_tag: str = None,
               type_tag: str = None,
               damage_tag: str = None,
               shop_items_dict: dict = None,
               powers_dict: dict = None,
               items_undiscovered_dict: dict = None,
               scale_health: int = None,
               symbol_of_health: str = None) -> None:

      if True:
          """Storage of all dictionaries"""
          self.shop_items_dict = shop_items_dict or {}
          self.powers_dict = powers_dict or {}
          self.items_undiscovered_dict = items_undiscovered_dict or {}

      if True:
          self.name = name  # NAME
          self.damage = damage or 5  # Damage response
          self.powers = powers or {}

          self.health = health  # Health

      if True:
          """
          Tags the dictionaries would use.
          Always update the tag per key update in dictionaries
          """
          self.heal_tag = heal_tag or "heal"
          self.price_tag = price_tag or "price"
          self.quantity_tag = quantity_tag or "quantity"
          self.info_tag = info_tag or "info"
          self.rarity_tag = rarity_tag or "rarity"
          self.type_tag = type_tag or "type"
          self.damage_tag = damage_tag or "damage"

      if True:
          self.bars_num = bars_num or 100  # Health value set up
          self.max_bars_num = max_bars_num or round(
              self.bars_num * 1.25)  # Max potential health
          if self.bars_num > self.max_bars_num:
              self.bars_num = self.max_bars_num  # Player's health has to be limited
          self.original_bars_num = original_bars_num or self.bars_num  # Original health

          self.scale_health = scale_health or 2
          self.symbol_of_health = symbol_of_health or ":"
          self.health = self.symbol_of_health * \
              int((round(self.bars_num) / self.scale_health))  # Use self.character

          # Note: bars = num of bars - int - ie 5
          # Note: health = amount of health - string - ie '======'

      if True:

          self.items = items or {}

          # Call the function once

          def total_items_calc():
              total_items = 0
              for item_name, item_value in self.items.items():
                  for key, value in item_value.items():
                      if key == self.quantity_tag:
                          total_items += value

              return total_items

          total_items = total_items_calc()

          """Calculates the max space to store those items"""
          self.max_inventory_space = max_inventory_space or round(
              total_items * 1.25)

          """Deletes [certain] items if exceeds max space"""

          while total_items > self.max_inventory_space:
              for item_name in self.items.keys():
                  if self.items[item_name][self.quantity_tag] > 0:
                      self.items[item_name][self.quantity_tag] -= 1
                      if self.items[item_name][self.quantity_tag] == 0:
                          del self.items[item_name]
                      break
              total_items = total_items_calc()

      if True:
          # Money available (can be a decimal)
          self.money_value = money_value or 250

  if True:
      """Displays Parts Of Character's Characteristics"""

      def display_name(self):
          print(
              f"{Fore.GREEN}🌟 Name: {Style.BRIGHT}{self.name}{Style.RESET_ALL}")
          return self.name

      def display_damage(self, extra: bool = False):
          if extra:
            self.display_name()
          print(
              f"{Fore.RED}⚔️ Damage: {Style.BRIGHT}{self.damage}{Style.RESET_ALL}")
          return self.damage

      def display_powers(self, extra: bool = False):
          if extra:
            self.display_name()

          _ = ""
          if not self.powers:
              print(
                  f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}")
          else:
              print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
              for power, power_type in self.powers.items():
                  for attribute, information in power_type.items():
                      if _ != power:
                          print(
                              f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}")
                      print(
                          f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}")
                      _ = power
          return self.powers

      def display_health(self, extra: bool = False):
          if extra:
            self.display_name()

          print(
              f"{Fore.GREEN}❤️ Health: {Style.BRIGHT}{self.health}{Style.RESET_ALL} : {Fore.MAGENTA}{self.bars_num}hp{Style.RESET_ALL}")
          return self.health, self.bars_num

      def display_max_health(self, extra: bool = False):
          if extra:
            self.display_name()
          print(
              f"{Fore.MAGENTA}💪 Max Health Possible: {Style.BRIGHT}{self.max_bars_num}{Style.RESET_ALL}")
          return self.max_bars_num

      def display_items(self, extra: bool = False):
          if extra:
            self.display_name()
          _ = ""
          if not self.items:
              print(
                  f"{Fore.YELLOW}🎒 Items: {Style.BRIGHT}No Items Available{Style.RESET_ALL}")
          else:
              print(f"{Fore.YELLOW}🎒 Items: {Style.RESET_ALL}")
              for item, item_type in self.items.items():
                  for attribute, information in item_type.items():
                      if _ != item:
                          print(
                              f"\t{Fore.CYAN}• {Style.BRIGHT}{item}{Style.RESET_ALL}")
                      print(
                          f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}")
                      _ = item

              total_items = sum(item[self.quantity_tag] for item in
                                self.items.values())
              print(
                  f"{Fore.CYAN}📦 Total Items: {Style.BRIGHT}{total_items} / {self.max_inventory_space}{Style.RESET_ALL}")

          return self.items

      def display_max_inventory_space(self, extra: bool = False):
          if extra:
            self.display_name()
          print(
              f"{Fore.MAGENTA}📚 Max Inventory Space: {Style.BRIGHT}{self.max_inventory_space}{Style.RESET_ALL}")
          return self.max_inventory_space

      def display_money(self, extra: bool = False):
          if extra:
            self.display_name()
          print(
              f"{Fore.YELLOW}💰 Money: {Style.BRIGHT}{self.money_value}{Style.RESET_ALL}")
          return self.money_value

  if True:
      """Displays Most Of Character's Characteristics"""

      def character_stats(self):  # Shows the overall stats
          os.system("cls" if os.name == "nt" else "clear")
          print(
              f"\n\t\t{Fore.CYAN}🌟 Stats for {Style.BRIGHT}{self.name}{Style.RESET_ALL}")
          print(
              f"{Fore.GREEN}~~!﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏!~~{Style.RESET_ALL}")
          self.display_name()
          self.display_damage()
          self.display_powers()
          self.display_health()
          self.display_max_health()
          self.display_items()
          self.display_max_inventory_space()
          self.display_money()
          print(
              f"{Fore.RED}-------------------------------------------------{Style.RESET_ALL}\n")

      def simple_display_stats(self):
          print(f"{Fore.GREEN}🌟 Name: {self.name}")
          print(f"{Fore.RED}❤️ HP: {self.health} {self.bars_num}")
          print(f"{Fore.YELLOW}💰 Money: ${self.money_value}")
          print(f"{Fore.BLUE}🎒 Inventory: {self.items}")
          print(
              f"{Fore.MAGENTA}🌀 Powers: {self.powers}{Style.RESET_ALL}")

          return self.name, self.bars_num, self.money_value, self.items, self.powers

  if True:

      """Few of Character's Essential Methods"""

      def update_health_by(self, delta):
          self.bars_num = min(max(0, self.bars_num + delta),
                              self.max_bars_num)
          if self.bars_num >= self.max_bars_num:
              self.bars_num = self.max_bars_num

          self.health = self.symbol_of_health * \
              int((round(self.bars_num) / self.scale_health))  # Use self.character

          return self.bars_num

      def update_health_to(self, delta):
          self.bars_num = min(max(0, delta), self.max_bars_num)
          if self.bars_num >= self.max_bars_num:
              self.bars_num = self.max_bars_num

          self.health = self.symbol_of_health * int((round(
              self.bars_num) / self.scale_health))  # Use self.character

          return self.bars_num

      def sum_of_character_items(self):
          total_items = sum(item[self.quantity_tag]
                            for item in self.items.values())
          return total_items

      def return_money_value(self):
          return self.money_value

      def return_current_health(self):
          return self.bars_num