import random
import time



class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.MAX_health = 100
        self.Atk = 100
        self.exp = 0
        self.MAX_exp = 100
        self.level = 1
        self.status = "Normal."

    def calculate_damage(Player, damage, attacker):
    	Player.health -= damage
    	print("{0} takes {1} damage from {2}!"
    		.format(Player.name.capitalize(), damage, attacker.name.capitalize()))
    	print()

    	if (0 >= Player.health):
    		Player.health = 0
    		Player.status = "Down."
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
#########      Work on this later     #############
#def use_item(Player, item):   <--within player class

#class item():
#    def __init__(self, name, value):
#        self.name = name
#        self.value = value

class enemy():
    
    def calculate_damage(enemy, damage, attacker):
        enemy.health -= damage
        print("{0} takes {1} damage from {2}!"
            .format(enemy.name.capitalize(), damage, attacker.name.capitalize()))
        print()

        if (0 >= enemy.health):
            enemy.health = 0
            enemy.status = "Down."
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

    class Healer():
        def __init__(self, name, level):
            self.name = name
            self.health = 125
            self.MAX_health = 125
            self.Atk = 80
            self.level = 1
            self.status = "Normal."
            self.role = "Healer"

        def healer_action():
            if (enemy.health <= (.35 * enemy.MAX_health)):
                result = random.randint(1,6)
                if (result % 2 == 0):
                    return 3
                else:
                    return random.randint(1,2)
            else:
                return random.randint(1,2,3)

    class Attacker():
        def __init__(self, name, level):
            self.name = name
            self.health = 100
            self.MAX_health = 100
            self.Atk = 100
            self.level = 1
            self.status = "Normal."
            self.role = "Attacker"   

        def attacker_action():
            if (enemy.health <=  (.40 * enemy.MAX_health)):
                result = random.randint(1,6)
                if (result % 2 == 0):
                    return 2
                else:
                    return random.randint(1,3)
            else:
                return random.randint(1,2,3)

    class Boss():
        def __init__(self, name, level):
            self.name = name
            self.health = 400
            self.MAX_health = 400
            self.Atk = 170
            self.level = 5
            self.status = "Normal."
            self.role = "Boss"

        def boss_action():
            result = random.randint(1,10)
            if (result <= 4):
                return 3
            else:
                return 1

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

def enemy_turn(enemy):
    sleep_time = random.randrange(2, 6)
    print("....enemy turn....")
    time.sleep(sleep_time)
    if (type(enemy) == Healer):     #To make things simple, the medic only heals themselves.
        enemy.healer_action()

    elif (type(enemy) == Attacker):
        enemy.attacker_action()

    else:
        enemy.boss_action()

def Battle(PlayerTeam, EnemyTeam):
    in_battle = True
    player_turn = False
    i=-1
    j=-1
    
    while in_battle:
        if (player_turn == False):
            player_turn = True
            i+=1
        else:
            player_turn = False
            j+=1

        if i >= len(PlayerTeam):
            i=0
        if j >= len(EnemyTeam):
            j=0
        player  = PlayerTeam[i]  #current_turn_player
        enemy = EnemyTeam[j]   #current_enemy_turn_player
        print()

        if (player_turn):
            print("It's {0}'s turn. {1} health remaining."
            .format(player.name, player.health))
            print()
            print("1) Melee attack.")
            print("2) Use item.")
            print("3) Special move!")
            choice = get_selection()
        else:
            choice = enemy_turn(enemy)

        if (choice == 1):
            if player_turn:
                print("Who will you attack?")
                print()
                Enemies = who_is_alive(EnemyTeam)
                for x in Enemies:
                    print(str(Enemies.index(x)+1) +") " + x.name)
                choice = get_selection()
                damage = random.randrange(player.Atk*.18, player.Atk*.25)
                Enemies[choice-1].calculate_damage(damage, player)
            else:
                damage = random.randrange(enemy.Atk*.15, enemy.Atk*.22)
                Hero = random.choice(who_is_alive(PlayerTeam))
                Hero.calculate_damage(damage, enemy)

        if (choice == 2):
            if(player_turn):
                print("We don't have any items right now. Please pick another choice.")
                print("Oh, wait! I found a grenade! That should work.")
                x = random.choice(who_is_alive(EnemyTeam))
                x.calculate_damage(25, player)
            else:
                print("The enemy threw a grenade at your team!")
                for i in who_is_alive(PlayerTeam):
                    i.calculate_damage(random.randrange(0,25), enemy)

        if (choice == 3 ):
            if (player_turn):
                print( "You charged the EnemyTeam alone!")
                damage = random.randrange(player.Atk*.14, player.Atk*.20)
                x = random.choice(who_is_alive(EnemyTeam))
                x.calculate_damage(damage, player)
                y = random.choice(who_is_alive(EnemyTeam))
                y.calculate_damage(damage, player)
            else:
                print("The enemy watches you closely...")
                sleep_time = random.randrange(2, 6)
                time.sleep(sleep_time)
        if not team_is_alive(PlayerTeam):  #| not team_is_alive(EnemyTeams):
            in_battle = False
    after_battle(PlayerTeam, EnemyTeam)


# def start_game():
# 	print("The game has started and the fight is on!")
# 	keep_playing = True
def mock_battle():
    tony = Player("Tony")
    sara = Player("sara")
    john = Player("john")
    Battle([sara, john],[tony])

def team_is_alive(team):
    canStillFight = False
    for teammate in team:
        if (teammate.status != "Down"):
            return True
    return canStillFight

def who_is_alive(team):
    Alive = []
    for teammate in team:
        if (teammate.status != "Down"):
            Alive.append(teammate)
    return Alive

#def get_next_player(team):

def after_battle(PlayerTeam, EnemyTeam):
    if team_is_alive(PlayerTeam) == False:
        print("Your team has been wiped out! You lose.")
    else:
        print("The enemy team has been defeated! Victory!")
