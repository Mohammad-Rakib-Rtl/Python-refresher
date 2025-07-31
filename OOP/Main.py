from Enemy import *
from Zombie import *
from Ogre import *

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

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        e1.special_attack()
        e2.special_attack()
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

        if e1.health_points > 0:
            print("Enemy 1 wins!")
        else:
            print("Enemy 2 wins!")


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie, ogre)
















