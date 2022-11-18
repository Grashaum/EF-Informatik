def spielfeld():
    board = [
        [2, 4, 1, 8, 8, 7],
        [4, 2, 8, 2, 1, 6],
        [4, 4, 8, 4, 2, 2],
        [2, 8, 1, 4, 1, 3],
        [2, 4, 4, 4, 10, 4]
    ]
    zeilennummer = 1
    for zeile in board: #board wurde in den letzten Zeilen definiert
        
        for zelle in zeile:#Zellen und zeilen sind teile des Spielfelds
            print(' - - ', end='')#diese Zeile soll enden, wenn es keine zellen mehr in der Zeile darunter hat; für jede Zelle einen Strich
        print(' ')
        print(zeilennummer, end=' ')
        zeilennummer = zeilennummer + 1 #zeilen werden nummeriert
        for zelle in zeile:
            print(f'|{zelle}', end='')# print neue zeile? auf jedenfall kommt vor jede zelle ein |
            if zelle < 10:
                print(' ', end='')# zahlen werden angepasst; die zehn tanzt nich aus der Reihe
        print('|')#Am Schluss von jeder Zeile kommt ein |

    for zelle in board[0]:
        print(' --', end='')# dieser teil ist noch der abschluss; die letzte Zeile wird seperat beschrieben
    print(' ')

spielfeld()
...