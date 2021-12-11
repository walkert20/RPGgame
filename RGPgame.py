import random
import time

print ("Hello")

class Player():
    def __init__(self, name):
    	self.name = name
        self.health = 100
        self.MAX_health = 100
        self.Atk = 100
        self.Def = 90
        self.exp = 0

    def calculate_damage(self, damage, attacker):
    	if (damage > self.health):
    		self.health = 0
    		print("{0} has taken {1} damage from {2}. {0} has died!"
    			.format(self.name.capitalize(), damage, attacker))
    	else:
    		self.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
            	.format(self.name.capitalize(), damage_amount, attacker))

    def calculate_heal(self, target_player, heal_amount):
    	if (heal_amount + target_player.health >= target_player.MAX_health):
    		target_player.health = target_player.MAX_health
    		print("{0} heals {1} back to ull health!"
    			.format(self.name.capitalize, target_player.name.capitalize))
    	else:
    		target_player += heal_amount
    		print("{0} heals {1} for {2}!"
    			.format(self.name.capitalize, target_player.name.capitalize, heal_amount))


