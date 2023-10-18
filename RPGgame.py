import random
import time
import player_unit
import enemy_unit
import items

defeated = []
away = []

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
    # base_team = PlayerTeam
    # base_enemy_team = EnemyTeam
    in_battle = True
    player_turn = False
    i=-1
    j=-1
    
    while in_battle == True:
        #enemy_defeated = 0
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


        print()
        player  = PlayerTeam[i]  #current_turn_player
        enemy = EnemyTeam[j]   #current_enemy_turn_player

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
            player.player_turn(EnemyTeam, PlayerTeam, choice)

        else:
            enemy.enemy_turn(PlayerTeam)

        if not(team_is_alive(PlayerTeam)) or not(team_is_alive(EnemyTeam)):
            in_battle = False
    current_team = after_battle(PlayerTeam, EnemyTeam)
    retry = input("Try again? (y/n) ")
    if retry == "y":
        # both teams recover all health
        Battle(base_team, base_enemy_team)
    else:
        return

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
        return
    else:
        print("The enemy team has been defeated! Victory!")
        for player in PlayerTeam:
            player.gain_exp(30)
        for player in defeated:
            player.health = int(.25*player.MAX_health)
            player.status = "Normal"
            PlayerTeam.append(player)
        return PlayerTeam

def test_adventure():
    name = input("What is your name? ")
    player = player_unit.Player(name)
    tony = player_unit.Player("Tony")
    sara = player_unit.Player("sara")
    pan = player_unit.Player("pan")
    paul = player_unit.Player("paul")
    # 3 fights:
    # 1) 5 v 3
    myTeam = [player, tony, sara, pan, paul]
    john = enemy_unit.Enemy("john", "attacker")
    jimmy = enemy_unit.Enemy("jimmy", "attacker")
    joe = enemy_unit.Enemy("joe", "attacker")
    Battle(myTeam, [john, jimmy, joe])
    # 2) 5 v 4
    soldier_1 = enemy_unit.Enemy("soldier_1", "attacker")
    soldier_2 = enemy_unit.Enemy("soldier_2", "healer")
    soldier_3 = enemy_unit.Enemy("soldier_3", "attacker")
    Battle(myTeam, [soldier_1, soldier_2, soldier_3])
    # 3) 5 v boss
    Bully = enemy_unit.Enemy("bully", "boss")
    Bully.MAX_health = 400
    Bully.health = 400
    Battle(myTeam, [Bully]) 


def mock_battle_1(): # 2v1 attacker.
    tony = player_unit.Player("Tony")
    sara = player_unit.Player("sara")
    john = enemy_unit.Enemy("john (enemy)", "attacker")
    a = ["water", "water", "grenade"]
    for x in a:
        items.store(x)
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
    Bully.MAX_health = 400
    Bully.health = 400
    Battle([vinny, sara, pan, paul], [Bully])

#mock_battle_1()
#mock_battle_2()
#mock_battle_3()
#mock_battle_4()
#mock_boss_battle()
