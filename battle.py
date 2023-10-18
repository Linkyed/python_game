from player import player
from maps_files.maps import MAP_WIDHT
class enemy:
    def __init__(self, name, hp, attack, armor, mana):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.armor = armor
        self.mana = mana

def battle_interface (player, enemy):

     print('=======================================================================')
     print('Player: HP 100/{}    Attack: {}    Armor: {}    Mana: {}'.format(player.hp, player.attack, player.armor, player.mana))
     print('{}: HP {}/{}    Attack: {}    Armor: {}   Mana: {}'.format(enemy.name, enemy.max_hp, enemy.hp, enemy.attack, enemy.armor, enemy.mana))

def combat(player, enemy):
    while (enemy.hp > 0):
        preview_scene_tittle = 'BATTLE AGAINST A ' + enemy.name.strip().upper()
        alighment = ((MAP_WIDHT*2)+1 - len(preview_scene_tittle))//2
        scene_tittle = ''
        for c in range (0, alighment):
            scene_tittle = scene_tittle + ' '
        scene_tittle = scene_tittle + preview_scene_tittle
        print('=======================================================================')

enemy_1 = enemy('Skeleton', 50, 5, 3, 0)

battle_interface(player, enemy_1)