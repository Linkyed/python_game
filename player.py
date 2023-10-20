import keyboard
import time
MAP_WIDHT = 35
class Player:
    def __init__(self, hp: int, armor: int, attack: int, mana: int, magic_power: float):
        self.hp = hp
        self.armor = armor
        self.armor_buff = 0
        self.attack = attack
        self.attack_buff = 0
        self.magic_power = magic_power
        self.mana = mana
        self.magic_power_buff = 0
        self.position = (0, 0)
        self.attack_choice = 1
        self.reward_choice = 1
        self.inventory  = {'Slot 1': None}
        self.inventory_full = False
    
    #Method to move the player across the map
    def actions(self, game_map):
        while (True):
            #Moving UP
            if (keyboard.is_pressed('up')):
                new_position = (self.position[0] - 1, self.position[1])
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            #Moving DOWN
            if (keyboard.is_pressed('down')):
                new_position = (self.position[0] + 1, self.position[1])
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            #Moving RIGHT
            if (keyboard.is_pressed('right')):
                new_position = (self.position[0], self.position[1] + 1)
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            #Moving LEFT
            if (keyboard.is_pressed('left')):
                new_position = (self.position[0], self.position[1] - 1)
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            if (keyboard.is_pressed('enter')):
                if (game_map.units[self.position[0]][self.position[1]].is_combat_unit):
                    return 'combat'
                elif (game_map.units[self.position[0]][self.position[1]].is_item_unit):
                    if (self.inventory_full == False):
                        self.inventory_full = True
                        for slot, item in self.inventory.items():
                            if (item == None):
                                self.inventory[slot] = game_map.units[self.position[0]][self.position[1]].item
                                print('Congrats, you recieved a {}!'.format(self.inventory[slot].name))
                                break
                        return 'item'
                    else:
                        print('Your inventory is full! Use a item to get a free space')
                        time.sleep(1)
                        return 'continue'
                elif (game_map.units[self.position[0]][self.position[1]].is_healing_unit):
                    healing_amount = 100 - self.hp
                    self.hp = 100
                    print("Player drinks the water and regenerate {} HP!".format(healing_amount))
                    time.sleep(1)
                    return 'healing'
            if (keyboard.is_pressed('esc')):
                return 'exit'
            
    def battle_actions(self, normal_attack, mana_attack, use_item):
        attack_confirmed = False
        while (True):
            if (keyboard.is_pressed('left')):
                if (self.attack_choice > 1):
                    self.attack_choice -= 1
                if (self.attack_choice == 1):
                    normal_attack = '-->Normal Attack'
                    mana_attack = 'Magic Attack'
                    use_item = 'Use Item'
                elif (self.attack_choice == 2):
                    normal_attack = 'Normal Attack'
                    mana_attack = '-->Magic Attack'
                    use_item = 'Use Item'
                elif (self.attack_choice == 3):
                    normal_attack = 'Normal Attack'
                    mana_attack = 'Magic Attack'
                    use_item = '-->Use Item'
                break
            if (keyboard.is_pressed('right')):
                if (self.attack_choice < 3):
                    self.attack_choice += 1
                if (self.attack_choice == 1):
                    normal_attack = '-->Normal Attack'
                    mana_attack = 'Magic Attack'
                    use_item = 'Use Item'
                elif (self.attack_choice == 2):
                    normal_attack = 'Normal Attack'
                    mana_attack = '-->Magic Attack'
                    use_item = 'Use Item'
                elif (self.attack_choice == 3):
                    normal_attack = 'Normal Attack'
                    mana_attack = 'Magic Attack'
                    use_item = '-->Use Item'
                break
            if (keyboard.is_pressed('enter')):
                if (self.attack_choice == 2 and self.mana > 0):
                    self.mana -=1
                    attack_confirmed = True
                elif (self.attack_choice == 2  and self.mana == 0):
                    attack_confirmed = False
                elif (self.attack_choice == 1):
                    attack_confirmed = True
                elif (self.attack_choice == 3):
                    attack_confirmed = True
                break
           
        return normal_attack, mana_attack, use_item,  attack_confirmed, self.attack_choice
    
    def reward_choice_actions(self):
        reward_confirmed = False
        while (True):
            if (keyboard.is_pressed('left')):
                if (self.reward_choice > 1):
                    self.reward_choice -= 1
                break
            if (keyboard.is_pressed('right')):
                if (self.reward_choice < 4):
                    self.reward_choice += 1
                break
            if (keyboard.is_pressed('enter')):
                reward_confirmed = True
                break
        return reward_confirmed
                
    def item_choice_action (self):
        print()

    #Method to show the player's neraby map units in a renge of a 3x3 square with the player in the center
    def show_unit_info(self, game_map):
        print('Current location info: ' + game_map.units[self.position[0]][self.position[1]].description)
        print('=======================================================================')

    def reset_buffs(self):
        self.armor_buff = 0
        self.attack_buff = 0
        self.magic_power_buff = 0

    #Method to set the position of the player on the map
    def set_position(self, position: tuple, game_map):
        self.position = position
        game_map.units[position[0]][position[1]].player_is_in = True

    #Method to show all info about the player in the console
    def show_info(self):
        #Creating two string that containt the stats of the player
        bar_1 = 'HP: 100/{}*ATTACK: {}'.format(self.hp, self.attack)
        bar_2 = 'ARMOR: {}*MANA: {}'.format(self.armor, self.mana)
        bar_3 = 'Inventoy: Slot 1: {}'.format(self.inventory['Slot 1'])
        #Creating the adjustment of the strings to align with the borders of the map
        adjustment_bar_1 = (2*MAP_WIDHT)+2 - (len(bar_1))
        adjustment_bar_2 = (2*MAP_WIDHT)+2 - (len(bar_2))
        spaces_bar_1 = ''
        spaces_bar_2 = ''
        for c in range (0, adjustment_bar_1):
            spaces_bar_1 = spaces_bar_1 + ' '
        for c in range (0, adjustment_bar_2):
            spaces_bar_2 = spaces_bar_2 + ' '

        bar_1 = bar_1.replace('*', spaces_bar_1)
        bar_2 = bar_2.replace('*', spaces_bar_2)
        #Printing the bars on the console
        print(bar_1 + '\n' + bar_2 + '\n' + bar_3)
        print('=======================================================================')


player = Player(100, 10, 5, 3, 8) 