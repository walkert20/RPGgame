import random
import time
import player_unit
import enemy_unit

defeated = []
away =[]

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

def Battle(PlayerTeam, EnemyTeam):
    in_battle = True
    player_turn = False
    i=-1
    j=-1
    
    while in_battle == True:
        enemy_defeated = 0
        if (player_turn == False):
            player_turn = True
            i += 1
        else:
            player_turn = False
            j += 1

        who_is_down(PlayerTeam)
        PlayerTeam = who_is_alive(PlayerTeam)
        EnemyTeam = who_is_alive(EnemyTeam)

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
            while (choice >= 4 or choice < 1):
                print("Invalid choice. Try again.")
                choice = get_selection()
            player.player_turn(EnemyTeam, choice)
        else:
            enemy.enemy_turn(PlayerTeam)

        if not(team_is_alive(PlayerTeam)) or not(team_is_alive(EnemyTeam)):
            in_battle = False
    after_battle(PlayerTeam, EnemyTeam)


def team_is_alive(team):
    allAlive = False
    for teammate in team:
        if(teammate.status != "Down"):
            return True
    return allAlive

def who_is_down(team):
    for teammate in team:
        if(teammate.status == "Down"):
            defeated.append(teammate)

def who_is_alive(team):
    Alive = []
    for teammate in team:
        if (teammate.status != "Down"):
            Alive.append(teammate)
    return Alive

def after_battle(PlayerTeam, EnemyTeam):
    if team_is_alive(PlayerTeam) == False:
        print("Your team has been wiped out! You lose.")
    else:
        print("The enemy team has been defeated! Victory!")
        for player in PlayerTeam:
            player.gain_exp(30)

def mock_battle_1(): # 2v1 attacker.
    tony = player_unit.Player("Tony")
    sara = player_unit.Player("sara")
    john = enemy_unit.Enemy("john", "attacker")
    Battle([sara, tony],[john])

def mock_battle_2(): # 1v1 healer.
    name = input("What is your name? ") 
    player = player_unit.Player(name)
    Tony = enemy_unit.Enemy("tony", "healer")
    Tony.health = 30
    Battle([player], [Tony])

def mock_battle_3(): # 3v3 attacker.
    name = input("What is your name? ")
    player = player_unit.Player(name)
    tony = player_unit.Player("Tony")
    sara = player_unit.Player("sara")
    john = enemy_unit.Enemy("john", "attacker")
    tobi = enemy_unit.Enemy("tobi", "attacker")
    kain = enemy_unit.Enemy("kain", "attacker")
    print(" Oi! Wake up! We got company!")
    print()
    sleep_time = random.randrange(2, 5)
    time.sleep(sleep_time)
    print('''Long story short, a battle has broken out! Work with your
        teammates to fight off the enemies!!!''')
    time.sleep(sleep_time)
    Battle([player, tony, sara], [john, tobi, kain])

def mock_battle_4(): # 2v2, 1 attacker, 1 healer.
    vinny = player_unit.Player("vinny")
    sara = player_unit.Player("sara")
    john = enemy_unit.Enemy("john", "attacker")
    tony = enemy_unit.Enemy("tony", "healer")
    Battle([vinny, sara],[john, tony])

def mock_boss_battle(): # 4v1 boss.
    vinny = player_unit.Player("vinny")
    sara = player_unit.Player("sara")
    pan = player_unit.Player("pan")
    paul = player_unit.Player("paul")
    Bully = enemy_unit.Enemy("bully", "boss")

#mock_battle_1()
#mock_battle_2()
#mock_battle_3()
#mock_battle_4()
