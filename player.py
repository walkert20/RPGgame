# # Player_class

# class Player():
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.MAX_health = 100
#         self.Atk = 100
#         self.exp = 0
#         self.MAX_exp = 100
#         self.level = 1
#         self.status = "Normal"

#     def calculate_damage(Player, damage, attacker):
#     	Player.health -= damage
#     	print("{0} takes {1} damage from {2}!"
#     		.format(Player.name.capitalize(), damage, attacker.name.capitalize()))
#     	print()
#     	if (0 >= Player.health):
#     		Player.health = 0
#     		Player.status = "Down"
#     		print("{0} has been defeated!".format(Player.name.capitalize()))
#     		print()

#     def LEVEL_UP(Player):
#     	Player.MAX_health += int(.15 * Player.MAX_health)
#     	Player.Atk += 15
#     	Player.exp = 0
#     	Player.MAX_exp += 15
#     	Player.level += 1

#     def calculate_heal(Player, heal_amount):
#     	Player.health += heal_amount
#     	print("{0} recovers {1} health!"
#     		.format(Player.name.capitalize(), heal_amount))
#     	if (Player.health > Player.MAX_health):
#     		Player.health = Player.MAX_health
#     		print("{0} is back at full health!"
#     			.format(Player.name.capitalize()))
#     	print()