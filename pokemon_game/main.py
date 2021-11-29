from constants import *
from models import *


# First we have to define the pokemon and its stats

pokemon1 = Pokemon("Charizard", 50, "Fire", "Flying")
pokemon2 = Pokemon("Blastoise", 50, "Water", None)
#We will add a current hp bassed on real combat status and IVs rn it is the same as base HP
pokemon1.current_hp = 78
pokemon2.current_hp = 79

#Stats

pokemon1.stats = {
    HP = 78,
    ATTACK = 84,
    DEFENSE = 78,
    SPATTACK = 109,
    SPEDEFENSE = 85,
    SPEED = 100
}

pokemon2.stats = {
    HP = 79,
    ATTACK = 83,
    DEFENSE = 100,
    SPATTACK = 85,
    SPEDEFENSE = 105,
    SPEED = 78
}


#Attacks

pokemon1.attacks = [Attack("Flamethrower", "Fire", SPECIAL, 15, 90, 100)]
pokemon2.attacks = [Attack("Hydro Pump", "Water", SPECIAL, 5, 110, 80)]


#Start battle

battle = Battle(pokemon1, pokemon2)


def ask_command(pokemon1):
    command = None
    while not command:
        # DO ATTACK -> attack 0
        tmp command = input("What should "+pokemon1+" do?").split(" ")
        if len(tmp_command) == 2
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


while not battle.is_finished():
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        #execute turn
        battle.execute_turn(turn)
        battle.print_current_status()
        




