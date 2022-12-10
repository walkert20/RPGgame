# Player_class
import random

used_item = 0

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

    def calculate_heal(Player, heal_amount):
    	Player.health += heal_amount
    	print("{0} recovers {1} health!"
    		.format(Player.name.capitalize(), heal_amount))
    	if (Player.health > Player.MAX_health):
    		Player.health = Player.MAX_health
    		print("{0} is back at full health!"
    			.format(Player.name.capitalize()))
    	print()

    def gain_exp(Player, exp):
        Player.exp += exp
        print ("{0} gained {1} exp.".format(Player.name.capitalize(), exp))
        if (Player.exp >= Player.MAX_exp):
            Player.LEVEL_UP()

    def LEVEL_UP(Player):
        print("{0} has leveled up!".format(Player.name.capitalize()))
        Player.MAX_health += int(.15 * Player.MAX_health)
        Player.Atk += 15
        Player.exp = 0
        Player.MAX_exp += 15
        Player.level += 1

    def load_player(unit):
        player = Player(unit.name)
        player.health = unit.health
        player.MAX_health = unit.MAX_health
        player.Atk = unit.Atk
        player.exp = unit.exp
        player.MAX_exp = unit.MAX_exp
        player.level = unit.level
        player.status = unit.status
        return player

    def using_item(player, storage, enemies, heroes):
        item_list = []
        for x in storage:
            if x in item_list:
                pass
            else:
                print(storage[storage.index(x)].name + "(" + str(storage.count(x)) + ")")
                item_list.append(x)
                # NOTE: THIS IS SLOW!!! O(n^2) SLOW AT WORST!!!!!! MAKE THIS FASTER LATER ON!!!!!
                # NOTE: A way to make this faster: make a finite list/library and just keep track of how many
                #       of each item the player has. This potentially could make it O(n) at worst.
                #       Example: Potions:2, grenades:3, etc.
                #       This could also give more usevalue from the item class.
                # NOTE: Also, throw this part into the main game.


        print()
        choice = get_item()                   #NOTE: THIS FUNCTION COULD REPLACE THE SAFE_CHOICE FUNTION   
        while (choice > len(storage) or choice < 1):
            print("Invalid choice. Try again.")
            choice = get_item() 

        # safe_choice(choice, item_list)
        item = item_list[choice-1]                #THIS WILL RETURN AN ITEM
        if item.output == "harm":
            enemy_targets(enemies)
            newChoice = get_target()
            while (newChoice > len(heroes) or newChoice < 1):
                print("Invalid choice. Try again.")
                newChoice = get_target()
            #safe_choice(newChoice, enemies)
            damage = item.value
            enemy = enemies[newChoice-1]
            enemy.calculate_damage(damage, player)
            if (enemy.health == 0):
                player.gain_exp(15*enemy.level)

        elif item.output == "heal":
            ally_targets(heroes)
            newChoice = get_target()
            while (newChoice > len(heroes) or newChoice < 1):
                print("Invalid choice. Try again.")
                newChoice = get_target()
            #safe_choice(newChoice, heroes)
            damage = item.value
            hero = heroes[newChoice-1]
            hero.calculate_heal(damage)

        # elif item.output == "buff":

        # elif item.output == "nerf":

    def player_turn(player, storage, enemies, heroes, choice):
        used_item = 0
        if(choice == 1):
            enemy_targets(enemies)
            choice = get_target()
            while (choice > len(enemies) or choice < 1):
                print("Invalid choice. Try again.")
                choice = get_target()
            damage = random.randrange(player.Atk*.18, player.Atk*.25)
            enemy = enemies[choice-1]
            enemy.calculate_damage(damage, player)
            if (enemy.health == 0):
                player.gain_exp(15*enemy.level)

        elif (choice == 2):
            if storage == []:
                print("You don't have any items at the moment. You picked up a rock and threw it at the enemy.")
                enemy = random.choice(enemies)
                enemy.calculate_damage(5, player)
                if (enemy.health == 0):
                    player.gain_exp(15*enemy.level)
            else:
                player.using_item(storage, enemies, heroes)

        elif (choice == 3):
            print( "You charged the enemy team alone!")
            damage = random.randrange(int(player.Atk*.14), int(player.Atk*.20))
            x = random.choice(enemies)
            x.calculate_damage(damage, player)
            y = random.choice(enemies)
            y.calculate_damage(damage, player)
            if (x == y and x.health == 0):
                player.gain_exp(15*x.level)
            else:
                if(x.health == 0):
                    player.gain_exp(15*x.level)
                if(y.health == 0):
                    player.gain_exp(15*y.level)

# def safe_choice(choice, list):
#   while (choice >= len (list) or choice <1):
        #        print("Invalid choice. Try again.")
        #        choice = get_target()
def ally_targets(heroes):
        for x in heroes:
            print(str(heroes.index(x)+1) +") " + x.name + " "+ str(x.health) +
            "/"+ str(x.MAX_health))

def enemy_targets(enemies):
    for x in enemies:
        print(str(enemies.index(x)+1) +") " + x.name + " "+ str(x.health) +
            "/"+ str(x.MAX_health))

def get_target():
	valid_input = False
	while (valid_input is False):
		print()
		choice = input("Who will you target? ")
		if (parse_int(choice) is True):
			return int(choice)
		else:
			print("The input was invalid. Please try again.")

def get_item():
        valid_input = False
        while (valid_input is False):
            print()
            choice = input("What do you have in mind?")
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