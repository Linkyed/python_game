MAP_WIDHT = 35
MAP_HEIGHT = 20
import time
from battle import add_combat
from items import Item
class Map_Unit:
    def __init__(self, content, is_open, is_wall, description, player_is_in):
        self.content = content
        self.is_open = is_open
        self.is_wall = is_wall
        self.description = description
        self.player_is_in = player_is_in
        self.is_combat_unit = False
        self.enemy = None
        self.is_item_unit = False
        self.item = None
        self.is_runic_unit = False
        self.is_healing_unit = False
        self.is_boss_unit = False
    def add_combat(self, combat_level):
        self.is_combat_unit = True
        self.enemy = add_combat(1)
        if (self.is_boss_unit):
            self.enemy = add_combat(2)
    def add_item(self):
        self.is_item_unit = True
        self.item = Item.create_item()
    

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
        elif (self.units[coordinate[0]][coordinate[1]].content.lower().strip() == 'x'):
            return False
        else:
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
        elif (unit_content.lower().strip() == 'b'):
            unit = Map_Unit('B', False, False, 'There is some creatures, press *ENTER* to fight them', False)
            unit.add_combat(1)
        elif (unit_content.lower().strip() == 'i'):
            unit = Map_Unit('I', False, False, 'There is chest here, press *ENTER* to open it', False)
            unit.add_item()
        elif (unit_content.lower().strip() == 'h'):
            unit = Map_Unit('H', False, False, 'There is beautiful water fountain here, press *ENTER* to drink it', False)
            unit.is_healing_unit = True
        elif (unit_content.lower().strip() == 's'):
            unit = Map_Unit('S', False, False, 'There is a really big creature, press *ENTER* to fight it', False)
            unit.is_boss_unit = True
            unit.add_combat(1)
            
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

def load_grid_map(filename: str):
    path = 'maps_files\-'.replace('-', '')

    with open(path + filename + '.txt') as map_file:
        line_counter = 0
        column_counter = 0
        map_grid = map_file.read().replace('	', '')
        for line in map_grid.split('\n'):
            for character in line:
                if (character.lower().strip() == 'p'):
                    player_position = (line_counter, column_counter)
                column_counter += 1
            column_counter = 0
            line_counter += 1
        map_grid = map_grid.replace('\n', '')
    return map_grid, player_position

def generate_map_grid(map_object, map_grid: str):
    accumulate = 0
    for i in range(0, MAP_HEIGHT):
        for j in range (0, MAP_WIDHT):
            map_object.create_units(map_grid[accumulate], i)
            accumulate += 1
    
def load_map():
    map_counter += 1
    

# ----------------Map 1: The Beginning---------------- #
def create_map1(player):
    #Instantiating the Map 1 Object
    map_1 = Map('Map 1: The Beginning')
    #Fullfiling it with only 'nothing' map units
    map_1_grid, player_position = load_grid_map('map1')
    #Coordinates of all walls and placing them on the map
    generate_map_grid(map_1, map_1_grid)

    player.set_position(player_position, map_1)


    return map_1

def create_map2(player):
    #Instantiating the Map 1 Object
    map_2 = Map('Map 2: The Soliman Labyrinth')
    #Fullfiling it with only 'nothing' map units
    map_2_grid, player_position = load_grid_map('map2')

    player.set_position(player_position)
    #Coordinates of all walls and placing them on the map
    generate_map_grid(map_2, map_2_grid)


    return map_2