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
    if not zeile.isnumeric() or not 5 >= int(zeile) > 0:
        print('Fehlerhafte Eingabe!')
        return False
    else:
        return True
    
def text_input(text):# es wird validiert ob der Text auch wirklich Text ist
    text = text.upper().strip()
    for h in text:
        if h not in 'ABCDEF':
            print('Fehlerhafte Eingabe!')
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
    buchstaben = ['A', 'B', 'C', 'D', 'E', 'F']
    spalte = buchstaben.index(spalte.upper()) #string wird in zahl umgewandelt
    zeile = int(zeile) - 1
    return (zeile, spalte)

def feldauswahl_erlaubt(zeile, spalte):
    if (spalte + 1) <= 5:
        if board[zeile][spalte] == board[zeile][spalte + 1]:
            return True
    if (spalte - 1) >= 0:
        if board[zeile][spalte] == board[zeile][spalte - 1]:
            return True
    if (zeile + 1) <= 4:
        if board[zeile][spalte] == board[zeile + 1][spalte]:
            return True
    if (zeile - 1) >= 0:
        if board[zeile][spalte] == board[zeile - 1][spalte]:
            return True
    print('Das ausgewählte Feld muss Nachbaren haben')
    return False

def auswerten(zeile, spalte):
    #while not feldauswahl_erlaubt(zeile, spalte):
        #eingabe()
    vorherige_zahl = board[zeile][spalte]
    nachbarzellen(zeile, spalte, vorherige_zahl)
    return zeile, spalte, vorherige_zahl

def nachbarzellen(x, y, vorherige_zahl):
    # Rahmenbedingungen
    if x < 0 or x > 4:
        return False
    if y < 0 or y > 4:
        return False
    # Feldüberprüfen
    # im Spielfeld die richtige Liste (zeile), dann richtige Position in Liste (spalte)
    if board[x][y] == vorherige_zahl:
        board[x][y] = 0
        nachbarzellen(x, y + 1, vorherige_zahl)  # rechts
        nachbarzellen(x, y - 1, vorherige_zahl)  # links
        nachbarzellen(x + 1, y, vorherige_zahl)  # unten
        nachbarzellen(x - 1, y, vorherige_zahl)  # oben

def drop_cells(zeile, spalte, vorherige_zahl):
    board[zeile][spalte] = vorherige_zahl * 2
    for zeilen_idx in [4, 3, 2, 1, 0]:
        for spalten_idx in [0, 1, 2, 3, 4, 5]:
            if board[zeilen_idx][spalten_idx] == 0:
                index = zeilen_idx
                while index > 0 and board [index][spalten_idx] == 0:
                    index = index -1
                board[zeilen_idx][spalten_idx] = board[index][spalten_idx] # die gefundene Zelle wird mit der alten gewechhselt
                board[index][spalten_idx] = 0 # die alte Zelle wird auf null gesetzt
    fill_emptycells()

def fill_emptycells():
    for zeilen_nr in range(0, 5):
        for palten_nr in range (0, 6):
            if board[zeilen_nr][palten_nr] == 0:
                board[zeilen_nr][palten_nr] = random.choice([1, 2, 4, 8])

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
        zeile, spalte, vorherige_zahl = auswerten(zeile, spalte)
        drop_cells(zeile, spalte, vorherige_zahl)

play()
