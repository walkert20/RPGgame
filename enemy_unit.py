# Enemy class
import random
import time

class Enemy():
	def __init__(self, name, role):
		self.name = name
		self.health = 100
		self.MAX_health = 100
		self.Atk = 100
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

	def set_parameters(enemy, health, MAX_health, Atk, level, status):
		enemy.health = health
		enemy.MAX_health = MAX_health
		enemy.Atk = Atk
		enemy.level = level
		self.status = status

	def healer_action(enemy, Heroes):
		result = random.randint(1,6)
		if (enemy.health <= .40*enemy.MAX_health):
			if (result % 3 == 0):
				print("{0} healed themself!".format(enemy.name.capitalize()))
				enemy.calculate_heal(int(random.randrange(.10* enemy.MAX_health, .20* enemy.MAX_health)))
			else:
				damage = random.randrange(enemy.Atk*.11, enemy.Atk*.17)
				hero = random.choice(Heroes)
				hero.calculate_damage(damage, enemy)
		else:
			damage = random.randrange(enemy.Atk*.11, enemy.Atk*.17)
			hero = random.choice(Heroes)
			hero.calculate_damage(damage, enemy)

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
			print("{0} Launched an attack!".format(
				enemy.name.capitalize()))
			damage = random.randrange(enemy.Atk*.22, enemy.Atk*.25)
			hero = random.choice(Heroes)
			hero.calculate_damage(damage, enemy)
		elif (result >5 and result <8):
			damage = int(enemy.Atk*.26)
			hero = random.choice(Heroes)
			print( "{0} launched a powerful attack on {1}!".
				format(enemy.name.capitalize(), hero.name.capitalize()))
			hero.calculate_damage(damage, enemy)
		else:
			damage = random.randrange(enemy.Atk*.20, enemy.Atk*.23)
			print("{0} attacked the whole team!".format(enemy.name.capitalize()))
			for hero in Heroes:
				hero.calculate_damage(damage, enemy)

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