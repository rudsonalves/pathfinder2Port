profBonusByRank = {
    'untrained': 0,
    'trained': 2,
    'expert': 4,
    'master': 6,
    'legendary': 8
}


class Proficiency:
    name: None
    rank = None
    _level = None

    def __init__(self, level=1, rank='untrained'):
        self.rank = rank
        self._level = level

    def get_bonus(self):
        if self.rank != 'untrained':
            return profBonusByRank[self.rank] + self.level

        return 0

    profBonus = property(get_bonus)

    def set_level(self, level):
        self._level = level

    def get_level(self):
        return self._level

    level = property(set_level, get_level)


class WeaponProficiencies:
    unarmed = None
    simpleWeapons = None
    uncommonSimpleWeapons = None
    martialWeapons = None
    uncommonMartialWeapons = None

    def __init__(self,
                 unarmed='untrained',
                 simpleWeapons='untrained',
                 uncommonSimpleWeapons='untrained',
                 martialWeapons='untrained',
                 uncommonMartialWeapons='untrained'):
        self.unarmed = unarmed
        self.simpleWeapons = simpleWeapons
        self.uncommonSimpleWeapons = uncommonSimpleWeapons
        self.martialWeapons = martialWeapons
        self.uncommonMartialWeapons = uncommonMartialWeapons


class ArmorProficiency:
    name: None
    rank: None
    bonus: None

    def __init__(self, name, rank='untrained'):
        if rank in profBonusByRank:
            self.rank = rank
            self.bonus = profBonusByRank[rank]
        else:
            raise TypeError("Name isn't in list profBonusByRank")


if __name__ == '__main__':
    prof = Proficiency(level=3, rank='expert')
    print(f'\nProficiency:{prof.rank} Bonus:{prof.get_Bonus()}\n\n')

    # atributos e métodos de uma classe iniciadas com "_" (underline) devem ser
    # tratadas como variáveis/funções privadas, ou seja, não devem ser
    # invocadas de fora da classe

    prof.level = 8  # usando o set_level para setar o self._level

    print(prof.level)  # usando o get_level para retornar o valor de
    # self._level

    print(prof._level)  # isto funciona, mas _level é uma variável privada, e
    # não deve ser acessada diretamente
