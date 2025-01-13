from class_character import Character
from class_inventory import  Inventory
from colorama import Fore, Style, init
import math
import random
from class_font import print_fonts
init()


class Battle:
   def __init__(self, character: Character):
       self.character = character  # Store character object
       self.consequences = ["fainted", "died", "injured", "lost",
                            "killed"]  # specific consequences when battle ends


       self.choices = ["Fight","Heal","Skip","Throw","Flee"]
       self.character.inventory = Inventory(self.character)


       self.exit = "(Type 'exit' to [exit]): "




   def return_player_bars_num(self, show:bool=False)-> int:
       if show:print(f"Character Health Status: {self.character.bars_num}")
       return self.character.bars_num






   def player_get_relative_health_ratio(self) -> float:
       return self.character.bars_num / self.character.original_bars_num


   def player_get_absolute_health_ratio(self) -> float:
       return self.character.bars_num / self.character.max_bars_num


   def player_get_color(self) -> str:
       ratio = self.player_get_relative_health_ratio()
       if ratio >= 0.70:return "green"
       elif ratio >= 0.30:return "yellow"
       else:return "red"


   @staticmethod
   def return_character_bars_num(character2, show=False)-> int:
       if show:print(f"Character Health Status: {character2.character.bars_num}")
       return character2.character.bars_num


   @staticmethod
   def __opponent_get_relative_health_ratio(character2) -> float:
       return character2.character.bars_num / character2.character.original_bars_num


   @staticmethod
   def __opponent_get_absolute_health_ratio(character2) -> float:
       return character2.character.bars_num / character2.character.max_bars_num




   def __opponent_get_color(self, character2) -> str:
       ratio = self.__opponent_get_relative_health_ratio(character2)
       if ratio >= 0.70:return "green"
       elif ratio >= 0.30:return "yellow"
       else:return "red"








   def set_health(self,new_health) -> int:  # sets the health to an integer value in relation to the character
       self.character.bars_num = round(min(max(new_health, 0),self.character.max_bars_num))
       return self.character.bars_num


   def player_return_current_hp(self):
       return self.character.health


   @staticmethod
   def __opponent_return_current_hp(character2):
       return character2.character.health




   # note the * allows the function to take as many positional arguments
   def grant_powers(self,*chosen_power: str) -> list:  # grants powers in respective to the character
       for weapon_name, weapon_info in self.character.powers_dict.items():
           if weapon_name in chosen_power:self.character.powers[weapon_name] = weapon_info  # Use self.character
       return self.character.powers


   def delete_powers(self, *chosen_power: str) -> list:
       for weapon_name in self.character.powers_dict:
           if weapon_name in chosen_power and weapon_name in self.character.powers:  # Use self.character
               del self.character.powers[weapon_name]
       return self.character.powers


   # __ at beginning means name manging, internal use, private members (not recommended to use method outside classes folder)
   def __is_dead(self, character2, net_player_hp: int,
                 net_opponent_hp: int) -> bool:  # use to check if someone is dead (health <= 0)
       if (self.character.bars_num <= 0) or (
               character2.character.bars_num <= 0):  # Use self.character
           if (self.character.bars_num <= 0) and (
                   character2.character.bars_num <= 0):
               self.character.bars_num = 1
               print(
                   "You have managed to use every ounce of strength for this final HP")  # a bonus advantage for player


           if self.character.bars_num <= 0:  # OPPONENT WINS
               self.character.bars_num = 0
               self.display_battle_info(character2, net_player_hp,
                                        net_opponent_hp)


               print()
               self.scene_changes_to("DEATH SCENE")
               print()


               print(f"You have {self.consequences[0]}")
               print(f"{character2.character.name} has won!")
           else:  # PLAYER WINS
               character2.character.bars_num = 0
               self.display_battle_info(character2, net_player_hp,
                                        net_opponent_hp)


               print()
               print("----DEATH----")
               print()


               print(
                   f"{character2.character.name} has {self.consequences[0]}")
               print("You have won!")
           print()
           return True  # death has occurred, game stops


       else:
           return False  # death has NOT occurred; game continues


   def display_powers(self) -> dict:
       _ = ""
       if not self.character.powers:  # Use self.character
           print(
               f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}")
       else:
           print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
           for power, power_type in self.character.powers.items():  # Use self.character
               for attribute, information in power_type.items():
                   if _ != power:
                       print(
                           f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}")
                   print(
                       f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}")
                   _ = power


       return self.character.powers


   def health_limit_check(self) -> bool:  # checks the limits of health that can be reached
       if self.character.bars_num >= self.character.max_bars_num:  print("Max Health Reached.")
       elif self.character.bars_num <= 0: print("Lowest Health Reached")


       return 0 <= self.character.bars_num <= self.character.max_bars_num


   def display_attack_dmg(self) -> int:  # checks how much initial damage you do (like the bare minimum excluding all other aspects)
       print(f"Attack Potency: {Fore.GREEN}{round(self.character.damage, 2)}{Fore.RESET}")  # Use self.character
       return self.character.damage


   def display_health_information(self, net_player_hp) -> int:


       if self.player_get_color() == "green":
           color_system = Fore.GREEN
       elif self.player_get_color() == "yellow":
           color_system = Fore.YELLOW
       else:
           color_system = Fore.RED
       if net_player_hp > 0:  # positive net Health = HEAL / GAIN HEALTH
           print(
               f"Health: {color_system}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET} | {Fore.GREEN}You Gained: {net_player_hp}HP{Fore.RESET}")  # Use self.character
       elif net_player_hp < 0:  # negative net Health = LOSE HEALTH
           print(
               f"Health: {color_system}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET} | {Fore.RED}You Lost: {net_player_hp}HP{Fore.RESET}")  # Use self.character
       else:
           print(
               f"Health: {color_system}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET}")  # Use self.character


       return self.character.bars_num
   # __ at beginning means name manging, internal use, private members (not recommended to use method outside classes folder)
   @staticmethod
   def __display_power_for_opponent(character2) -> dict:
       _ = ""
       if not character2.character.powers:  # Use self.character
           print(
               f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}")
       else:
           print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
           for power, power_type in character2.character.powers.items():  # Use self.character
               for attribute, information in power_type.items():
                   if _ != power:
                       print(
                           f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}")
                   print(
                       f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}")
                   _ = power
       return character2.character.powers


   @staticmethod
   def __health_limit_check_for_opponent(character2) -> bool:
       if character2.character.bars_num >= character2.character.max_bars_num:  print("Max Health Reached.")
       elif character2.character.bars_num <= 0: print("Lowest Health Reached")


       return 0 <= character2.character.bars_num <= character2.character.max_bars_num


   @staticmethod
   def __display_attack_dmg_for_opponent(character2) -> int:
       print(f"Attack Potency: {Fore.GREEN}{round(character2.character.damage, 2)}{Fore.RESET}")  # Use self.character
       return character2.character.damage


   def __display_health_information_for_opponent(self, character2,
                                                 net_opponent_hp) -> bool:


       if self.__opponent_get_color(character2) == "green":
           color_system = Fore.GREEN
       elif self.__opponent_get_color(character2) == "yellow":
           color_system = Fore.YELLOW
       else:
           color_system = Fore.RED


       if net_opponent_hp > 0:  # positive net Health = HEAL / GAIN HEALTH
           print(
               f"Health: {color_system}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET} | {Fore.GREEN}{character2.character.name} Gained: {net_opponent_hp}HP{Fore.RESET}")  # Use self.character
       elif net_opponent_hp < 0:  # negative net Health = LOSE HEALTH
           print(
               f"Health: {color_system}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET} | {Fore.RED}{character2.character.name} Lost: {net_opponent_hp}HP{Fore.RESET}")  # Use self.character
       else:
           print(
               f"Health: {color_system}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET}")  # Use self.character
       return character2.character.bars_num


   def display_battle_info(self, character2, net_player_hp: int,
                           net_opponent_hp: int) -> list:  # Information shown through the display battle class for each character


       #self.scene_changes_to("BATTLE STATS")


       # PLAYER DETAILS
       print(
           f"{Fore.MAGENTA}\n{self.character.name} (YOU){Fore.RESET}")  # Use self.character
       self.display_powers()
       self.display_attack_dmg()
       self.display_health_information(net_player_hp)
       self.health_limit_check()


       # OPPONENT DETAILS
       print(
           f"{Fore.RED}\n{character2.character.name} (OPPONENT){Fore.RESET}")  # Use self.character
       self.__display_power_for_opponent(character2)
       self.__display_attack_dmg_for_opponent(character2)
       self.__display_health_information_for_opponent(character2,
                                                      net_opponent_hp)
       self.__health_limit_check_for_opponent(character2)


       return [self.character.name, character2.character.name]


   def choose_weapon(self) -> str:  # Character chooses a weapon/power/superpower


       while True:
           print("Available powers:",
                 list(self.character.powers.keys()))  # Use self.character
           player_power_choice = input(f"Choose a weapon / power from the list above : {self.exit}: ")


           if player_power_choice in self.character.powers:
               break
           elif player_power_choice == 'exit':
               print("You didn't choose a weapon.")
               break


           else:
               print("Invalid choice. Please try again.")




       return player_power_choice


   @staticmethod  # very static - no .self - local; not global
   def determine_critical_chance(chance: float = 0.30,
                                 multiplier: float = 1.25) -> float:  # Character imposes a critical hit dmg when lucky


       base_multiplier = 1.00
       return multiplier if random.random() <= chance else base_multiplier


   def adjust_health(self, character2, c1: bool = True,
                     c2: bool = True) -> None:  # Adjusts the overall health method for both characters
       if c1:
           if self.character.bars_num >= self.character.max_bars_num:  # A defined max health limit for player # Use self.character
               self.character.bars_num = self.character.max_bars_num  # Use self.character
           self.character.health = "=" * int(
               round(self.character.bars_num))  # Use self.character


       if c2:
           if character2.character.bars_num >= character2.character.max_bars_num:  # A defined max health limit for opponent # Use self.character
               character2.character.bars_num = character2.character.max_bars_num  # Use self.character
           character2.character.health = "=" * int(
               round(character2.character.bars_num))  # Use self.character










   def initialize_fight(self) -> str:  # initializes the fight scene


       while True:
           print_fonts(text = f"Choices : {' 🦾 '.join(self.choices)} " , font_type = "italic", color=(250,150,200))  # Want to fight?
           print_fonts(text = "What will you choose? ", font_type="bold", color=(200,170,255))
           if (attack_result := input("Choice: ").lower().strip()) in [choice.lower().strip() for choice in self.choices]: break


       return attack_result


   @staticmethod
   def scene_changes_to(scene: str) -> str:
       # print_fonts(text = "\n😎--------------------------------------------------------------------------------😎", color = (255,160,155))
       print_fonts(text = f"\t\t\t\t-*-*-*-* {scene.upper()} *-*-*-*-\t\t\t\t", font_type = "italic", color = (255,200,150))
       # print_fonts(text = "😎--------------------------------------------------------------------------------😎\n", color = (255,160,155))
       return scene.upper()


   @staticmethod
   def net_health_calc(before_hp: int, after_hp: int) -> int:
       return after_hp - before_hp




   def _player_dmg_taken(self, overall_opponent_dmg: int) -> int:
       self.character.bars_num -= overall_opponent_dmg
       return self.character.bars_num


   @staticmethod
   def _opponent_dmg_taken(character2, overall_player_dmg: int) -> int:
       character2.character.bars_num -= overall_player_dmg
       return character2.character.bars_num


   def fight(self, character2):
       if (self.character.powers or character2.character.powers) and (
               (self.character.bars_num > 0) and (
               character2.character.bars_num > 0)):  # NEEDS A POWER before fighting # Use self.character
           net_player_hp, net_opponent_hp = 0, 0  # local variables to calculate NET HP for opponent *relative to each attack
                                               # local variables to calculate NET HP for player *relative to each attack


           before_player_hp, before_opponent_hp = self.character.return_current_health(), character2.character.return_current_health()


           player_option_choose = None
           self.adjust_health(character2, True, True)


           fighting = True
           player_turn = True




           while fighting:
               while player_turn:
                   self.scene_changes_to("BATTLE STATS")
                   self.display_battle_info(character2, net_player_hp,
                                            net_opponent_hp) # displays the battle info




                   net_player_hp, net_opponent_hp = 0, 0  # reset
                   before_player_hp, before_opponent_hp = self.character.return_current_health(), character2.character.return_current_health()




                   self.scene_changes_to("MAIN SCENE")
                   player_option_choose = self.initialize_fight() #brings out the choices




                   if player_option_choose == "fight".lower().strip():
                       self.scene_changes_to("CHOICE SCENE")
                       player_power_choice = self.choose_weapon()  # What powers/weapon does the player want to choose?


                       if player_power_choice != 'exit'.lower().strip():
                           self.scene_changes_to("FIGHTING SCENE")


                           # OVERALL DAMAGE AFFECT FOR PLAYER
                           overall_player_dmg = round((player_dmg := round(
                                self.character.powers[player_power_choice][self.character.damage_tag] + self.character.damage)) * (
                                                                        player_critical_dmg := self.determine_critical_chance()))  # Use self.character


                           self._opponent_dmg_taken(character2, overall_player_dmg)


                           if player_critical_dmg != 1.00:
                               print("CRITICAL DAMAGE!")
                               print(f"({player_dmg}) to ({overall_player_dmg}) by {(player_critical_dmg - 1.00) * 100}%")


                           print(f"You have used '{player_power_choice}' with attack_dmg of {overall_player_dmg}")


                           player_turn = False
                       else:
                           print("Returning you back to the main scene...")
                   elif player_option_choose == "heal".lower().strip():
                       if self.character.items:
                           self.scene_changes_to("CHOICE SCENE")


                           healing_item, quantity = self.character.inventory.choose_item(include_healing_affect = True), 1




                           if healing_item != 'exit'.lower().strip():
                               print()
                               self.scene_changes_to("HEALING SCENE")


                               self.character.inventory.use_item(healing_item, quantity)
                               player_turn = False
                           else:
                               print("Returning you back to the main scene...")


                       else:
                           print(f"Sorry, it looks like you do not have any items. Choose "
                                 "another option")
                   elif player_option_choose == "throw".lower().strip():
                       arrow = "-->"
                       if self.character.items:
                           while True:
                               self.scene_changes_to("CHOICE SCENE")


                               player_item_choice, quantity = self.character.inventory.choose_item(include_damage_affect = True), 1  # What powers/weapon does the player want to choose?


                               if player_item_choice != 'exit'.lower().strip():


                                   old_quantity = \
                                   self.character.items[player_item_choice][
                                       self.character.quantity_tag]


                                   self.character.items[player_item_choice][
                                       self.character.quantity_tag] -= quantity


                                   new_quantity = \
                                   self.character.items[player_item_choice][
                                       self.character.quantity_tag]




                                   self.scene_changes_to("FIGHTING SCENE")
                                   self.character.display_items()
                                   print(f"Sum of Item '{player_item_choice}': {old_quantity} {arrow} {new_quantity} ")


                                   # OVERALL DAMAGE AFFECT FOR PLAYER
                                   overall_player_dmg = round((player_dmg := round(self.character.items[player_item_choice][self.character.damage_tag] + self.character.damage)) * (player_critical_dmg := self.determine_critical_chance()))  # Use self.character
                                   self._opponent_dmg_taken(character2, overall_player_dmg)




                                   if player_critical_dmg != 1.00:
                                       print("CRITICAL DAMAGE!")
                                       print(f"({player_dmg}) to ({overall_player_dmg}) by {(player_critical_dmg - 1.00) * 100}%")




                                   print(f"You have thrown '{player_item_choice}' with attack_dmg of {overall_player_dmg}")


                                   print()


                                   player_turn = False
                                   break
                               else:
                                   print("Returning you back to the main scene...")
                                   break
                       else:
                           print(f"Sorry, it looks like you do not have any items. Choose "
                                 "another option")


                   elif player_option_choose == "flee".lower().strip():
                       self.scene_changes_to("ESCAPING SCENE")


                       print(f"You have fled from the scene!")
                       input("\n\t->\n")
                       player_turn, fighting = False, False
                       break
                   else:
                       self.scene_changes_to("FIGHTING SCENE")
                       print(f"You have skipped a turn!")
                       player_turn = False
                       continue


               if player_option_choose == "flee".lower().strip(): break






               opponent_turn = not player_turn


               while opponent_turn:
                   print()


                   # OPPONENT ATTACK!
                   if random.randint(a = 1, b = 7) < 10:


                       opponent_power_choice = random.choice(list(character2.character.powers.keys()))  # Use self.character


                       # OVERALL DAMAGE AFFECT FOR OPPONENT
                       overall_opponent_dmg = round((opponent_dmg := round(character2.character.powers[opponent_power_choice][self.character.damage_tag] + character2.character.damage)) * (opponent_critical_dmg := self.determine_critical_chance()))
                       if opponent_critical_dmg != 1.00:
                           print("CRITICAL DAMAGE!")
                           print(f"({opponent_dmg}) to ({overall_opponent_dmg}) by {(opponent_critical_dmg - 1.00) * 100}%")
                       print(f"{character2.character.name} has used '{opponent_power_choice}' with attack_dmg of {overall_opponent_dmg}")  # Use self.character


                       self._player_dmg_taken(overall_opponent_dmg)
                       opponent_turn = False


                   else:
                       # OVERALL HEALTH AFFECT FOR OPPONENT
                       print(f"{character2.character.name} has skipped a turn")  # Healing affect takes place for enemy # Use self.character
                       try: health_ratio = character2.character.bars_num / self.character.bars_num  # Use self.character
                       except ZeroDivisionError: health_ratio = 0


                       damage_impact = self.character.damage * 0.1  # Use self.character
                       opponent_relative_increase = math.ceil(damage_impact * health_ratio)
                       character2.character.bars_num += opponent_relative_increase  # Use self.character


                       if opponent_relative_increase: print(f"{character2.character.name} has gained {opponent_relative_increase} health")


                       opponent_turn = False


                   # Adjusts new health for both characters
                   self.adjust_health(character2, True, True)


                   print()










               after_player_hp, after_opponent_hp = self.character.return_current_health(), character2.character.return_current_health()
               net_player_hp = self.net_health_calc(before_player_hp, after_player_hp)
               net_opponent_hp = self.net_health_calc(before_opponent_hp, after_opponent_hp)




               # use to check if someone gets defeated
               if self.__is_dead(character2, net_player_hp, net_opponent_hp): break  # breaks loop if someone dies when health <= 0
               else: player_turn = not opponent_turn




       else:
           if not (self.character.powers or character2.character.powers): print("Ensure both plays have enough weapons or powers to battle. (At least one weapon/power)")
           else:print("Ensure both players have enough health to battle (health > 0).")