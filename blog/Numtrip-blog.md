### Benutzeringabe ##
Als 1. habe ich mir ein Konzept überlegt, die Koordinaten eines bestimmten Feldes zu definieren. Ich bin auf Koordinaten aus Zahlen und Buchstaben gekommen. So ist es für mich persöhnlich praktischer, die Zeilen und Spalten zu unterscheiden (Spalten: Buchst., Zeilen: Zahlen)

Die Beiden eingaben müssen noch validiert werden:
dafür habe ich mich entschieden, für beide eine einzelne Funktion zu schreiben, was für einige schwierigkeiten geführt hat, da ich die ganze formel zweimal schreiben musste... es hat nach ein paar versuchen jedoch geklappt.

in der Funktion auswerten werden die Buchstaben in Zahlen umbewandelt


>def auswerten(zeile, spalte):
>
>    buchstaben = ['A', 'B', 'C', 'D', 'E', 'F']
>
>    spalte = buchstaben.index(spalte.upper())
>    zeile = int(zeile) - 1
>
>    print(zeile)
>
>    board[zeile][spalte] = 0


In der Funktion Play wird alles noch einmal aufgerufen

in der Funktion ... wird geschaut, ob die benachbarten Zellen die gleiche zahl beinhalten
