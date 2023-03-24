# Kapitel 3-8

## 3. Vom LAN zum Internet
Das Schulhausnetzwerk ist ein LAN (Local Area Network)
Das Telefonnetzwerk ist ein WAN (Wide Area Network)

Netzwerke: Gruppe von Hosts, die ähnliche ansprüche haben. 
Topologien : Je nach Art der Verbindung zum Medium entsteht eine andere Topologie.

-> Bus: "serieschaltung" der Komputer

-> Stern - switch: Bei dieser Topologie sind alle Computer durch ein zentrales Gerät verbunden.

Router: verbinden verschiedene LAN's miteinander. Oft benutzt man geräte, die switch und ein router zugleich sind.

Hosts sind allgemein geräte, die nachrichten senden und empfangen.

Gateway

## 4. IP-Adressen
* Nertwerkteil
        
    Vorderer Teil der IP-Adresse.
    Er ist für alle Geräte im selben Netzwerk gleich und entspricht der Grundadresse von allen Geräten, welche sich in diesem Netzwerk befinden.
* Hostteil

    Hinterer Teil der IP-Adresse.
    Er ist für jedes Gerät (auf englisch Host genannt) unterschiedlich. Es dürfen keine zwei Geräte im selben Netz den selben Hostteil in ihrer IP-Adresse aufweisen.

Diese Netzmaske sieht zunächst wie eine IP-Adresse aus, d.h. sie besteht auch aus vier Zahlen von je einem Byte Länge.

Ergänzt man den Netzwerkteil mit lauter 0 zu einer vollen 32 Bit langen IP-Adresse, so erhält man die Netzwerkadresse.

Die Netzwerkadresse wird gebraucht, wenn mehrere Netzwerke miteinander über Router verbunden werden. Sie darf nicht als IP-Adresse für ein einzelnes Gerät verwendet werden!

Auch bei den IP-Adressen gibt es Broadcastadressen (wie bei den MAC-Adressen). Sie werden gebraucht, wenn ein IP-Paket an alle Geräte innerhalb eines Netzwerkes gesendet werden sollen. Im Unterschied zur MAC-Adresse kann man aber auch ein IP-Paket an alle Geräte in einem anderen Netzwerk, als dem eigenen senden.

Pakete aus dem Internet für den Weitertransport im privaten Netzwerk erhalten eine private IP-Adresse.

## 5. Schichtenmodell
MAC-Adresse

Mac-Tabelle

Routing-Tabelle

Ethernet-Frame

ARP