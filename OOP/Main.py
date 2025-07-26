from Enemy import *

ogre = Enemy()
# enemy2 = Enemy()
# enemy2.health_points = 200
ogre.type_of_enemy = "Ogre"
 
# print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage}')

# print(enemy.health_points)

print(ogre.talk())
print(ogre.walk_forward())
print(ogre.attack())