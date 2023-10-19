import random

class Item:
    def __init__(self, id):
        self.id = id
        if (id == 1):
            self.name = 'Healing Potion'
            self.description = 'A magic liquid that can restore your health'
            self.effect = 'Healing'
            self.hp_restored = 50
        elif (id == 2):
            self.name = 'Strenght Potion'
            self.description = 'A magic liquid that can increase your attack power'
            self.effect = 'Attack Buff'
            self.attack_buff = 5
        elif (id == 3):
            self.name = 'Magic Power Potion'
            self.description = 'A magic liquid that can increase your magic power'
            self.effect = 'Magic Buff'
            self.magic_buff = 8

    def create_item():
        item_id = random.randint(1, 3)
        return Item(item_id)
    
    def __str__(self) -> str:
        return self.name

        
        