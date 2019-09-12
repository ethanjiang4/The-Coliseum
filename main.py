# Medieval Fantasy - You've been sentenced to trial for accusations of heresy. You requested trial by combat.
# Now you need to survive 10 rounds of combat against warriors of the State.
# Death will take you back to the beginning.

# Overview:
# Prologue
# Character Selection
# Combat Begin
# Trial N Prologue
# Combat
# After Combat, upgrades
# Upon Defeat, restart
# Upon Trial 10 completion, fight the Inquisitor (Boss)
# Upon Boss defeat, Victory! Unlock a new character to play.

from classes import *
from combatPhase import *
from restPhase import *

characters = []

characters.append("Faye\n\nA swift warrior from a faraway land. Lower damage with quick strikes and strong technique.\n\nEnter 1 to select.")
characters.append("Ren\n\nA tall knight that served under the State. Heavy damage with self-healing and high HP, somewhat slow.\n\nEnter 2 to select.")
characters.append("Yuna\n\nAn intelligent sorceress from the University. Powerful offensive magic spells, low HP.\n\nEnter 3 to select.")
characters.append("Luke\n\nA thief captured from the slums. Deception abilities coupled with blazing speed, low HP.\n\nEnter 4 to select.")

unlocked = 1
day = 1

while True:
    prologue = "Test Prologue. Press any button to continue."
    print(prologue)
    text = input()

    # display available characters.
    print("Character Selection\n")
    for i in range(0, unlocked):
        print(characters[i])
    text = input()
    while int(text) > unlocked:
        print("Please select a valid character.")
        text = input()
    
    # Create player object, and depending on the character selected, update its stats.
    player = Player()
    player.charSelect(text)
    
    # Maybe add in char specific prologue if needed.
    while player.hp > 0:
        precombat = "You enter the coliseum. It is Day "
        print(precombat + str(day))

        # Combat Phase
            # Battle
            # Items / Upgrades
        survived = combatPhase(player, day) #True or False
        if survived:
            print("The enemy is slain. You live to fight another day.")
            print("Enter anything to continue.")
            text = input()
            if player.intimidated:
                player.resolveIntimidate()
                player.intimidated = False
        else:
            print("You have perished. Enter anything to restart.")
            text = input()
            break
        # Rest Phase
            # Heals
        restPhase(player)
        day += 1