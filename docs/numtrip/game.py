import random
board = [
        [2, 4, 8, 8, 8, 4],
        [4, 2, 8, 2, 1, 4],
        [4, 4, 8, 4, 2, 4],
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
    
def text_input(text):# es wird validiert ob der Text auch wirklich Text ist
    text = text.upper().strip()
    for h in text:
        if h not in 'ABCDEF':
            print('Die spalte sollte ein Buchstabe sein')
            return False
        else:
            return True

def eingabe():
    zeile = input('Geben Sie die Zeile des Feldes ein (Form: Zahl(1-5)): ')
    while not verify_input(zeile):
        zeile = input('Geben Sie die Zeile des Feldes ein (Form: Zahl(1-5)): ')
    spalte = input('Geben Sie die Spalte des Feldes ein (Form: Buchst.(a-f)): ')
    while not text_input(spalte):
        spalte = input('Geben Sie die Spalte des Feldes ein (Form: Buchst.(a-f)): ')
    return (zeile, spalte)

def auswerten(zeile, spalte):
    buchstaben = ['A', 'B', 'C', 'D', 'E', 'F']
    spalte = buchstaben.index(spalte.upper()) #string wird in zahl umgewandelt
    zeile = int(zeile) - 1
    nachbarzellen(zeile, spalte)
    board[zeile][spalte] = 0# zeile und spalte werden auf null gesetzt; wird 'geleert'

def nachbarzellen(zeile, spalte): #überprüfung der Nachbarszellen
    zahl = board[zeile][spalte] 
    board[zeile][spalte] = 0
    if not zeile == 4 and board[zeile +1][spalte] == zahl: # +1 weil man in der liste boart 'vorwärts'geht und nicht nach oben
        nachbarzellen(zeile +1, spalte)
    if not spalte == 5 and board[zeile][spalte +1] == zahl:
        nachbarzellen(zeile, spalte +1)
    if not zeile == 0 and board[zeile -1][spalte] == zahl: 
        nachbarzellen(zeile -1, spalte)
    if not zeile == 0 and board[zeile][spalte -1] == zahl:
        nachbarzellen(zeile, spalte -1)
    drop_cells(zeile, spalte)
def drop_cells(zeile, spalte):
    for zeilen_idx in [4, 3, 2, 1, 0]:
        for spalten_idx in [0, 1, 2, 3, 4, 5]:
            index = zeilen_idx
            while not index <= 0 and board [index][spalten_idx] == 0:
                index = index -1
            board[zeilen_idx][spalten_idx] = board[index][spalten_idx] # die gefundene Zelle wird mit der alten gewechhselt
            board[index][spalten_idx] = random.choice([2, 4, 8]) # die alte Zelle wird auf null gesetzt
    fill_emptycells(zeile, spalte)

def fill_emptycells(zeile, spalte):
    pass
    for zeile in board:
        for zelle in zeile:
            if zelle == 0:
                board[zeile][spalte] = random.choice(1, 2, 4, 8)

def spielende():
    for zeile in board:
        for zelle in zeile:
            if zelle >= 100:
                print('Sie haben gewonnen!!')
                return True
    return False

def play():
    while not spielende():
        spielfeld()
        zeile, spalte = eingabe()
        auswerten(zeile, spalte)

play()
