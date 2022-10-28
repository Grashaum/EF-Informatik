
# Variablen
gesucht = 'test'
gefunden = []
falsch_geraten = []

def show():
    print('Falsche Buchstaben:', falsch_geraten)#print falsche buchstaben und alle buchstaben, die nicht vorkommen
    for buchstabe in gesucht:# überprüfen ob der eingegebene buchstabe im wort vorkommt
        if buchstabe in gefunden:#wenn er vorkommt
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')#neue zeile

def is_valid(inp):# überprüfen ob der Input ein buchstabe ist und klein geschrieben
    return True

def eingabe():# wenn der input nicht valid ist, fragt es nach neuer eingabe
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        buchstabe = input('Buchstabe? ')
    return buchstabe.lower()

def auswerten(valid_inp):
    if valid_inp in gesucht:
        gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)

def gewonnen():
    for buchstabe in gesucht:
        if buchstabe not in gefunden:
            return False
    return True

def game_over():  
    return gewonnen()
    #len of attempts zählen

def play():
    while not game_over():
        buchstabe = eingabe()
        auswerten(buchstabe)
        print(buchstabe)
        show()
    if gewonnen():
        print('...:)')
    else:
        print("!!!")
play()