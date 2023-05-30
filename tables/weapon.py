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

    def _init_(self, name, armorProficiency, price, acBonus, dexCap,
               checkPenalty, speedPenalty, strength, bulk, group,
               armorTraits):
        self.name = name
        self.armorProficiency = armorProficiency
        self.price = priceToCopperPiece(price)
        self.acBonus = int(acBonus if acBonus.strip() != '-' else 0)
        self.dexCap = int(dexCap if dexCap.strip() != '-' else 0)
        self.checkPenalty = checkPenalty
        self.speedPenalty = speedPenalty
        self.strength = strength
        self.bulk = bulk
        self.group = group
        self.armorTraits = armorTraits

    def _repr_(self):
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

    def _init_(self):
        ''' loadArmors loads armor.csv to generate diferent kinds of armor '''
        with open(Store.armors.value) as csvfile:
            skipLine = True
            lines = csv.reader(csvfile, delimiter=';')
            for row in lines:
                if skipLine:
                    skipLine = False
                    continue
                armor = Armor(*row)
                self.dictArmors[armor.name] = armor

    def _iter_(self):
        return self.dictArmors._iter_()

    def _getitem_(self, key):
        return self.dictArmors[key]

    def keys(self):
        return self.dictArmors.keys()

    def values(self):
        return self.dictArmors.values()


if _name_ == '_main_':
    dArmor = ArmorTable()

    for key in dArmor:
        print(key)
        print(dArmor[key])

    # print(dArmor.keys())
    # print(dArmor.values())
