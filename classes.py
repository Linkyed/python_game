import keyboard
from maps_files.maps import MAP_HEIGHT, MAP_WIDHT
#Class to create a object to represent the player
class Player:
    def __init__(self, hp: int, armor: int, attack: int, mana: int):
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.mana = mana
        self.position = (0, 0)
    
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

#Class to create an map unit
class Map_Unit:
    def __init__(self, content, is_open, is_wall, description, player_is_in):
        self.content = content
        self.is_open = is_open
        self.is_wall = is_wall
        self.description = description
        self.player_is_in = player_is_in

    

#Class to create an map object
class Map:
    def __init__(self, name):
        self.name = name
        self.units = []
        for i in range (0, MAP_HEIGHT):
            self.units.append([])

    #Method to verify if a unit has nothing in there
    def is_accessible_unit(self, coordinate:tuple):
        if (self.valid_coordinate(coordinate) == False):
            return False
        elif (self.units[coordinate[0]][coordinate[1]].is_wall):
            return False
        elif (self.units[coordinate[0]][coordinate[1]].content.lower().strip() == 'n'):
            return True

    #Method to open a unit of the map
    def open_unit(self, position:tuple, show_nearby_walls: bool):
        if (self.valid_coordinate(position) == False):
            return False
        else:
            self.units[position[0]][position[1]].is_open = True
            
            if (show_nearby_walls):
                positions_to_open = [(position[0]-1, position[1]), (position[0]+1, position[1]), (position[0], position[1]-1), (position[0], position[1]+1)]
                for next_position in positions_to_open:
                    if (self.valid_coordinate(next_position) and self.units[next_position[0]][next_position[1]].is_wall):
                        self.open_unit(next_position, False)
            return True
    
    def create_units(self, unit_content:str, line: int):
        unit = None
        if (unit_content.lower().strip() == 'n'):
            unit = Map_Unit('N', False, False, 'Nothing to see here', False)
        elif (unit_content.lower().strip() == '-'):
            unit = Map_Unit('-', False, True, "It's a wall", False)
        elif (unit_content.lower().strip() == 'x'):
            unit = Map_Unit('X', False, True, "It's blocked",False) 
        elif (unit_content.lower().strip() == 'p'):
            unit = Map_Unit('N', True, False, 'Nothing to see here', True)
        self.units[line].append(unit)

    #Method to show the map in console
    def show_map(self):
        print('=======================================================================')
        for line in self.units:
            line_str = ''
            for unit in line:
                if (unit.is_open):
                    if (unit.player_is_in):
                        line_str = line_str + 'P' + ' '
                    elif (unit.content.lower().strip() == 'n'):
                        line_str = line_str + ' ' + ' '
                    else:
                        line_str = line_str + unit.content + ' '
                else:
                    line_str = line_str + 'X '
            print(' ' + line_str)
        print('=======================================================================')

    def show_map_dev(self):
        print('=======================================================================')
        for line in self.units:
            line_str = ''
            for unit in line:
                line_str = line_str + unit.content + ' '
            print(' ' + line_str)
        print('=======================================================================')

    def valid_coordinate(self, coordinate: tuple):
        if ((coordinate[0] > 19 or coordinate[1] > 34) or (coordinate[0] < 0 or coordinate[1] < 0)):
            return False
        else:
            return True
