class Enemy:

    # type_of_enemy: str
    # health_points: int = 10
    # attack_damage: int = 1

    def __init__(self, type_of_enemy, health_points, attack_damage):
        # pass
        # print("create new enemy")
        self.type_of_enemy = type_of_enemy ## we are setting each variable to args value
        self.health_points = health_points
        self.attack_damage = attack_damage



    ### example of abstraction (which hides the functionality like torch switch)
    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared to fight!')
        # return f'I am a {self.type_of_enemy}. Be prepared to fight!'

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you.')
        # return f'{self.type_of_enemy} moves closer to you.'

    def attack(self):
        # return f'{self.type_of_enemy} attacks for {self.attack_damage} damage.'
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage.')


# ogre = Enemy()
# # enemy2 = Enemy()
# # enemy2.health_points = 200
# ogre.type_of_enemy = "Ogre"
# 
# # print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage}')
# 
# # print(enemy.health_points)
# 
# print(ogre.talk())
# print(ogre.walk_forward())
# print(ogre.attack())