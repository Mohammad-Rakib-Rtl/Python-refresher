from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

# zombie = Zombie("Zombie", 10)
# ogre = Ogre(30)

# big_zombie = Enemy("Big zombie", 299, 2938)

# enemy2 = Enemy()
# enemy2.health_points = 200


# ogre.type_of_enemy = "Ogre"
# ogre.attack_damage = 1
# ogre.health_points = 10
 
# print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage}')

# print(enemy.health_points)

# print(ogre.talk())
# print(ogre.walk_forward())
# print(ogre.attack())

# big_zombie.health_points = 10
#
# print(ogre.attack_damage)
# print(big_zombie.attack_damage)
# print(big_zombie.health_points)

# print(ogre.get_health_points()) #### encapsulation show making some instance variable more private

# print(zombie.attack_damage)
# 
# print(zombie.walk_forward())
# print(zombie.get_health_points())
# print(zombie.talk())
# print(zombie.spread_disease())
# 
# print(ogre.attack_damage)
# print(ogre.type_of_enemy)
# print(ogre.talk())
# print(ogre.get_health_points())
# 
# print("----------------------")
# 
# print(f'{zombie.type_of_enemy} has {zombie.get_health_points()} health points and can do attack of {zombie.attack_damage}')
# print(f'{ogre.type_of_enemy} has {ogre.get_health_points()} health points and can do attack of {ogre.attack_damage}')
# zombie.talk()
# ogre.talk()


#### Polymorphism ####

# def battle(e1: Enemy, e2: Enemy):
#     e1.talk()
#     e2.talk()
#
#     while e1.health_points > 0 and e2.health_points > 0:
#         print('------------------')
#         e1.special_attack()
#         e2.special_attack()
#         print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left.')
#         print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left.')
#         e2.attack()
#         e1.health_points -= e2.attack_damage
#         e1.attack()
#         e2.health_points -= e1.attack_damage
#
#     print('--------------')
#
#     if e1.health_points > 0:
#         print(f'{e1.get_type_of_enemy()} wins!')
#     else:
#         print(f'{e2.get_type_of_enemy()} wins!')

## Composition

def hero_battle(hero: Hero, enemy: Enemy):


    while hero.health_points > 0 and enemy.health_points > 0:
        print('------------------')

        enemy.special_attack()

        print(f'Hero: {hero.health_points} HP left.')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left.')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('--------------')

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')





zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
ogrerange_creep = Enemy("Ranger", 10, 2)

hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()

# battle(zombie, ogre)
# print(range_creep.special_attack())
# print(ogre.special_attack())


hero_battle(hero, zombie)













