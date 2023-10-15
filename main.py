
import os
import keyboard
import time
import numpy as np

#Class to create a object to represent the player
class Player:
    def __init__(self, life: int, armor: int, attack: int, position: tuple):
        self.life = life
        self.armor = armor
        self.attack = attack
        self.position = position
    
    #Function to move the player across the map
    def move_actions(self, game_map):
        while (True):
            #Moving UP
            if (keyboard.is_pressed('up')):
                new_position = (self.position[0] - 1, self.position[1])
                #print(game_map.is_nothing_unit(new_position))
                if (game_map.is_nothing_unit(new_position)):
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
                #print(game_map.is_nothing_unit(new_position))
                if (game_map.is_nothing_unit(new_position)):
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
                #print(game_map.is_nothing_unit(new_position))
                if (game_map.is_nothing_unit(new_position)):
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
                #print(game_map.is_nothing_unit(new_position))
                if (game_map.is_nothing_unit(new_position)):
                    game_map.units[self.position[0]][self.position[1]].content = ' '
                    game_map.units[self.position[0]][self.position[1]].player_is_in = False
                    self.position = new_position
                    game_map.units[self.position[0]][self.position[1]].content = 'P'
                    game_map.units[self.position[0]][self.position[1]].player_is_in = True
                    self.show_nearby_units(game_map)
                break

    def show_nearby_units(self, game_map):
        start = (self.position[0] - 1, self.position[1] - 1)
        
        for c in range(0, 3):   
            for j in range (0, 3):
                position_to_open = (start[0] + c, start[1] + j)
                game_map.open_unit(position_to_open)

    def set_position(self, position: tuple):
        self.position[0] = position[0]
        self.position[1] = position[1]

#Creating the player 
player = Player(100, 10, 5, (14, 0)) 

#Class to create an map unit
class Map_Unit:
    def __init__(self, content, is_open, is_wall, player_is_in):
        self.content = content
        self.is_open = is_open
        self.is_wall = is_wall
        self.player_is_in = player_is_in


#Class to create an map object
class Map:
    def __init__(self, name, units):
        self.name = name
        self.units = units
    
    #method to fullfil the map with 15x15 matrix with map_units
    def fullfil_map(self):
        for i in range(0, 15):
            map_aux = [] 
            for j in range(0, 15):
                map_aux.append(Map_Unit('X', False, False, False))
            self.units.append(map_aux)

    def place_player(self, player):
        self.units[player.position[0]][player.position[1]].content = 'P'
        self.units[player.position[0]][player.position[1]].player_is_in = True

    #Method to place the walls of the map, using a list of coordinates of the walls
    def place_walls(self, wall_coordinates):
        for coordinate in wall_coordinates:
            self.units[coordinate[0]][coordinate[1]].content = '-'
            self.units[coordinate[0]][coordinate[1]].is_wall = True

    def is_nothing_unit(self, coordinate:tuple):
        if ((coordinate[0] > 14 or coordinate[1] > 14) or (coordinate[0] < 0 or coordinate[1] < 0)):
            return False
        elif (self.units[coordinate[0]][coordinate[1]].is_wall):
            return False
        else:
            return True

    def open_unit(self, position:tuple):
        if ((position[0] > 14 or position[1] > 14) or (position[0] < 0 or position[1] < 0)):
            return False
        else:
            self.units[position[0]][position[1]].is_open = True
            if (self.units[position[0]][position[1]].content == 'X'):
                self.units[position[0]][position[1]].content = ' '
            return True
    
    #Method to show the map in console
    def show_map(self):
        for line in self.units:
            for unit in line:
                if (unit.is_open):
                    print(unit.content + ' ', end='')
                else:
                    print('X ', end='')
            print()

# ----------------FUNCTIONS----------------


# ----------------MAPS----------------

# 1 - Initial Map
map_1 = Map('Initial Map', [])
map_1.fullfil_map()
# Walls
wall_coordinates = [(0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12),
                    (1, 3), (1, 7), (1, 8), (1, 12),
                    (2, 3), (2, 7), (2, 8), (2, 12),
                    (3, 3), (3, 7), (3, 8), (3, 12),
                    (4, 3), (4, 12 ),
                    (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 12),
                    (6, 10), (6, 12),
                    (7, 0), (7, 1), (7, 2), (7, 3),  (7, 4), (7, 5), (7, 6), (7, 7), (7, 10), (7, 12),
                    (8, 7), (8, 8), (8, 9), (8, 10), (8, 12), (8, 13), (8, 14),
                    (9, 2),
                    (10, 2), (10, 3), (10, 4), (10, 7), (10, 8), (10, 9), (10, 10), (10, 12), (10, 13), (10, 14),
                    (11, 2), (11, 4), (11, 7), (11, 10), (11, 12),
                    (12, 1), (12, 2), (12, 4), (12, 5), (12, 6), (12, 7), (12, 10), (12, 12), (12, 13), (12, 14),
                    (13, 1), (13, 10),
                    (14, 1), (14, 10)]
map_1.place_walls(wall_coordinates)
map_1.place_player(player)

# ----------------MAIN LOOP----------------
while (True):
    player.show_nearby_units(map_1)
    map_1.show_map()

    player.move_actions(map_1)
    time.sleep(0.1)
    os.system('cls')

