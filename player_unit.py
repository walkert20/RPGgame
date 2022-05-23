# Player_class
import random

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.MAX_health = 100
        self.Atk = 100
        self.exp = 0
        self.MAX_exp = 100
        self.level = 1
        self.status = "Normal"

    def calculate_damage(Player, damage, attacker):
    	Player.health -= damage
    	print("{0} takes {1} damage from {2}!"
    		.format(Player.name.capitalize(), damage, attacker.name.capitalize()))
    	print()
    	if (0 >= Player.health):
    		Player.health = 0
    		Player.status = "Down"
    		print("{0} has been defeated!".format(Player.name.capitalize()))
    		print()

    def LEVEL_UP(Player):
    	Player.MAX_health += int(.15 * Player.MAX_health)
    	Player.Atk += 15
    	Player.exp = 0
    	Player.MAX_exp += 15
    	Player.level += 1

    def calculate_heal(Player, heal_amount):
    	Player.health += heal_amount
    	print("{0} recovers {1} health!"
    		.format(Player.name.capitalize(), heal_amount))
    	if (Player.health > Player.MAX_health):
    		Player.health = Player.MAX_health
    		print("{0} is back at full health!"
    			.format(Player.name.capitalize()))
    	print()

    def player_turn(player, Enemies, choice):
    	if(choice == 1):
    		for x in Enemies:
    			print(str(Enemies.index(x)+1) +") " + x.name + " "+ str(x.health) +
    				"/"+ str(x.MAX_health))
    		choice = get_target()
    		damage = random.randrange(player.Atk*.18, player.Atk*.25)
    		Enemies[choice-1].calculate_damage(damage, player)

    	elif (choice == 2):
    		print("We don't have any items right now. Please pick another choice.")
    		print("Oh, wait! I found a grenade! That should work.")
    		for enemy in Enemies:
    			enemy.calculate_damage(20, player)

    	elif (choice == 3):
    		print( "You charged the enemy team alone!")
    		damage = random.randrange(int(player.Atk*.14), int(player.Atk*.20))
    		x = random.choice(Enemies)
    		x.calculate_damage(damage, player)
    		y = random.choice(Enemies)
    		y.calculate_damage(damage, player)

    	else:
    		print("The input was invalid. Please try again next time.")

def get_target():
	valid_input = False
	while (valid_input is False):
		print()
		choice = input("Who will you target? ")
		if (parse_int(choice) is True):
			return int(choice)
		else:
			print("The input was invalid. Please try again.")

def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
