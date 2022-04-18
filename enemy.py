# # Enemy class

# class Enemy():
#     def __init__(self, name, role):
#         self.name = name
#         self.health = 100
#         self.MAX_health = 100
#         self.Atk = 100
#         self.exp = 0
#         self.MAX_exp = 100
#         self.level = 1
#         self.status = "Normal"
#         self.role = role
    
#     def calculate_damage(enemy, damage, attacker):
#         enemy.health -= damage
#         print("{0} takes {1} damage from {2}!"
#             .format(enemy.name.capitalize(), damage, attacker.name.capitalize()))
#         print()
#         if (0 >= enemy.health):
#             enemy.health = 0
#             enemy.status = "Down"
#             print("{0} has been defeated!".format(enemy.name.capitalize()))
#             print()

#     def calculate_heal(enemy, heal_amount):
#         enemy.health += heal_amount
#         print("{0} recovers {1} health!"
#             .format(enemy.name.capitalize(), heal_amount))
#         if (enemy.health > enemy.MAX_health):
#             enemy.health = enemy.MAX_health
#             print("{0} is back at full health!"
#                 .format(enemy.name.capitalize()))
#         print()

#     def healer_action(enemy):   #To make things simple, the medic only heals themselves.
#         result = random.randint(1,6)
#         if (result % 2 == 0):
#             enemy.calculate_heal(int(random.randrange(.10* enemy.MAX_health, .20* enemy.MAX_health)))
#             return 3
#         else:
#             return random.randint(1,2)

#     def attacker_action(enemy):
#         result = random.randint(1,6)
#         if (result % 2 == 0):
#             return 3                
#         else:
#             return random.randint(1,2)

#     def boss_action():
#         result = random.randint(1,10)
#         if (result <= 4):
#             return 3
#         else:
#             return 1