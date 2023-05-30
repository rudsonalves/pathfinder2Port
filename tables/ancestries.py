import json
from store import Store


class Ancestries:
    name = ''
    description = ''
    boosts = []
    flaw = []

    def __init__(self, name, description, boosts, flaw):
        self.name = name
        self.description = description
        self.boosts = boosts
        self.flaw = flaw

    def __repr__(self) -> str:
        return f'Ancestry: {self.name}\nDescription: {self.description}\n' + \
            f'Boosts: {self.boosts}\nFlaw: {self.flaw}\n'


class AncestriesTable:
    dictAncestries = {}

    def __init__(self):
        def fromJson(name, ancestryMap):
            return Ancestries(
                name,
                ancestryMap['description'],
                ancestryMap['boosts'],
                ancestryMap['flaw']
            )

        file = open(Store.ancestries.value)

        data = json.load(file)

        file.close()

        for name in data:
            ancestryMap = data[name]
            newAncestry = fromJson(name, ancestryMap)
            self.dictAncestries[name] = newAncestry


if __name__ == '__main__':
    dAncestries = AncestriesTable()

    for key in dAncestries.dictAncestries:
        print(dAncestries.dictAncestries[key])
