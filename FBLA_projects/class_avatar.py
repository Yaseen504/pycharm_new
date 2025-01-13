

from class_battle import Battle
from class_character import Character
from class_inventory import Inventory
from class_money import Money
from class_shop import Shop


"""
Allows users to use methods within the character class.
[Name Of Character].[Character Class].[Class Of Choice].[Method of Choice] ()
[Name].[Character Class].[Class].[Method] ()
IE. Jake.character.inventory.add_items()
"""


class Avatar(Character):
   def __init__(self, character: Character):
       self.character = character
       super().__init__(**vars(self.character))


       #Character Class
       self.character = Character(**vars(self.character))


       #Inventory Class
       self.character.inventory = Inventory(self.character)


       #Shop Class
       self.character.shop = Shop(self.character)


       #Money Class
       self.character.money = Money(self.character)


       #Battle Class
       self.character.battle = Battle(self.character)