#! python
import random


def dice(d):
    return random.randint(1, d)


def atributeStatistic():
    min = 99
    sum = 0
    for i in range(4):
        d6 = dice(6)
        sum += d6
        if min > d6:
            d6 = min

    return sum - min


def atributeModifier():
    modifier = int((atributeStatistic - 10)/2)
    return modifier


def characterAtributes():
    atributes = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
    character = {}
    for atribute in atributes:
        character[atribute] = atributeStatistic

    for modifier in atributes:
        character[modifier] = atributeModifier

    return character


def printCharacter(character):
    for attrib, mod in character.keys():
        print('{0}: {1:>2}/t{1:>2}'.format(attrib,
              character[attrib], character[mod]))


if __name__ == '__main__':
    p = characterAtributes
    printCharacter(p)
