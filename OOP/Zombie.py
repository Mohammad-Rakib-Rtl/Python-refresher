from Enemy import *

class Zombie(Enemy):

    def __init__(self, type_of_enemy, health_points):
        super().__init__(type_of_enemy=type_of_enemy,
                         health_points=health_points,
                         attack_damage=50)


    def talk(self):
        print("Grrr grrr wahahohh! Grumbling *")

    def spread_disease(self):
        print("The zombie is trying to spread infection.")