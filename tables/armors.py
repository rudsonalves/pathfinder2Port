''' Este módulo possui tabelas de geração de características dos
perssonagens '''

import csv
from store import Store
from common.functions import priceToCopperPiece


class Armor:
    name = None
    armorProficiency = None
    price = None
    acBonus = None
    dexCap = None
    checkPenalty = None
    speedPenalty = None
    strength = None
    bulk = None
    group = None
    armorTraits = None

    def __init__(self, name, armorProficiency, price, acBonus, dexCap,
                 checkPenalty, speedPenalty, strength, bulk, group,
                 armorTraits):
        self.name = name
        self.armorProficiency = armorProficiency
        self.price = priceToCopperPiece(price)
        self.acBonus = int(acBonus if acBonus.strip() != '-' else '0')
        self.dexCap = int(dexCap if dexCap.strip() != '-' else '0')
        self.checkPenalty = checkPenalty
        self.speedPenalty = speedPenalty
        self.strength = strength
        self.bulk = bulk
        self.group = group
        self.armorTraits = armorTraits

    def __repr__(self):
        return f'{self.name}\n' + \
            f'Armor Prof: {self.armorProficiency}\n' + \
            f'Price: {self.price}\t' + \
            f'AC Bonus: {self.acBonus}\t' + \
            f'Dex Cap: {self.dexCap}\n' + \
            f'Check Penalt: {self.checkPenalty}\t ' + \
            f'Speed Penalt: {self.speedPenalty}\t' + \
            f'Strength: {self.strength}\n' + \
            f'Bulk: {self.bulk}\t' + \
            f'Group: {self.group}\t' + \
            f'Traits: {self.armorTraits}\n'


class ArmorTable:
    ''' ArmorTable is a class meant for generating a class that loads an
    armor table '''
    dictArmors = {}

    def __init__(self) -> None:
        with open(Store.armors.value) as csvfile:
            skipLine = True
            lines = csv.reader(csvfile, delimiter=';')
            for row in lines:
                if skipLine:
                    skipLine = False
                    continue
                armor = Armor(*row)
                self.dictArmors[armor.name] = armor


if __name__ == '__main__':
    armorTable = ArmorTable()

    for armor in armorTable.dictArmors:
        print(armorTable.dictArmors[armor])
