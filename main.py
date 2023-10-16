
import os
import time
import classes
import maps

# ----------------FUNCTIONS----------------

#Function to show all the interface of the game, tittle, map grid, player info and maybe some other stuff in the future
def interface(game_map, player):
    #Showing and aligning the title of the map
    name = game_map.name
    alighment = (31 - len(name))//2
    tittle = ''
    for c in range (0, alighment):
        tittle = tittle + ' '
    tittle = tittle + name
    print(tittle)
    #Showing the map
    game_map.show_map()
    #Showing the player info below the map
    player.show_info()


# ----------------MAPS----------------

# 1 - Initial Map
map1 = maps.create_map1()

#Creating the player 
player = classes.Player(100, 10, 5, 3,  (14, 0)) 

# ----------------MAIN LOOP----------------
while (True):
    #Showing the nearby units of the players
    player.show_nearby_units(map1)
    #Showing all the interface in the console
    interface(map1, player)
    #Waiting the player to move
    player.move_actions(map1)
    #Sleep time to prevent duplicated inputs
    time.sleep(0.1)
    #Cleaning the console to show the next frame of the game
    os.system('cls')

