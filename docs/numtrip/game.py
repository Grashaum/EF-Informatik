board = [
        [2, 4, 8, 8, 8, 8],
        [4, 2, 8, 2, 1, 4],
        [4, 4, 8, 4, 2, 2],
        [2, 8, 8, 4, 1, 2],
        [2, 4, 4, 4, 16, 4]
    ]
def spielfeld():

    def spaltennummer():
        print('    A  B  C  D  E  F')
    spaltennummer()
    zeilennummer = 1
    for zeile in board: #board wurde in den letzten Zeilen definiert
        print('  ', end='')
        for zelle in zeile:#Zellen und zeilen sind teile des Spielfelds
            print(' --', end='')#diese Zeile soll enden, wenn es keine zellen mehr in der Zeile darunter hat; für jede Zelle einen Strich
        print(' ')
        print(zeilennummer, end=' ')
        zeilennummer = zeilennummer + 1 #zeilen werden nummeriert
        for zelle in zeile:
            if zelle == 0:
                print ('|  ', end='')
            elif zelle > 10:
                print(f'|{zelle}', end='') # zahlen werden angepasst; die zehn tanzt nicht aus der Reihe 
            else:
                print(f'|{zelle} ', end='')# print neue zeile? auf jedenfall kommt vor jede zelle ein | 
        print('|')# Am Schluss von jeder Zeile kommt ein |
            
    print('  ', end='')
    for zelle in board[0]:
        print(' --', end='')# dieser teil ist noch der abschluss; die letzte Zeile wird seperat beschrieben
    print('')


def verify_input(zeile):
    if not zeile.isnumeric():
        print('Die Ziffern müssen Zahlen sein!')
        return False
    else:
        return True
    
def text_input(text):
    text = text.upper().strip()
    for h in text:
        if h not in 'ABCDEF':
            print('Die spalte sollte ein Buchstabe sein')
            return False
        else:
            return True


def eingabe():
    zeile = input('Geben Sie die Zeile des Feldes ein (Form: Zahl(1-5)): ')
    spalte = input('Geben Sie die spalte des Feldes ein (Form: Buchst.(a-f)): ')
    while not verify_input(zeile):
        zeile = input('Geben Sie die Zeile des Feldes ein (Form: Zahl(1-5)): ')
    produkt = verify_input(zeile)
    if produkt:
        print('Produkt', produkt)
    else:
        print('Fehlerhafte Eingabe!')

    while not text_input(spalte):
        spalte = input('Geben Sie die spalte des Feldes ein (Form: Buchst.(a-f)): ')
    if text_input(spalte):
        print('Produkt', text_input(spalte))
    else:
        print('Fehlerhafte Eingabe!')
    return (zeile, spalte)

def auswerten(zeile, spalte):
    buchstaben = ['A', 'B', 'C', 'D', 'E', 'F']
    spalte = buchstaben.index(spalte.upper())
    zeile = int(zeile) - 1
    print(zeile)
    board[zeile][spalte] = 0

def zellen_kombination():
    '''
    def fill4(x, y, alteFarbe, neueFarbe):
    if getPixel(x, y) == alteFarbe:
        setPixel(x, y, neueFarbe)
        fill4(x, y + 1, alteFarbe, neueFarbe)  # unten
        fill4(x, y - 1, alteFarbe, neueFarbe)  # oben
        fill4(x + 1, y, alteFarbe, neueFarbe)  # rechts
        fill4(x - 1, y, alteFarbe, neueFarbe)  # links
    gebraucht: koordinaten    
    '''

def play():
    while True:
        spielfeld()
        zeile, spalte = eingabe()
        auswerten(zeile, spalte)
        spielfeld()

play()
