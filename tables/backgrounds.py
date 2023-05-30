import json
from store import Store


class Backgrounds:
    name = ''
    description = ''
    boosts = []
    trained = []
    feat = []

    def __init__(self, name, description, boosts, trained, feat):
        self.name = name
        self.description = description
        self.boosts = boosts
        self.trained = trained
        self.feat = feat

    def __repr__(self) -> str:
        return f'Class: {self.name}\nDescription: {self.description}\n' + \
            f'Boosts: {self.boosts}\nTrained: {self.trained}\n' + \
            f'Feat: {self.feat}\n'


class BackgroundsTable:
    dictBackbgrounds = {}

    def __init__(self):
        def fromJson(name, backgroundMap):
            return Backgrounds(
                name,
                backgroundMap['description'],
                backgroundMap['boosts'],
                backgroundMap['trained'],
                backgroundMap['feat']
            )

        file = open(Store.background.value)

        data = json.load(file)
        file.close()

        for name in data:
            backgroundMap = data[name]
            newBackground = fromJson(name, backgroundMap)
            self.dictBackbgrounds[name] = newBackground


if __name__ == '__main__':
    dBackground = BackgroundsTable()

    for key in dBackground.dictBackbgrounds:
        print(dBackground.dictBackbgrounds[key])
