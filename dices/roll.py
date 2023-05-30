import random


def dice(die):
    return random.randint(1, die)


def rollDice(n, die):
    dices = []
    for i in range(n):
        dices.append(dice(die))

    return dices
