from Enemy import *

enemy = Enemy()
# enemy2 = Enemy()
# enemy2.health_points = 200
enemy.type_of_enemy = "Ogre"
 
print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage}')