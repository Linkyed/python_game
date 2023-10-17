import keyboard

#Class to create a object to represent the player
class Player:
    def __init__(self, hp: int, armor: int, attack: int, mana: int):
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.mana = mana
        self.position = (0, 0)
    
    #Method to move the player across the map
    def move_actions(self, game_map):
        while (True):
            #Moving UP
            if (keyboard.is_pressed('up')):
                new_position = (self.position[0] - 1, self.position[1])
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = ' '
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].content = 'P'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    self.show_nearby_units(game_map)
                break
            #Moving DOWN
            if (keyboard.is_pressed('down')):
                new_position = (self.position[0] + 1, self.position[1])
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = ' '
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].content = 'P'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    self.show_nearby_units(game_map)
                break
            #Moving RIGHT
            if (keyboard.is_pressed('right')):
                new_position = (self.position[0], self.position[1] + 1)
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = ' '
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].content = 'P'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    self.show_nearby_units(game_map)
                break
            #Moving LEFT
            if (keyboard.is_pressed('left')):
                new_position = (self.position[0], self.position[1] - 1)
                if (game_map.is_accessible_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = ' '
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].content = 'P'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    self.show_nearby_units(game_map)
                break

    #Method to show the player's neraby map units in a renge of a 3x3 square with the player in the center
    def show_nearby_units(self, game_map):
        start = (self.position[0] - 1, self.position[1] - 1)
        
        for c in range(0, 3):   
            for j in range (0, 3):
                position_to_open = (start[0] + c, start[1] + j)
                game_map.open_unit(position_to_open)

    #Method to set the position of the player on the map
    def set_position(self, position: tuple):
        self.position = position
    
    #Method to show all info about the player in the console
    def show_info(self):
        #Creating two string that containt the stats of the player
        bar_1 = '|HP: 100/{}*ATTACK: {}|'.format(self.hp, self.attack)
        bar_2 = '|ARMOR: {}*MANA: {}|'.format(self.armor, self.mana)
        #Creating the adjustment of the strings to align with the borders of the map
        adjustment_bar_1 = 31 - (len(bar_1)-1)
        adjustment_bar_2 = 31 - (len(bar_2)-1)
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
        print('===============================')

#Class to create an map unit
class Map_Unit:
    def __init__(self, content, is_open, is_wall, player_is_in):
        self.content = content
        self.is_open = is_open
        self.is_wall = is_wall
        self.player_is_in = player_is_in

    

#Class to create an map object
class Map:
    def __init__(self, name):
        self.name = name
        self.units = []
        for i in range (0, 15):
            self.units.append([])

    #Method to verify if a unit has nothing in there
    def is_accessible_unit(self, coordinate:tuple):
        if ((coordinate[0] > 14 or coordinate[1] > 14) or (coordinate[0] < 0 or coordinate[1] < 0)):
            return False
        elif (self.units[coordinate[0]][coordinate[1]].is_wall):
            return False
        elif (self.units[coordinate[0]][coordinate[1]].content == 'N' or 
              self.units[coordinate[0]][coordinate[1]].content == ' '):
            return True

    #Method to open a unit of the map
    def open_unit(self, position:tuple):
        if ((position[0] > 14 or position[1] > 14) or (position[0] < 0 or position[1] < 0)):
            return False
        else:
            self.units[position[0]][position[1]].is_open = True
            return True
    
    def create_units(self, unit_content:str, line: int):
        unit = None
        if (unit_content.lower().strip() == 'n'):
            unit = Map_Unit(' ', False, False, False)
        elif (unit_content.lower().strip() == '-'):
            unit = Map_Unit('-', False, True, False)
        elif (unit_content.lower().strip() == 'x'):
            unit = Map_Unit('X', False, True, False)
        elif (unit_content.lower().strip() == 'p'):
            unit = Map_Unit('P', True, False, True)    
        self.units[line].append(unit)

    #Method to show the map in console
    def show_map(self):
        print('===============================')
        for line in self.units:
            line_str = ''
            for unit in line:
                if (unit.is_open):
                    line_str = line_str + unit.content + ' '
                else:
                    line_str = line_str + 'X '
            print(' ' + line_str)
        print('===============================')

    def show_map_dev(self):
        print('===============================')
        for line in self.units:
            line_str = ''
            for unit in line:
                line_str = line_str + unit.content + ' '
            print(' ' + line_str)
        print('===============================')