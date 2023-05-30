from dices.roll import rollDice


def atributeStatistic():
    dices = rollDice(4, 6)

    return sum(dices) - min(dices)


def atributeModifier(atribute):
    return int((atribute - 10)/2)


def generateAtribute():
    atribute = atributeStatistic()
    modifier = atributeModifier(atribute)

    return atribute, modifier
