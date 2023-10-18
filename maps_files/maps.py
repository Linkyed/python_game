import classes
import time
MAP_WIDHT = 35
MAP_HEIGHT = 20

map_counter = 0
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
    map_1 = classes.Map('Map 1: The Beginning')
    #Fullfiling it with only 'nothing' map units
    map_1_grid, player_position = load_grid_map('map1')
    #Coordinates of all walls and placing them on the map
    generate_map_grid(map_1, map_1_grid)
    
    player.set_position(player_position, map_1)


    return map_1

def create_map2(player):
    #Instantiating the Map 1 Object
    map_2 = classes.Map('Map 2: The Soliman Labyrinth')
    #Fullfiling it with only 'nothing' map units
    map_2_grid, player_position = load_grid_map('map2')

    player.set_position(player_position)
    #Coordinates of all walls and placing them on the map
    generate_map_grid(map_2, map_2_grid)


    return map_2