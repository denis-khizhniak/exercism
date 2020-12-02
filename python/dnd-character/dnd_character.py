import random
from math import floor


def modifier(ability):
    return floor((ability - 10) / 2)


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.constitution_modifier = modifier(self.constitution)
        self.hitpoints = 10 + self.constitution_modifier

    def roll_dice(self):
        random.seed()
        return random.choice(range(1, 7))

    def roll4dices(self):
        return [self.roll_dice() for i in range(4)]

    def ability(self):
        return sum(sorted(dice for dice in self.roll4dices())[1:])
