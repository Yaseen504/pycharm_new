from class_character import Character
from colorama import Fore, Style, init
init()
import copy




"""Handles all the work for the inventory. Great for storing and manipulating items."""
class Inventory:
   def __init__(self, character: Character):
       self.character = character


       self.exit = "(Type 'exit' to [exit]): "


   """Checks if player has any inventory space left"""
   def has_inventory_space(self, add_quantity: int = 0) -> bool:
       total_items = sum(item[self.character.quantity_tag] for item in
                         self.character.items.values())
       return total_items + add_quantity <= self.character.max_inventory_space


   """Adds an item for the player"""
   def add_items(self, new_items: str, quantity: int) -> bool:


       old_quantity, new_quantity = self.character.sum_of_character_items(), None
       arrow = "-->"




       for item_name, item_data in self.character.items_undiscovered_dict.items():
           if new_items in item_name:
               if quantity > 0:
                   if quantity <= \
                           self.character.items_undiscovered_dict[
                               item_name][
                               self.character.quantity_tag]:
                       if self.has_inventory_space(quantity):
                           if item_name in self.character.items:
                               self.character.items[item_name][
                                   self.character.quantity_tag] += quantity
                           else:
                               self.character.items[
                                   item_name] = copy.deepcopy(
                                   item_data)
                               self.character.items[item_name][
                                   self.character.quantity_tag] = quantity


                           self.character.items_undiscovered_dict[
                               item_name][
                               self.character.quantity_tag] -= quantity


                           if \
                           self.character.items_undiscovered_dict[
                               item_name][
                               self.character.quantity_tag] == 0:
                               del \
                               self.character.items_undiscovered_dict[
                                   item_name]


                           new_quantity = self.character.sum_of_character_items()


                           data_collector = f"""'{new_items}' has been added into {self.character.name}'s Inventory with quantity of '{quantity}'.
Sum of Item '{new_items}': {old_quantity} {arrow} {new_quantity}"""


                           self.character.display_items(True)
                           print(data_collector)
                           print()
                           return True


                       else:
                           info_checker = "You need more room in your inventory."
                           print(info_checker)
                           print()


                           return False
                   else:
                       info_checker = "Enter a quantity that is readily available."  # meaning that the dictionary has that amount of items per your needs
                       print(info_checker)
                       print()


                       return False
               else:
                   info_checker = "Enter a positive quantity. Item quantity cannot be negative."
                   print(info_checker)
                   print()


                   return False


       info_checker = "Enter a valid item."
       print(info_checker)
       return False


   """Removes an item for the player"""
   def remove_items(self, items_to_remove: str,
                    quantity: int) -> bool:


       old_quantity, new_quantity = self.character.sum_of_character_items(), None
       arrow = "-->"


       if items_to_remove in self.character.items:
           if quantity > 0:
               if quantity <= self.character.items[items_to_remove][
                   self.character.quantity_tag]:
                   if self.character.items[items_to_remove][
                       self.character.quantity_tag] > quantity:
                       self.character.items[items_to_remove][
                           self.character.quantity_tag] -= quantity
                       new_quantity = self.character.sum_of_character_items()
                   else:
                       del self.character.items[
                           items_to_remove]  # Remove item completely
                       new_quantity = 0


                   data_collector = f"""'{items_to_remove}' with a quantity of '{quantity}' has been removed from {self.character.name}'s Inventory.
Sum of Item '{items_to_remove}': {old_quantity} {arrow} {new_quantity}"""
                   self.character.display_items(True)
                   print(data_collector)
                   print()
                   return True
               else:
                   info_checker = "Enter a quantity that is readily available."
                   print(info_checker)
                   print()
                   return False
           else:
               info_checker = "Enter a positive quantity. Item quantity cannot be negative."
               print(info_checker)
               print()
               return False
       else:
           info_checker = "Enter a valid item."
           print(info_checker)
           print()
           return False


   """Player uses the item and gains health"""
   def use_item(self, item_use:str , quantity:int):


       old_quantity, new_quantity = self.character.items[item_use][self.character.quantity_tag], None
       arrow = "-->"
       before_health, after_health = self.character.bars_num, None


       old_quantity_total =  self.character.sum_of_character_items()


       # Check if the item exists in the player's inventory
       if item_use not in self.character.items:
           info_checker = f"Item '{item_use}' does not exist in the inventory!"
           print(info_checker)
           print()
           return False


       # Check if there is enough quantity of the item
       if self.character.items[item_use][
           self.character.quantity_tag] < quantity:
           info_checker = f"Not enough quantity of '{item_use}' to use {quantity} units!"
           print(info_checker)
           print()
           return False


       # Calculate the healing effect of the item
       heal_amount = self.character.items[item_use][
                         self.character.heal_tag] * quantity


       # Update the player's health using the heal amount
       self.character.update_health_by(heal_amount)
       after_health = self.character.bars_num


       # Reduce the item's quantity
       self.character.items[item_use][
           self.character.quantity_tag] -= quantity


       # If the quantity reaches 0, remove the item from the inventory
       if self.character.items[item_use][
           self.character.quantity_tag] <= 0:
           del self.character.items[item_use]
           new_quantity = 0
       else:
           new_quantity = self.character.items[item_use][self.character.quantity_tag]


       new_quantity_total =  self.character.sum_of_character_items()


       # Return the player's updated health (bars_num)
       data_collector = f"""{self.character.name} has used '{item_use}' with a quantity of '{quantity}';
Healed by {heal_amount}hp: {before_health}hp {arrow} {after_health}hp
Sum of Item '{item_use}': {old_quantity} {arrow} {new_quantity}
Sum of Total Items: {old_quantity_total} {arrow} {new_quantity_total}"""


       self.character.display_items(True)
       self.character.display_health()
       print(data_collector)
       print()
       return True






   def choose_item(self, include_damage_affect = False, include_healing_affect = False) -> str:  # Character chooses a weapon/power/superpower
       item_choice = False
       pick_item_choice = None
       if self.character.items:
           while not item_choice:
               print("Available Item: ")
               self.character.display_items()  # Use self.character
               pick_item_choice = input(f"Choose a item from the list above {self.exit}")




               if pick_item_choice == 'exit':
                   print("You didn't choose an item. Exiting...")
                   break


               elif pick_item_choice in self.character.items:  # Use self.character
                   if not include_damage_affect:
                       if not include_healing_affect:
                           print("You have chosen:", pick_item_choice)
                           item_choice = True
                           break
                       else:
                           if self.character.heal_tag in self.character.items[pick_item_choice]:
                               print("You have chosen:", pick_item_choice)
                               item_choice = True
                               break
                           else:
                               print(f"Please choose an item that has a {self.character.heal_tag} affect!")
                               item_choice = False
                               break


                   else:
                       while True:
                           if self.character.damage_tag in self.character.items[pick_item_choice]:
                               print("You have chosen:", pick_item_choice)
                               item_choice = True
                               break
                           else:
                               print(f"Please choose an item that has a {self.character.damage_tag} affect!")
                               item_choice = False
                               break




               else:
                   print("Invalid choice. Please try again.")
       else:
           print(
               "Sorry, it looks like you do not have any items. Choose "
               "another option")




       return pick_item_choice








   """Returns the current items."""
   def get_items(self) -> dict:
       return self.character.items


   """Returns the total UNIQUE item count."""
   def get_item_unique_count(self) -> int:
       return len(self.character.items)


   """Returns the total item count."""
   def get_item_full_count(self) -> int:
       total_items = sum(
           item[self.character.quantity_tag] for item in self.character.items.values())
       return total_items


   """Display the Items"""
   def display_items(self, extra: bool = False):
       if extra: self.character.display_name()
       _ = ""
       if not self.character.items:
           print(
               f"{Fore.YELLOW}🎒 Items: {Style.BRIGHT}No Items Available{Style.RESET_ALL}")
       else:
           print(f"{Fore.YELLOW}🎒 Items: {Style.RESET_ALL}")
           for item, item_type in self.character.items.items():
               for attribute, information in item_type.items():
                   if _ != item:
                       print(
                           f"\t{Fore.CYAN}• {Style.BRIGHT}{item}{Style.RESET_ALL}")
                   print(
                       f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}")
                   _ = item


           total_items = sum(item[self.character.quantity_tag] for item in
                             self.character.items.values())
           print(
               f"{Fore.CYAN}📦 Total Items: {Style.BRIGHT}{total_items} / {self.character.max_inventory_space}{Style.RESET_ALL}")


       return self.character.items
