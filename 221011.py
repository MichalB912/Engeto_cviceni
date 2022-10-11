""" 
auta = ['Škoda', 'Fiat', 'Opel', 'Audi']

while auta:
    auta.pop(0)
    print(auta) 
"""


""" 
string = 'While smyčky mohou být nekonečné'

while string:
    string = string[1:]
    print(string) 
"""


# funkce "break"
""" 
n = 5

while n > 0:
    n -= 1
    if n == 2:
        break
    print(n) 
"""


# nekonečná smyčka while
""" 
switch = True

while switch:
    vstupni_hodnota = input('Zadej písmeno: ')
    
    if vstupni_hodnota.isalpha():
        print(f'{vstupni_hodnota} je opravdu písmeno.')
    else:
        print(f'{vstupni_hodnota} není písmeno, končím program.')
        switch = False 
"""


# vnořená smyčka while
""" 
nadpisy = ['1. kapitola', '2. kapitola']

while len(nadpisy):
    print(nadpisy.pop(0))

    podnadpisy = ['podkapitola 1', 'podkapitola 2']

    while len(podnadpisy):
        print('  ', podnadpisy.pop(0))
 """


# komprehence (snese jen jednu podmínku)
""" 
n = 5

while n > 0: print(n); n -= 1 
"""


# počet výskytů prvku
""" 
barvy = [ 'zelena', 'modra', 'cerna', 'cervena', 'cervena', 'zluta', 'modra', 'seda', 'cerna' , 'cervena', 'zelena' ]

pocet_barev = {}

while barvy:
    barva = barvy.pop()

    if barva not in pocet_barev:
        pocet_barev[barva] = 0

    pocet_barev[barva] += 1

print(pocet_barev) 
"""


# WALRUS operátor
""" 
print(jmeno := 'Lucie')
"""


# úkol z lekce 5, "KOŠÍK"

# TODO proměnné
potraviny = {         #jsou to listy ve slovníku
    'mleko': [30, 5], # index 0 -> cena; index 1 -> mnozstvi 
    'maso': [100, 1], 
    'banan': [30, 10], 
    'jogurt': [10, 5], 
    'chleb': [20, 5], 
    'jablko': [10, 10], 
    'pomeranc': [15, 10], 
}

nabidka = '''
+-----------+------+
| POTRAVINA | CENA |
+-----------+------+
| mleko     | 30,- |
| maso      |100,- |
| banan     | 30,- |
| jogurt    | 10,- |
| chleb     | 20,- |
| jablko    | 10,- |
| pomenrac  | 15,- |
+-----------+------+
'''

kosik = {}

oddelovac = '=' * 40

# TODO pozdrav a vypsání nabídky
print(
    'Vítejte v našem online nákupním centru', 
    oddelovac, 
    nabidka, 
    'Zvol si zboží, pro zaplacení stiskni "q"', 
    sep='\n'
)
# TODO celý cyklus
while (zbozi := input('Zadej název zboží: ')) != 'q':
    # TODO pokud zboží nebude v nabídce
    if zbozi not in potraviny:
        print(zbozi, 'bohužel není v nabídce')
    # TODO pokud vybrané zboží není v nákupním košíku

    # TODO pokud vybrané zboží je v košíku

    # TODO pokud zboží již není skladem

# TODO vypiš obsah košíku