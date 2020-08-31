import random

attack_dict = dict(Punch={'Damage': 35, 'Chance': 2, 'Variable': 5},
                   Kick={'Damage': 40, 'Chance': 4, 'Variable': 7},
                   Uppercut={'Damage': 55, 'Chance': 5, 'Variable': 10},
                   Headbutt={'Damage': 50, 'Chance': 5, 'Variable': 10},
                   Taunt={'Damage': 10, 'Chance': 1, 'Variable': 8})


fighter_dict = dict(Player={'Name': "", 'Health': 100},
                    Opponent={'Name': "Trev", 'Health': 100})


# Dice, random number between low and high
def dice(low, high):
    return int(random.randint(low, high))


# Returns a random attack using Dice and dictionary length
def attack_type():
    global current_attack
    current_attack = list(attack_dict.keys())[dice(0, (len(attack_dict.keys())-1))]


# given an attack this will return the damage with the variable as a dice roll minus to positive
def attack_damage(attack):
    global current_damage
    current_damage = \
        (attack_dict[attack]["Damage"]+dice(-attack_dict[attack]["Variable"], attack_dict[attack]["Variable"]))


# rolls a dice to see if it is higher than the attack chance in the attack_dict
def attack_chance(attack):
    global attack_success
    if dice(1, 6) >= (attack_dict[attack]["Chance"]):
        attack_success = "True"
    else:
        attack_success = "False"


# This looks messy, but it's mainly the print statements that are ugly.
def attacking(attack, current_fighter, current_target):
    attack_chance(attack)
    if attack_success == "True":
        attack_damage(attack)
        fighter_dict[current_target]["Health"] -= current_damage
        if fighter_dict[current_target]["Health"] <= 0:
            print(fighter_dict[current_fighter]["Name"] + " " + attack + "ed "
                  + fighter_dict[current_target]["Name"] + " for " + str(current_damage)
                  + " and knocked them out!")
        else:
            print(fighter_dict[current_fighter]["Name"] + " " + attack + "ed "
                  + fighter_dict[current_target]["Name"] + " for " + str(current_damage)
                  + " and " + fighter_dict[current_target]["Name"] + " has "
                  + str(fighter_dict[current_target]["Health"]) + " health left.")
    else:
        print(fighter_dict[current_fighter]["Name"] + " attempted to " + attack + " "
              + fighter_dict[current_target]["Name"] + " but missed!")


def attack_try():
    try:
        attacking(input("Punch or Kick? ").capitalize(), "Player", "Opponent")
    except:
        print("That isn't an attack, try again.")
        attack_try()


current_attack = ""
current_damage = 0
attack_success = ""


fighter_dict["Player"]["Name"] = input("Name your fighter! ").capitalize()
print("Okay " + fighter_dict["Player"]["Name"] + " you\'re facing " + fighter_dict["Opponent"]["Name"])

while fighter_dict["Player"]["Health"] > 0:
    attack_try()
    if fighter_dict["Opponent"]["Health"] <= 0:
        print("You win!")
        break
    else:
        attack_type()
        attacking(current_attack, "Opponent", "Player")

print("Game Over!")
