import random
import time

print ("Hello")


items = []


class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.MAX_health = 100
        self.Atk = 100
        self.Def = 90
        self.exp = 0
        self.MAX_exp = 100
        self.level = 1
        self.status = "Normal."

    def calculate_damage(Player, damage, attacker):
    	Player.health -= damage
    	print("{0} takes {1} damage from {2}!"
    		.format(Player.name.capitalize(), damage, attacker))

    	if (0 > Player.health):
    		Player.health = 0
    		Player.status = "Defeated."
    		print("{0} has been defeated!")


#     def calculate_heal(Player, target_player, heal_amount):
#     	if (heal_amount + target_player.health >= target_player.MAX_health):
#     		target_player.health = target_player.MAX_health
#     		print("{0} heals {1} back to full health!"
#     			.format(Player.name.capitalize, target_player.name.capitalize))
#     	else:
#     		target_player += heal_amount
#     		print("{0} heals {1} for {2}!"
#     			.format(Player.name.capitalize, target_player.name.capitalize, heal_amount))

# def parse_int(input):
#     try:
#         int(input)
#         return True
#     except ValueError:
#         return False

# def get_selection():
#     valid_input = False
#     while (valid_input is False):
#         print()
#         choice = input("What will you do?: ")
#         if (parse_int(choice) is True):
#             return int(choice)
#         else:
#             print("The input was invalid. Please try again.")

# def enemy_turn(Player):
# 	sleep_time = random.randrange(2, 6)
# 	print("....enemy turn....")
# 	time.sleep(sleep_time)

# 	if (Player.role == "medic"): #To make things simple, the medic only heals themselves.
# 		if (Player.health <=  (.35 * Player.MAX_health)):
# 			result = random.randint(1,6)
# 			if (result % 2 == 0):
# 				return 3
# 			else:
# 				return random.randint(1,2)
# 		else:
# 			return random.randint(1,2,3)

# 	elif (Player.role == "attacker"):
# 		if (Player.health <=  (.40 * Player.MAX_health)):
# 			result = random.randint(1,6)
# 			if (result % 2 == 0):
# 				return 2
# 			else:
# 				return random.randint(1,3)
# 		else:
# 			return random.randint(1,2,3)

# 	else:
# 		result = random.randint(1,10)
# 		if (result <= 4):
# 			return 3
# 		else:
# 			return 1

# def play_round (player, computer):
# 	game_in_progress = True
# 	current_player = computer

# 	while game_in_progress:
# 		if (current_player == computer):
# 			current_player = player
# 		else:
# 			current_player = computer

# 		print()
# 		print( "Your move. You have {0} health remaining. "
# 			"Your enemy has {1} health remaining. "
# 			.format(player.health, computer.health))
# 		print()

# 		if(current_player == player):
# 			print("Available moves:")
# 			print("1) Basic attack.")
# 			print("2) Use item.")
# 			print("3) Special move!")
# 			choice = get_selection()
# 		else:
# 			choice = enemy_turn(computer)

# 		if (choice == 1):
# 			damage = random.randrange(player.Atk * .18, player.Atk *.25)
# 			if (current_player == player):
# 				computer.calculate_damage(computer, damage, player)
# 			else:
# 				player.calculate_damage(player, damage, computer)

# 		elif (choice == 2):
# 			save()
# 			print()
# 			print("Your progress has been saved!(Only it hasn't...")
# 		elif (choice == 3):
# 			heal = random.randrange(player.Def * .20, player.Def * .30)
# 			target = player
# 			current_player.calculate_heal(player, target, heal)
# 		else:
# 			print ("That wasn't a valid input. Try again.")

# 		if (player.health == 0):
# 			print("Your team has been wiped out! You lose.")
# 		if (computer.health == 0):
# 			print("The enemy team has been defeated! Victory!")


# def start_game():
# 	print("The game has started and the fight is on!")
# 	keep_playing = True

# 	while (keep_playing is True):
# 		print()
# 		play_round()
