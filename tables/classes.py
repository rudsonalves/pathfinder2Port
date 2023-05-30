import json
from store import Store


class CharClasses:
    name = ''
    description = ''
    primary = []
    secondary = []

    def __init__(self, name, description, primary, secondary) -> None:
        self.name = name
        self.description = description
        self.primary = primary
        self.secondary = secondary

    def __repr__(self) -> str:
        return f'Class: {self.name}\nDescription: {self.description}\n' + \
            f'primary: {self.primary}\nsecondary: {self.secondary}'


class ClassesTable:
    dictClasses = {}

    def __init__(self):
        def fromJson(name, classMap):
            return CharClasses(
                name,
                classMap['description'],
                classMap['primary'],
                classMap['secondary']
            )

        file = open(Store.classes.value)

        data = json.load(file)
        file.close()

        for name in data:
            classMap = data[name]
            newClass = fromJson(name, classMap)
            self.dictClasses[name] = newClass

    def __iter__(self):
        return self.dictClasses.__iter__()

    def __getitem__(self, key):
        return self.dictClasses[key]

    def keys(self):
        return self.dictClasses.keys()

    def values(self):
        return self.dictClasses.values()


if __name__ == '__main__':
    dClasses = ClassesTable()

    # for key in dClasses:
    #     print(dClasses[key])

    print(dClasses.keys())
    print(dClasses.values())
