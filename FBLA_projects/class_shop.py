from class_character import Character
from class_font import print_fonts
import copy


class Shop:


   def __init__(self, character: Character):
       self.character = character


   """Checks if player has any inventory space left"""
   def has_inventory_space(self, add_quantity: int = 0) -> bool:
       total_items = sum(item[self.character.quantity_tag] for item in
                         self.character.items.values())
       return total_items + add_quantity <= self.character.max_inventory_space


   """Player buys an item"""
   def buy_item(self, new_items: str, quantity: int) -> bool:
       old_quantity, new_quantity = self.character.sum_of_character_items(), None
       old_money, new_money = self.character.return_money_value(), None
       arrow = "-->"


       for item_name, item_data in self.character.shop_items_dict.items():
           if new_items in item_name:
               if quantity > 0:
                   if quantity <= \
                           self.character.shop_items_dict[item_name][
                               self.character.quantity_tag]:
                       total_price = \
                       self.character.shop_items_dict[item_name][
                           self.character.price_tag] * quantity
                       if self.character.money_value >= total_price:
                           if self.has_inventory_space(quantity):


                               self.character.money_value -= total_price


                               if item_name in self.character.items:
                                   self.character.items[item_name][
                                       self.character.quantity_tag] += quantity


                               else:
                                   self.character.items[
                                       item_name] = copy.deepcopy(
                                       item_data)
                                   self.character.items[item_name][
                                       self.character.quantity_tag] = quantity


                               self.character.shop_items_dict[
                                   item_name][
                                   self.character.quantity_tag] -= quantity


                               if self.character.shop_items_dict[
                                   item_name][
                                   self.character.quantity_tag] == 0:
                                   del self.character.shop_items_dict[
                                       item_name]


                               new_quantity = self.character.sum_of_character_items()
                               new_money = self.character.return_money_value()


                               data_collector = f"""{self.character.name} has bought '{new_items}' with a quantity of '{quantity}'.
Sum of Item '{new_items}': {old_quantity} {arrow} {new_quantity}
Sum of Money: ${old_money} {arrow} ${new_money}"""
                               self.character.display_items(True)
                               self.character.display_money(True)
                               print(data_collector)
                               return True


                           else:
                               info_checker = "You need more room in your inventory."
                               print(info_checker)
                               return False
                       else:
                           info_checker = "You do not have enough money."
                           print(info_checker)
                           return False
                   else:
                       info_checker = "Enter a quantity that is readily available."
                       print(info_checker)
                       return False
               else:
                   info_checker = "Enter a positive quantity. Item quantity cannot be negative."
                   print(info_checker)
                   return False


       info_checker = "Enter a valid item."
       print(info_checker)
       return False


   """Player goes into a shop and buys multiple items"""
   def currently_buying_items(self) -> bool:
       self.character.character_stats()


       # Loop to allow the user to continue buying items until they choose to stop
       continue_shopping = True
       while continue_shopping:
           self.show_items_for_sale()  # Assuming there’s a method to display available shop items


           # Prompt the user to enter the item they want to buy
           while True:
               item_name = input(
                   "Enter the name of the item you want to buy (or type 'exit' to stop): ").strip()
               quantity = 1


               if item_name.lower() == 'exit':
                   print("Exiting the shop. Thank you for visiting!")
                   break  # Exit the loop if the user types 'exit'


               elif not self.checker(item_name, quantity):
                   break


               else:


                   while True:
                       quantity = input(
                           f"How many '{item_name}' would you like to buy? (or type 'exit' to stop): ")


                       if quantity.lower() == 'exit':
                           print(
                               "Exiting the shop. Thank you for visiting!")
                           break  # Exit the loop if the user types 'exit'
                       elif self.checker(item_name, int(quantity)):
                           print()
                           quantity = int(quantity)
                           self.buy_item(item_name, quantity)
                           break
                   break


           # Ask if the user wants to continue
           while True:
               continue_shopping = input(
                   "Would you like to buy something else? (Y/N): ").strip().upper()
               if continue_shopping == "N":
                   print("Thank you for shopping! Goodbye!")
                   continue_shopping = False
                   break
               elif continue_shopping == "Y":
                   break
       return False


   """Shop displays items that are for sale"""
   def show_items_for_sale(
           self):  # The store is displayed as well as its items
       print_fonts("Store: ", "underline")
       fancy = "***"
       red, green, blue = 200, 100, 0
       inc = 10
       for item_name, item_info in self.character.shop_items_dict.items():


           print_fonts(f"{fancy}{item_name}{fancy}", "bold",
                       (100, 150, blue))
           for attribute, value in item_info.items():
               blue += inc
               if blue >= 255:
                   blue = 255
                   inc *= -1
               elif blue <= 0:
                   blue = 0
                   inc *= -1
               print_fonts(f"{attribute.capitalize()}: {value}",
                           "italic", (red, green, blue))


           print()
       return self.character.shop_items_dict


   "Checks to make sure user picks a reasonable item and amount"
   def checker(self, chosen_item: str, quantity: int):
       # Validate if the chosen item exists in the shop


       if chosen_item not in self.character.shop_items_dict:
           print(
               f"Sorry, {chosen_item} is not available in the shop.")
           return False


       # Validate if the quantity is valid
       elif quantity <= 0:
           print("Invalid quantity. Please enter a positive number.")
           return False


       # Check if the shop has enough stock
       elif quantity > self.character.shop_items_dict[chosen_item][
           self.character.quantity_tag]:
           print(
               f"Sorry, we only have {self.character.shop_items_dict[chosen_item][self.character.quantity_tag]} "
               f"{chosen_item}(s) left in stock.")


           return False


       # Check if the user can afford the purchase
       elif (quantity * self.character.shop_items_dict[
           chosen_item][
           self.character.price_tag]) > self.character.money_value:
           print("You can't afford this!")
           return False


       # Check if the user has enough inventory space for the purchase
       elif not self.has_inventory_space(quantity):
           print("Not enough inventory space to buy these items.")
           return False


       else:
           return True
