def spielfeld():
    board = [
        [2, 4, 1, 8, 8, 8],
        [4, 2, 8, 2, 1, 4],
        [4, 4, 8, 4, 2, 2],
        [2, 8, 1, 4, 1, 2],
        [2, 4, 4, 4, 16, 4]
    ]
    def zellennummer():
        print('    A  B  C  D  E  F')
    zellennummer()
    zeilennummer = 1
    for zeile in board: #board wurde in den letzten Zeilen definiert
        print('  ', end='')
        for zelle in zeile:#Zellen und zeilen sind teile des Spielfelds
            print(' --', end='')#diese Zeile soll enden, wenn es keine zellen mehr in der Zeile darunter hat; für jede Zelle einen Strich
        print(' ')
        print(zeilennummer, end=' ')
        zeilennummer = zeilennummer + 1 #zeilen werden nummeriert
        for zelle in zeile:
            print(f'|{zelle}', end='')# print neue zeile? auf jedenfall kommt vor jede zelle ein |
            if zelle < 10:
                print(' ', end='')# zahlen werden angepasst; die zehn tanzt nich aus der Reihe
        print('|')# Am Schluss von jeder Zeile kommt ein |
    print('  ', end='')
    for zelle in board[0]:
        print(' --', end='')# dieser teil ist noch der abschluss; die letzte Zeile wird seperat beschrieben
    print('')
def verify_input(raw):
     if not raw[:3].isnumeric():
        print('Die Ziffern müssen Zahlen sein!')
        return False
def text_input(text):
    text = text.upper().strip()
    for h in text:
        if h not in 'ABCDEF':
            print('Die spalte sollte ein Buchstabe sein')
            return False


spielfeld()
zinput = input('Geben Sie die Zeile des Feldes ein (Form: Zahl(1-5)): ')
tinput = input('Geben Sie die spalte des Feldes ein (Form: Buchst.(a-f)): ')
while not verify_input(zinput):
    zinput = input('Geben Sie die Zeile des Feldes ein (Form: Zahl(1-5)): ')
produkt = verify_input(zinput)
if produkt:
    print('Produkt', produkt)
else:
    print('Fehlerhafte Eingabe!')

while not text_input(tinput):
    tinput = input('Geben Sie die spalte des Feldes ein (Form: Buchst.(a-f)): ')
produkt = text_input(tinput)
if produkt:
    print('Produkt', produkt)
else:
    print('Fehlerhafte Eingabe!')