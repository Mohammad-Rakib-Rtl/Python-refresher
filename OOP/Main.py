from Enemy import *

ogre = Enemy("Zombie", 1, 299)
big_zombie = Enemy("Big zombie", 299, 2938)

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

big_zombie.health_points = 10

print(ogre.attack_damage)
print(big_zombie.attack_damage)
print(big_zombie.health_points)
