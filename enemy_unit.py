# Enemy class
import random
import time

class Enemy():
    def __init__(self, name, role):
        self.name = name
        self.health = 100
        self.MAX_health = 100
        self.Atk = 100
        self.exp = 0
        self.MAX_exp = 100
        self.level = 1
        self.status = "Normal"
        self.role = role
    
    def calculate_damage(enemy, damage, attacker):
        enemy.health -= damage
        print("{0} takes {1} damage from {2}!"
            .format(enemy.name.capitalize(), damage, attacker.name.capitalize()))
        print()
        if (0 >= enemy.health):
            enemy.health = 0
            enemy.status = "Down"
            print("{0} has been defeated!".format(enemy.name.capitalize()))
            print()

    def calculate_heal(enemy, heal_amount):
        enemy.health += heal_amount
        print("{0} recovers {1} health!"
            .format(enemy.name.capitalize(), heal_amount))
        if (enemy.health > enemy.MAX_health):
            enemy.health = enemy.MAX_health
            print("{0} is back at full health!"
                .format(enemy.name.capitalize()))
        print()

    def healer_action(enemy, Heroes):   #To make things simple, the medic only heals themselves.
        result = random.randint(1,6)
        if (result % 3 == 0):
            enemy.calculate_heal(int(random.randrange(.10* enemy.MAX_health, .20* enemy.MAX_health)))
            return 3
        else:
            return random.randint(1,2)

    def attacker_action(enemy,Heroes):
        result = random.randint(1,10)
        if (result % 3 == 0):
        	print("The enemy threw a grenade at your team!")
        	for hero in Heroes:
        		hero.calculate_damage(random.randrange(0,20), enemy)
        else:
            choice = random.randint(1,2)
            if (choice == 1):
            	damage = random.randrange(enemy.Atk*.15, enemy.Atk*.22)
            	hero = random.choice(Heroes)
            	hero.calculate_damage(damage, enemy)
            else:
            	damage = random.randrange(enemy.Atk*.20, enemy.Atk*.30)
            	hero = random.choice(Heroes)
            	print( "{0} launched a powerful attack on {1}!".
            		format(enemy.name.capitalize(), hero.name.capitalize()))
            	hero.calculate_damage(damage, enemy)

    def boss_action(enemy, Heroes):
        result = random.randint(1,10)
        if (result <= 4):
            return 3
        else:
            return 1

    def enemy_turn(enemy, Heroes):
    	sleep_time = random.randrange(2, 5)
    	print("....enemy turn....")
    	time.sleep(sleep_time)
    	if (enemy.role == "healer"):
    		return enemy.healer_action(Heroes)
    	elif (enemy.role == "attacker"):
    		return enemy.attacker_action(Heroes)
    	else:
    		return enemy.boss_action(Heroes)