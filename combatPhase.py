from classes import *
from timeit import default_timer as timer
import time
import random

# Dict to display health status.
healthStatus = {
    5 : "You are healthy and strong.",
    4 : "You are a little beat up, but can still fight.",
    3 : "You are weary and tired, but can still fight.",
    2 : "You are hurt and stumbling.",
    1 : "You are nearly dead."
}

healthStatusEnemy = {
    5 : "The enemy is healthy and strong.",
    4 : "The enemy is a little beat up, but can still fight.",
    3 : "The enemy is weary and tired, but can still fight.",
    2 : "The enemy is hurt and stumbling.",
    1 : "The enemy is nearly dead."
}

# Dict to obtain injury values 
injuryVals = {
    "Bleeding" : 3,
    "Fractured Skull" : 15,
    "Fractured Ribs" : 10,
    "Blunt Force Trauma" : 5,
    "Fractured Pelvis" : 8,
    "Poison" : 5,
    "Laceration" : 3
}

# Dict for injury lengths
injuryTime = {
    "Bleeding" : 5,
    "Fractured Skull" : 1,
    "Fractured Ribs" : 1,
    "Blunt Force Trauma" : 1,
    "Fractured Pelvis" : 1,
    "Poison" : 3,
    "Laceration" : 3 
}

# Attack Dictionary
attackDict = {
    "1" : "Overhead Strike",
    "2" : "Jab",
    "3" : "Slash",
    "4" : "Kick"
}
attackDictEnemy = {
    "1" : "Above",
    "2" : "Left",
    "3" : "Right",
    "4" : "Below"
}

# Response Dictionary
responseDict = {
    "w" : "1",
    "a" : "2",
    "d" : "3",
    "s" : "4"
}

hitRate = {
    "1" : 35,
    "2" : 80,
    "3" : 65,
    "4" : 50
}

# Hit Rate Dictionary
hitRateEnemy = {
    "1" : 40,
    "2" : 20,
    "3" : 25,
    "4" : 30
}
# Base Damage Dictionary
baseDamage = {
    "1" : 30,
    "2" : 12,
    "3" : 20,
    "4" : 25
}
# Base Injury Dictionary
baseInjury = {
    "1" : 50,
    "2" : 10,
    "3" : 20,
    "4" : 30
}
# Injury Type Dictionary
injuryType = {
    "1" : ["Fractured Skull", "Blunt Force Trauma", "Bleeding", "Laceration"],
    "2" : ["Fractured Ribs", "Blunt Force Trauma", "Bleeding", "Laceration"],
    "3" : ["Fractured Ribs", "Blunt Force Trauma", "Bleeding", "Laceration"],
    "4" : ["Fractured Pelvis", "Blunt Force Trauma", "Bleeding", "Laceration"]
}

# Chars and their abilities
playerAbilities = {
    "Faye" : ["Dovetail Strike"],
    "Ren" : ["Self Heal"],
    "Yuna" : ["Self-Enlightenment", "Ice Spike", "Flamespitter", "Soothing Light"],
    "Luke" : ["Stun Grenade", "Cutthroat"]
}

