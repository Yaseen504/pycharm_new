from class_character import Character
from colorama import Fore, Style, init
init()


"""Manipulates money"""

class Money:
   def __init__(self, character: Character):
       self.character = character

   def money_get(self, money_earned: float):
       self.character.money_value += money_earned
       return self.character.money_value

   def money_lose(self, money_lost: float):
       self.character.money_value -= money_lost
       return self.character.money_value

   def money_initialize_to(self, initially: float = 2):  # default
       self.character.money_value = initially
       return self.character.money_value

   def money_reset_to(self, reset_money: float = 2):  # default
       self.character.money_value = reset_money
       return self.character.money_value

   def money_multiply(self, multiplier: float = 1.2):  # default
       self.character.money_value *= multiplier
       return self.character.money_value

   def money_divide(self, divider: float = 1.2):  # default
       self.character.money_value /= divider
       return self.character.money_value

   def become_rich(self, unlimited: float = 1000):  # default
       self.character.money_value = unlimited
       return self.character.money_value

   def become_poor(self, limited: float = 0):  # default
       self.character.money_value = limited
       return self.character.money_value

   def become_middle_class(self, normal: float = 500):
       self.character.money_value = normal
       return self.character.money_value

   def generate_income(self, income: float = 8,
                       week: int = 5):  # default
       for _ in range(week):
           self.character.money_value += income
       return self.character.money_value

   def reduction_in_money(self, reduction: float = 2,
                          week: int = 5):  # default
       for _ in range(week):
           self.character.money_value -= reduction
       return self.character.money_value

   def display_money(self):
       print(
           f"{Fore.YELLOW}💰 Money: {Style.BRIGHT}{self.character.money_value}{Style.RESET_ALL}")