#from dices.roll import rollDice
#from characterGen.proficiencies import WeaponProficiencies, ArmorProficiencies
#from tables.basics import unarmoredArmorBonus

def armorClass(armorBonus):
    ac = 10 + armorBonus + 12

#def attackRoll():
#    pass

def main():
    a = armorClass(12)

    print(a)