# playerAttack 
def playerAttack(player, enemy, attack, abilitySelect):
    # Depending on attack type, calculate base hit rate.
    # Add in player's TECHNIQUE and enemy's AGILITY
    # Then use random chance to generate an attack.

    result = []
    if abilitySelect == -1:
        # Formula: average base chance, technique, and agility. Then gen a number to see if it falls within.
        chance = (hitRate[attack] + player.technique + (100 - enemy.agility)) / 3
        print("Chance: " + str(chance))
        select = random.randint(0, 100)
        if select <= chance:
            result.append("Hit")
        else:
            result.append("Miss")
            result.append("None")
            return result
        
        # IF HIT, use player's PHYSIQUE and enemy's PHYSIQUE and random chance to calculate damage.
        # Use random chance to determine injury.
        # Damage formula: Difference between physiques = % dmg modification from base.
        physDiff = enemy.physique - player.physique
        damage = baseDamage[attack] * (1 - (physDiff / 100))
        # Apply damage
        print("Damage: " + str(damage))
        enemy.hp -= damage
        # Injury % formula: Base injury chance + % modification from physDiff
        injuryChance = baseInjury[attack] * (1 - (physDiff / 100))
        print("Injury: " + str(injuryChance))
        select = random.randint(0, 100)
        if select <= injuryChance:
            injurySelect = random.randint(0, 3)
            result.append(injuryType[attack][injurySelect])
            # add injury to enemy.
            enemy.injuries[result[1]] = injuryTime[result[1]]

        else:
            result.append("None")
    else:
        # Ability selected.
        ability = playerAbilities[player.name][abilitySelect]
        print("You used " + ability + "!")
        if ability == "Dovetail Strike":
            # Attack enemy 3 times
            hit = playerAttack(player, enemy, "1", -1)
            time.sleep(1.5)
            if hit[0] == "Hit":
                print("Your overhead strike hit!")
                if hit[1] != "None":
                    time.sleep(1)
                    print("You cause a " + hit[1] + ".")
            else:
                print("Your overhead strike missed.")
            hit = playerAttack(player, enemy, "2", -1)
            time.sleep(1.5)
            if hit[0] == "Hit":
                print("Your jab hit!")
                if hit[1] != "None":
                    time.sleep(1)
                    print("You cause a " + hit[1] + ".")
            else:
                print("Your jab missed.")
            hit = playerAttack(player, enemy, "3", -1)
            time.sleep(1.5)
            if hit[0] == "Hit":
                print("Your slash hit!")
                if hit[1] != "None":
                    time.sleep(1)
                    print("You cause a " + hit[1] + ".")
            else:
                print("Your slash missed.")
            time.sleep(1.5)
            return hit

    # Return: [String "Hit" or "Miss", String Injury or "None"]
    return result

def enemyAttack(player, enemy):
    result = []
    # Select enemy attack:
    attack = str(random.randint(1, 4))
    # Formula: sum hitRate + averaged player agility and 100 - enemy technique
    react = hitRateEnemy[attack] + (player.agility + (100 - enemy.technique)) / 2
    reactSeconds = react / 100
    # print("react seconds: " + str(reactSeconds))
    sleepTime = random.randint(1, 4)
    time.sleep(sleepTime)
    print("Enemy attacks from: " + attackDictEnemy[attack] + "!")
    start = timer()
    response = input()
    end = timer()
    reactTime = end - start
    print('reacttime: ' + str(reactTime))
    if response in responseDict and responseDict[response] == attack and reactTime < reactSeconds:
        result.append("Miss")
        result.append("None")
        return result
    else:
        result.append("Hit")
        # Calculate damage
        physDiff = player.physique - enemy.physique
        damage = baseDamage[attack] * (1 - (physDiff / 100))
        # Apply damage
        player.hp -= damage
        # Apply injuries
        injuryChance = baseInjury[attack] * (1 - (physDiff / 100))
        select = random.randint(0, 100)
        if select <= injuryChance:
            injurySelect = random.randint(0, 3)
            result.append(injuryType[attack][injurySelect])
            # add injury to player.
            player.injuries[result[1]] = injuryTime[result[1]]
        else:
            result.append("None")
    return result
    

