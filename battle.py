from player import player
MAP_WIDHT = 35
import math
import os
import time
import random
class enemy:
    def __init__(self, name, hp, attack, armor, mana):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.armor = armor
        self.mana = mana

def add_combat(dificult_level):
    enemy_names = ['Skeleton', 'Goblin', 'Bandit']
    if (dificult_level == 1):
        hp = random.randint(20, 35)
        attack = 0
        armor = 0
        name_choice = random.randint(0, 2)
        if (hp >=50):
            attack = random.randint(5, 10)
            if (attack >= 8):
                armor = random.randint(2, 4)
            else:
                armor = random.randint(5, 8)
        else:
            attack = random.randint(10, 15)
            if (attack >= 13):
                armor = random.randint(1, 3)
            else:
                armor = random.randint(2, 5)
        return enemy(enemy_names[name_choice], hp, attack, armor, 0)

def normal_damage_calculator(attack, armor):
    range_of_attack_variance = (attack*1.40 - attack*0.8)//2
    rng = random.randint(-range_of_attack_variance, range_of_attack_variance)
    damage = int(round((attack + rng)*(1.0 - math.log2(armor)/10)))
    is_critical = False
    if (random.randint(1, 20) == 1):
        damage = 2*damage
        is_critical = True
    return damage, is_critical


def magic_damage_calculator(attack, armor):
    range_of_attack_variance = (attack*1.80 - attack*0.8)//2
    rng = random.randint(-range_of_attack_variance, range_of_attack_variance)
    damage = int(round((attack + rng)*(1.0 - math.log2(armor)/10)))
    is_critical = False
    if (random.randint(1, 20) == 1):
        damage = math.floor(2.25*damage + 1)
        is_critical = True
    return damage, is_critical
    

normal_attack = '-->Normal Attack'
mana_attack = 'Mana Attack'
attack_choise = 'Normal Attack'

def combat(player, enemy, n_attack, m_attack, combat_log):
    player_win = False
    while (enemy.hp > 0 and player.hp > 0):
        preview_scene_tittle = 'BATTLE AGAINST A ' + enemy.name.strip().upper()
        alighment = ((MAP_WIDHT*2)+1 - len(preview_scene_tittle))//2
        scene_tittle = ''
        for c in range (0, alighment):
            scene_tittle = scene_tittle + ' '
        scene_tittle = scene_tittle + preview_scene_tittle
        print('=======================================================================')
        print('Player: HP 100/{}    Attack: {}    Armor: {}    Mana: {}'.format(player.hp, player.attack, player.armor, player.mana))
        print('{}: HP {}/{}    Attack: {}    Armor: {}   Mana: {}'.format(enemy.name, enemy.max_hp, enemy.hp, enemy.attack, enemy.armor, enemy.mana))
        print('=======================================================================')
        print('Combat Log: ')
        print(combat_log)
        print('=======================================================================')
        print('Choose your attack: {}                   {}'.format(n_attack, m_attack))
        print('=======================================================================')
        n_attack, m_attack, confirmed_attack, current_choice = player.battle_actions(n_attack, m_attack)
        if (confirmed_attack):
            if (current_choice == 1):
                damage, critical = normal_damage_calculator(player.attack, enemy.armor)
                enemy.hp -= damage
                if (critical):
                    combat_log = combat_log + ':Player: hit a Critical Hit! Causing *{}* attack damage to the :{}:\n'.format(damage, enemy.name)
                else:
                    combat_log = combat_log + ':Player: deals *{}* attack damage to the :{}:\n'.format(damage, enemy.name)
            elif (current_choice == 2):
                damage, critical = magic_damage_calculator(player.magic_power, enemy.armor)
                enemy.hp -= damage
                if (critical):
                    combat_log = combat_log + ':Player: hit a Critical Hit! Causing *{}* magic damage to the :{}:\n'.format(damage, enemy.name)
                else:
                    combat_log = combat_log + ':Player: deals *{}* magic damage to the :{}:\n'.format(damage, enemy.name)
            if (enemy.hp > 0):
                damage, critical = normal_damage_calculator(enemy.attack, player.armor)
                player.hp -= damage
                if (critical):
                    combat_log = combat_log + ':{}: hit a Critical Hit! causing *{}* attack damage to the :Player:\n'.format(enemy.name, damage)
                else:
                    combat_log = combat_log + ':{}: deals *{}* attack damage to the :Player:\n'.format(enemy.name, damage)
                if (player.hp <= 0):
                    combat_log = combat_log + ':Player: died, good bye...'
                    player_win = False
                    
            else:
                combat_log = combat_log + ':{}: has been defeated, congratulations!'.format(enemy.name)
                player_win = True    

        time.sleep(0.1)
        os.system('cls')
    
    print('=======================================================================')
    print('Player: HP 100/{}    Attack: {}    Armor: {}    Mana: {}'.format(player.hp, player.attack, player.armor, player.mana))
    print('{}: HP {}/{}    Attack: {}    Armor: {}   Mana: {}'.format(enemy.name, enemy.max_hp, enemy.hp, enemy.attack, enemy.armor, enemy.mana))
    print('=======================================================================')
    print('Combat Log: ')
    print(combat_log)
    print('=======================================================================')

    time.sleep(3)
    os.system('cls')
    return player_win
    

choices = ['-->+2 Attack', '+1 Armor', '+1 Mana', '+2 Magic Power']
def battle_reward(player):
    confirmation = False
    while(confirmation == False):
        preview_scene_tittle = 'CHOOSE YOUR REWARD'
        alighment = ((MAP_WIDHT*2)+1 - len(preview_scene_tittle))//2
        scene_tittle = ''
        for c in range (0, alighment):
            scene_tittle = scene_tittle + ' '
        scene_tittle = scene_tittle + preview_scene_tittle
        print(scene_tittle)
        print('=======================================================================')
        print(choices[0], choices[1], choices[2], choices[3])
        confirmation = player.reward_choice_actions()
        if (player.reward_choice == 1):
            choices[0] = '-->+2 Attack'
            choices[1] = '+1 Armor'
            choices[2] = '+1 Mana'
            choices[3] = '+2 Magic Power'
        elif (player.reward_choice == 2):
            choices[0] = '+2 Attack'
            choices[1] = '-->+1 Armor'
            choices[2] = '+1 Mana'
            choices[3] = '+2 Magic Power'
        elif (player.reward_choice == 3):
            choices[0] = '+2 Attack'
            choices[1] = '+1 Armor'
            choices[2] = '-->+1 Mana'
            choices[3] = '+2 Magic Power'
        elif (player.reward_choice == 4):
            choices[0] = '+2 Attack'
            choices[1] = '+1 Armor'
            choices[2] = '+1 Mana'
            choices[3] = '-->+2 Magic Power'
            
        if (confirmation):
            if (player.reward_choice == 1):
                player.attack += 2
                print('Now the player has {} Attack!'.format(player.attack))
            elif (player.reward_choice == 2):
                player.armor += 1
                print('Now the player has {} Armor!'.format(player.armor))
            elif (player.reward_choice == 3):
                player.mana += 1
                print('Now the player has {} Mana!'.format(player.mana))
            elif (player.reward_choice == 4):
                player.magic_power += 2
                print('Now the player has {} Magic Power!'.format(player.magic_power))
            time.sleep(3)
        time.sleep(0.1)
        os.system('cls')






