# Player Heal - based on Willpower
# Player upgrade skills
import time
import random

def restPhase(player):
    player.injuries = {}
    print("\nYou take a much needed rest. Your injuries have healed.")
    time.sleep(1.5)
    # Health gained = random number from 10 to willpower% of 50.
    maxRegen = (player.willpower / 100) * 50
    health = random.randint(10, int(maxRegen))
    player.hp += health
    if player.hp > player.maxhp:
        player.hp = player.maxhp
    print("You regain some health.")
    time.sleep(1.5)
    # Boost stats, from 0-5.
    boost = random.randint(0, 5)
    player.physique += boost
    boost = random.randint(0, 5)
    player.technique += boost
    boost = random.randint(0, 5)
    player.agility += boost
    boost = random.randint(0, 5)
    player.willpower += boost
    boost = random.randint(0, 5)
    player.intelligence += boost
    print("Your skills have increased!")
    time.sleep(1.5)