# player Player Object
def combatPhase(player, day):
    # depending on the day, we generate an enemy to battle.

    # FOR NOW - always choose enemy 0, 1, or 2.
    typeNum = random.randint(0, 2)

    # Obtain enemy level
    level = random.randint(1, 10)
    if level < 5:
        level = 1
    elif level < 8:
        level = 2
    elif level <= 10:
        level = 3

    # Create enemy
    enemy = Enemy()
    enemy.initEnemy(typeNum, level)

    print("\nYou encounter a "+ enemy.name + ".")
    print(enemy.desc + "\n")
    print("Enter anything to continue.")
    flush = input()

    # Apply intimidation debuff if enemy intimidation is > player's HP.
    if enemy.intimidation > player.hp:
        print("You tremble in sight of the enemy. Your skills have decreased slightly.")
        player.intimidate()
        player.intimidated = True

    # Higher agility goes first.
    playerTurn = False
    if player.agility >= enemy.agility:
        playerTurn = True
    
    while True:
        if playerTurn:
            print("It's your turn.")
            # TESTING
            print("Enemy HP: " + str(enemy.hp))
            # player turn.
            playerTurn = False

            # Process:
                # Display status
                # Resolve injuries
                    # Check for death by injury
                # Option to Attack or Ability
                # If Attack, run calculations
                # If Ability, display abilities and user selects what to do.
            
            if player.hp < 10:
                healthNum = 1
            elif player.hp < 20:
                healthNum = 2
            elif player.hp < 30:
                healthNum = 3
            elif player.hp < 50:
                healthNum = 4
            else:
                healthNum = 5
            print(healthStatus[healthNum])

            # Resolve Injuries
            for name in player.injuries:
                if player.injuries[name] > 0:
                    # Apply damage
                    player.hp -= injuryVals[name]
                    # Reduce turns
                    player.injuries[name] -= 1
                    print("You take damage from your " + name +".")
                    time.sleep(1)
            # Check for death by injury.
            if player.hp <= 0:
                return False
            # boolean to use in case player enters in something invalid.
            actionSelect = True
            while actionSelect:
                # Give player option to attack or use ability.
                print("What do you do?")
                print("Attack - 1")
                print("Ability - 2")
                
                text = input()
                # Attack
                if text == "1":
                    print("Select attack: ")
                    print("Overhead Strike - 1")
                    print("Jab - 2")
                    print("Slash - 3")
                    print("Kick - 4")
                    text = input()
                    if text != "1" and text != "2" and text != "3" and text != "4":
                        print("Enter a valid choice.")
                    else:
                        result = playerAttack(player, enemy, text, -1) # Result: [string "Hit" or "Miss", string Injury or "None"]
                        time.sleep(2)
                        if result[0] == "Hit":
                            print("Successful attack!")
                            if result[1] != "None":
                                print("You caused a " + result[1] + ".")
                        else:
                            print("You missed.")
                        time.sleep(1)
                        actionSelect = False
                elif text == "2":
                    print("Select ability:")
                    count = 0
                    for ability in player.abilities:
                        print(str(count) + ". " + ability + ": " + str(player.abilities[ability]) + " uses left.")
                        count += 1
                    print("Enter b to go back.")
                    abilitySelect = input()
                    if abilitySelect == "b":
                        print("Going back...")
                    elif abilitySelect.isalpha():
                        print("Enter a valid choice.")
                    elif -1 < int(abilitySelect) <= count:
                        ability = playerAbilities[player.name][int(abilitySelect)]
                        if player.abilities[ability] == 0:
                            print("Select a valid ability.")
                        elif abilitySelect != "b":
                            player.abilities[ability] -= 1
                            result = playerAttack(player, enemy, text, int(abilitySelect))
                            actionSelect = False
                    else:
                        print("Select a valid ability.")
                else:
                    print("Enter a valid choice.")

            # Check enemy death
            if enemy.hp <= 0:
                return True


            # TODO ABILITIES

        else:
            # enemy turn.
            print("It's the enemy's turn.")
            playerTurn = True

            if enemy.hp < 10:
                healthNum = 1
            elif enemy.hp < 20:
                healthNum = 2
            elif enemy.hp < 30:
                healthNum = 3
            elif enemy.hp < 50:
                healthNum = 4
            else:
                healthNum = 5
            print(healthStatusEnemy[healthNum])
            time.sleep(2)

            # Resolve Injuries
            for name in enemy.injuries:
                if enemy.injuries[name] > 0:
                    # Apply damage
                    enemy.hp -= injuryVals[name]
                    # Reduce turns
                    enemy.injuries[name] -= 1
                    print("The enemy takes damage from their " + name +".")
                    time.sleep(1)
            time.sleep(1)
            # Check for death by injury.
            if enemy.hp <= 0:
                return True

            # Enemy attack
            result = enemyAttack(player, enemy) # Result: [string "Hit" or "Miss", string Injury or "None"]
            if result[0] == "Hit":
                print("The enemy successfully struck you.")
                if result[1] != "None":
                    print("You are injured with a " + result[1] + ".")
            else:
                print("The enemy missed!")
            
            # Check player death.
            if player.hp <= 0:
                return False
        

