import keyboard
from maps_files.maps import MAP_WIDHT
class Player:
    def __init__(self, hp: int, armor: int, attack: int, mana: int, magic_power: float):
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.magic_power = magic_power
        self.mana = mana
        self.position = (0, 0)
        self.attack_choice = 1
        self.reward_choice = 1
    
    #Method to move the player across the map
    def actions(self, game_map):
        while (True):
            #Moving UP
            if (keyboard.is_pressed('up')):
                new_position = (self.position[0] - 1, self.position[1])
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = 'N'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            #Moving DOWN
            if (keyboard.is_pressed('down')):
                new_position = (self.position[0] + 1, self.position[1])
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = 'N'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            #Moving RIGHT
            if (keyboard.is_pressed('right')):
                new_position = (self.position[0], self.position[1] + 1)
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = 'N'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            #Moving LEFT
            if (keyboard.is_pressed('left')):
                new_position = (self.position[0], self.position[1] - 1)
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = 'N'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    game_map.open_unit(new_position, True)
                return 'continue'
            if (keyboard.is_pressed('esc')):
                return 'exit'
            
    def battle_actions(self, normal_attack, mana_attack):
        attack_confirmed = False
        while (True):
            if (keyboard.is_pressed('left')):
                normal_attack, mana_attack = '-->Normal Attack', 'Mana Attack'
                self.attack_choice = 1
                break
            if (keyboard.is_pressed('Right')):
                normal_attack, mana_attack = 'Normal Attack', '-->Mana Attack'
                self.attack_choice = 2
                break
            if (keyboard.is_pressed('enter')):
                if (self.attack_choice == 2 and self.mana > 0):
                    self.mana -=1
                    attack_confirmed = True
                elif (self.attack_choice == 2  and self.mana == 0):
                    attack_confirmed = False
                elif (self.attack_choice == 1):
                    attack_confirmed = True
                break
        return normal_attack, mana_attack, attack_confirmed, self.attack_choice
    
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
                

    #Method to show the player's neraby map units in a renge of a 3x3 square with the player in the center
    def show_unit_info(self, game_map):
        print('Current location info: ' + game_map.units[self.position[0]][self.position[1]].description)
        print('=======================================================================')


    #Method to set the position of the player on the map
    def set_position(self, position: tuple, game_map):
        self.position = position
        game_map.units[position[0]][position[1]].player_is_in = True

    #Method to show all info about the player in the console
    def show_info(self):
        #Creating two string that containt the stats of the player
        bar_1 = '|HP: 100/{}*ATTACK: {}|'.format(self.hp, self.attack)
        bar_2 = '|ARMOR: {}*MANA: {}|'.format(self.armor, self.mana)
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
        print(bar_1 + '\n' + bar_2)
        print('=======================================================================')


player = Player(100, 10, 5, 3, 8) 