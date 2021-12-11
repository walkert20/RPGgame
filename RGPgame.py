import random
import time

print ("Hello")

class Player():
    def __init__(name):
    	name = name
        health = 100
        MAX_health = 100
        Atk = 100
        Def = 90
        exp = 0
        MAx_exp = 100
        role = None

    def calculate_damage(Player, damage, attacker):
    	if (damage > Player.health):
    		Player.health = 0
    		print("{0} has taken {1} damage from {2}. {0} has died!"
    			.format(Player.name.capitalize(), damage, attacker))
    	else:
    		Player.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
            	.format(Player.name.capitalize(), damage_amount, attacker))

    def calculate_heal(Player, target_player, heal_amount):
    	if (heal_amount + target_player.health >= target_player.MAX_health):
    		target_player.health = target_player.MAX_health
    		print("{0} heals {1} back to full health!"
    			.format(Player.name.capitalize, target_player.name.capitalize))
    	else:
    		target_player += heal_amount
    		print("{0} heals {1} for {2}!"
    			.format(Player.name.capitalize, target_player.name.capitalize, heal_amount))

def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("What will you do?: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Please try again.")

def enemy_turn(Player):
	sleep_time = random.randrange(2, 6)
	print("....enemy turn....")
	time.sleep(sleep_time)

	if (Player.role == "medic"): #To make things simple, the medic only heals themselves.
		if (Player.health <=  (.35 x Player.MAX_health)):
			result = random.randint(1,6)
			if (result % 2 == 0):
				return 3
			else:
				return random.randint(1,2)
		else:
			return random.randint(1,2,3)

	elif (Player.role == "attacker"):
		if (Player.health <=  (.40 x Player.MAX_health)):
			result = random.randint(1,6)
			if (result % 2 == 0):
				return 2
			else:
				return random.randint(1,3)
		else:
			return random.randint(1,2,3)

	else:
		result = random.randint(1,10)
		if (result <= 4):
			return 3
		else:
			return 1