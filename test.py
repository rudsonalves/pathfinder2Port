#!python
''' Este é um arquivo de teste '''

from characterGen import Character


def main():
    ''' Esta é a função main '''

    p1 = Character('Jary', 'dwarf', 'fighter')
    p2 = Character('Abu', ancestry='human', charClass='wizard')

    print(p1)
    print()
    print(p2)


if __name__ == '__main__':
    main()
    print(help(main))
