'''
Um das Sternchenquadrat anzuzeigen, braucht es sine funktion für anfang und ende 
und eine zweite für die zeilen dazwischen


eigener versuch:
def rechteck():
    eingabe1 = input("Gib Breite ein: ")
    eingabe2 = input("Gib Höhe ein: ")
    zahl1 = int(eingabe1)
    zahl2 = int(eingabe2)
    print(" *" * zahl1)
    for i in range (zahl2):
       print(" *",  end='')
rechteck()
'''
zahl = 12
def horizontal():
    print('*' * zahl)

horizontal()
for i in range (zahl):
    print('*' + ' ' * (zahl - 2) + '*')
horizontal()