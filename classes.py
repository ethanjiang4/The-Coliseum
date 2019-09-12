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

# Objects and General Setup

# Class for main player. Records Name, HP, Abilities, Stats, Injuries, Items
class Player:
    name = "NULL"
    hp = 0
    # STATS - all out of 100.
    physique = 0 # damage + physical resist
    technique = 0 # accuracy
    agility = 0 # time to react
    willpower = 0 # magic resist
    intelligence = 0 # chance to find good items + upgrades

    # COLLECTIONS
    # all dictionaries
    abilities = {} # [ability name : uses left]
    injuries = {} # [injury name : turns left]
    # Note items is a dict of dicts
    items = {} # [item : [stat : affect]]
    intimidated = False

    def charSelect(self, charNum):
        # depending on character number, update the values.
        if charNum == '1':
            # Faye selected
            # Base stats
            self.name = "Faye"
            self.maxhp = 70
            self.hp = 70
            self.physique = 35
            self.technique = 85
            self.agility = 50
            self.willpower = 75
            self.intelligence = 50
            self.abilities["Dovetail Strike"] = 4
            self.items["Quicksilver Sword"] = {"agility": 10, "physique": 10}
        elif charNum == '2':
            # Ren selected
            # Base stats
            self.name = "Ren"
            self.maxhp = 90
            self.hp = 90
            self.physique = 45
            self.technique = 60
            self.agility = 25
            self.willpower = 70
            self.intelligence = 45
            self.abilities["Self Heal"] = 3
            self.items["Bloody Mace"] = {"physique": 10}
            self.items["Heavy Armour"] = {"physique": 10, "agility": -5}
        elif charNum == '3':
            # Yuna selected
            # Base stats
            self.name = "Yuna"
            self.maxhp = 50
            self.hp = 50
            self.physique = 20
            self.technique = 70
            self.agility = 20
            self.willpower = 70
            self.intelligence = 70
            self.abilities["Self-Enlightenment"] = 3
            self.abilities["Ice Spike"] = 5
            self.abilities["Flamespitter"] = 4
            self.abilities["Soothing Light"] = 4
            self.items["Chakra Robes"] = {"technique": 20}
        elif charNum == '4':
            # Luke selected
            # Base stats
            self.name = "Luke"
            self.maxhp = 60
            self.hp = 60
            self.physique = 35
            self.technique = 65
            self.agility = 70
            self.willpower = 60
            self.intelligence = 55
            self.abilities["Stun Grenade"] = 2
            self.abilities["Cutthroat"] = 3
            self.items["Poison Dagger"] = {"technique": 15}

    def displayStats(self):
        print(self.name)
        print(self.hp)
    def intimidate(self):
        self.physique -= 5
        self.technique -= 5
        self.agility -= 5
        self.willpower -= 5
    def resolveIntimidate(self):
        self.physique += 5
        self.technique += 5
        self.agility += 5
        self.willpower += 5
# Class for Enemies

class Enemy:
    desc = ""
    name = ""
    maxhp = 0
    hp = 0
    # STATS : BASE 
    physique = 0 # damage + physical resist
    technique = 0 # accuracy
    agility = 0 # time to react
    willpower = 0 # magic resist
    intimidation = 0 # debuff to enemy

    abilities = {}
    injuries = {}
    items = {}

    def initEnemy(self, typeNum, level):
        self.abilities = {}
        self.injuries = {}
        self.items = {}
        # depending on type number, generate the appropriate enemy.
        # 0 - Brute
        if typeNum == 0:
            self.name = "Brute Level " + str(level)
            self.desc = "A musclebound lowlife that does grunt work for the State. Unsavoury, clumsy, but hits like a truck."
            self.maxhp = 100
            self.hp += 100
            self.physique += 75
            self.technique += 25
            self.agility += 30
            self.willpower += 50
            self.intimidation += 45
            # The brute does not have any items.
        elif typeNum == 1:
            self.name = "Shanker Level " + str(level)
            self.desc = "A lithe, slimy man armed with a blade. Faster than he seems."
            self.maxhp = 70
            self.hp += 70
            self.physique += 45
            self.technique += 40
            self.agility += 55
            self.willpower += 30
            self.intimidation += 25
            # The Shanker does not have any items.
        elif typeNum == 2:
            self.name = "Mercenary Level " + str(level)
            self.desc = "A hired sword from a nearby town. Is actually able to wield a blade with some finesse."
            self.maxhp = 90
            self.hp += 90
            self.physique += 60
            self.technique += 60
            self.agility += 45
            self.willpower += 40
            self.intimidation += 30
            # The Merc does not have any items.
        elif typeNum == 3:
            self.name = "Guardian Level " + str(level)
            self.desc = "A burly man working security for the State. His heavyset frame seems difficult to take down."
            self.maxhp = 130
            self.hp += 130
            self.physique += 70
            self.technique += 30
            self.agility += 20
            self.willpower += 40
            self.intimidation += 65
            self.abilities["Enrage"] = 1 # A stat buff
            # The Guardian does not have any items.
        elif typeNum == 4:
            self.name = "Assassin Level " + str(level)
            self.desc = "A lightning quick rogue hired by the State. Difficult to catch and deadly with a blade."
            self.maxhp = 75
            self.hp += 75
            self.physique += 60
            self.technique += 65
            self.agility += 60
            self.willpower += 30
            self.intimidation += 30
            self.abilities["Cutthroat"] = 2 # A fast, low damaging attack that inflicts Bleeding
        elif typeNum == 5:
            self.name = "Mage Level " + str(level)
            self.desc = "A combat sorcerer employed by the State. Can control the elements with deadly results."
            self.maxhp = 50
            self.hp += 50
            self.physique += 35
            self.technique += 80
            self.agility += 35
            self.willpower += 60
            self.intimidation += 40
            self.abilities["Fireball"] = 3
            self.abilities["Acid Spray"] = 3
            self.abilities["Ice Spike"] = 3
        
        # After base stats are created, we boost depending on level.
        boost = (level - 1) * 4
        self.hp += boost
        self.physique += boost
        self.technique += boost
        self.agility += boost
        self.willpower += boost
        self.intimidation += boost

