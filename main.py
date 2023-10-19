
import os
import time
import classes
from maps_files import maps
import battle
from player import player
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

# ----------------MAPS----------------

map_being_played = maps.create_map1(player)

loop = 'continue'
# ----------------MAIN LOOP----------------
while (loop != 'exit'):

    #Showing all the interface in the console
    interface(map_being_played, player)
    #Waiting the player to move
    loop = player.actions(map_being_played)
    #Sleep time to prevent duplicated inputs
    time.sleep(0.075)
    while (loop == 'combat'):
        os.system('cls')
        enemy = map_being_played.units[player.position[0]][player.position[1]].enemy
        win = battle.combat(player, enemy, '-->Normal Attack', 'Mana Attack', 'Use Item', '')
        if (win):
            battle.battle_reward(player)
            map_being_played.units[player.position[0]][player.position[1]].content = 'N'
            map_being_played.units[player.position[0]][player.position[1]].is_combat_unit = False
            map_being_played.units[player.position[0]][player.position[1]].description = 'All the creatures are dead, nothing to see here'
            map_being_played.units[player.position[0]][player.position[1]].enemy = None
            player.reset_buffs()
            loop = 'continue'
        else:
            print('GAME OVER')
            time.sleep(1)
            loop = 'exit'
        time.sleep(0.075)
    if (loop == 'item'):
        time.sleep(1)
        map_being_played.units[player.position[0]][player.position[1]].content = 'N'
        map_being_played.units[player.position[0]][player.position[1]].is_item_unit = False
        map_being_played.units[player.position[0]][player.position[1]].description = 'The chest was already open, nothing to see here'
        map_being_played.units[player.position[0]][player.position[1]].item = None
    #Cleaning the console to show the next frame of the game
    os.system('cls')
    
print('Thanks for playing! :)')

