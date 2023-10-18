
import os
import time
import classes
from maps_files import maps
import tkinter

# ----------------FUNCTIONS----------------

#Function to show all the interface of the game, tittle, map grid, player info and maybe some other stuff in the future
def interface(game_map, player):
    #Showing and aligning the title of the map
    name = game_map.name
    alighment = ((maps.MAP_WIDHT*2)+1 - len(name))//2
    tittle = ''
    for c in range (0, alighment):
        tittle = tittle + ' '
    tittle = tittle + name
    print(tittle)
    #Showing the map
    game_map.show_map()
    #Showing the player info below the map
    player.show_info()
    player.show_unit_info(game_map)

#Creating the player 
player = classes.Player(100, 10, 5, 3) 

# ----------------MAPS----------------

map_being_played = maps.create_map1(player)

loop = 'continue'
# ----------------MAIN LOOP----------------
while (loop == 'continue'):
    #Showing the nearby units of the players
    #player.show_nearby_units(map_being_played)
    #Showing all the interface in the console
    interface(map_being_played, player)
    #Waiting the player to move
    loop = player.actions(map_being_played)
    #Sleep time to prevent duplicated inputs
    time.sleep(0.075)
    #Cleaning the console to show the next frame of the game

    os.system('cls')
    
print('Thanks for playing! :)')

