# LERNZIELE
## Funktionsweise Server-Client Modell
Das Server-Client-Modell ist ein verbreitetes Konzept in der Informationstechnologie, das die Interaktion zwischen Computern in einem Netzwerk beschreibt. Dabei übernimmt der Server die Rolle des zentralen Dienstleisters, der Informationen, Ressourcen oder Services bereitstellt, während der Client die Rolle des Anfragenden oder Nutzenden einnimmt, der diese Dienste in Anspruch nimmt. Hier ist eine grobe Erklärung der Funktionsweise des Server-Client-Modells:

Server: Der Server ist ein leistungsstarker Computer oder eine spezialisierte Hardware, die Dienste oder Ressourcen bereitstellt. Er kann eine Vielzahl von Funktionen ausführen, wie z.B. Datenbanken, Webseiten, E-Mail-Dienste, Dateiserver oder Anwendungen. Der Server ist immer eingeschaltet und wartet darauf, Anfragen von Clients zu erhalten.

Client: Der Client ist ein Computer, ein Smartphone, ein Tablet oder eine andere Geräte, das mit dem Server kommuniziert, um Dienste oder Ressourcen abzurufen. Der Client kann eine spezielle Software oder eine Webanwendung nutzen, um die Anfragen an den Server zu senden und die Antworten zu erhalten.

Anfrage und Antwort: Der Client sendet eine Anfrage an den Server, in der er bestimmte Informationen oder Dienste anfordert. Diese Anfrage kann beispielsweise das Laden einer Webseite, das Abrufen von Daten aus einer Datenbank oder das Senden einer E-Mail umfassen. Der Server empfängt die Anfrage, verarbeitet sie und sendet eine entsprechende Antwort zurück an den Client.

Kommunikationsprotokolle: Die Kommunikation zwischen Server und Client erfolgt über definierte Kommunikationsprotokolle wie HTTP (Hypertext Transfer Protocol) für Webanwendungen, SMTP (Simple Mail Transfer Protocol) für E-Mails oder FTP (File Transfer Protocol) für den Dateitransfer. Diese Protokolle legen die Regeln und Standards fest, wie die Anfragen und Antworten strukturiert und übermittelt werden.

Skalierbarkeit und Lastverteilung: Das Server-Client-Modell ermöglicht eine Skalierbarkeit der Dienste, indem mehrere Server eingesetzt werden, um die Last zu bewältigen. Lastverteilungsmechanismen sorgen dafür, dass Anfragen auf verschiedene Server verteilt werden, um die Auslastung gleichmäßig zu verteilen und die Leistung zu optimieren.

Das Server-Client-Modell bildet die Grundlage für viele Netzwerkdienste und Anwendungen, die im Internet und in lokalen Netzwerken verwendet werden. Es ermöglicht eine effiziente Kommunikation zwischen Computern und die Bereitstellung von Diensten und Ressourcen über das Netzwerk. 

## Funktionsweise und Aufgaben einer API
Eine API (Application Programming Interface) ist eine Schnittstelle, die es verschiedenen Anwendungen ermöglicht, miteinander zu kommunizieren und Daten oder Funktionen auszutauschen. Die Funktionsweise und Aufgaben einer API können wie folgt beschrieben werden:

Kommunikation und Datenübertragung: Eine API definiert die Kommunikationsprotokolle, Datenformate und Methoden, die von einer Anwendung verwendet werden können, um mit einer anderen Anwendung zu interagieren. Sie stellt eine standardisierte Schnittstelle bereit, über die Daten zwischen den Anwendungen ausgetauscht werden können.

Zugriff auf Funktionen und Ressourcen: Eine API ermöglicht den Zugriff auf spezifische Funktionen, Dienste oder Ressourcen einer Anwendung. Sie definiert, welche Operationen durchgeführt werden können und welche Daten verfügbar sind. Entwickler können die API nutzen, um bestimmte Aufgaben zu automatisieren oder auf die Funktionalität einer Anwendung zuzugreifen.

Datenformatierung und -transformation: APIs können auch eine Rolle bei der Formatierung und Transformation von Daten spielen. Sie können beispielsweise Daten aus einem bestimmten Format in ein anderes Format umwandeln, um eine reibungslose Kommunikation zwischen verschiedenen Anwendungen zu gewährleisten.

Sicherheit und Zugriffskontrolle: APIs bieten auch Sicherheitsmechanismen und Zugriffskontrollen, um den geschützten Zugriff auf Daten und Funktionen zu gewährleisten. Sie können Authentifizierungs- und Autorisierungsmechanismen implementieren, um sicherzustellen, dass nur autorisierte Anwendungen oder Benutzer auf die API zugreifen können.

Vereinfachung der Entwicklung: Eine API abstrahiert komplexe Funktionen und Datenstrukturen und stellt eine vereinfachte Schnittstelle bereit, die von Entwicklern leichter genutzt werden kann. Sie ermöglicht es, Anwendungen schneller zu entwickeln, da Entwickler auf vorhandene Funktionen und Dienste zugreifen können, anstatt sie von Grund auf neu zu entwickeln.

Die Aufgaben einer API variieren je nach Kontext und Anwendungsbereich. APIs können beispielsweise in Webentwicklung, mobilen Anwendungen, Datenbanken, Cloud-Services und vielen anderen Bereichen eingesetzt werden. Sie sind ein grundlegendes Konzept in der Softwareentwicklung und ermöglichen die Integration und Interoperabilität verschiedener Anwendungen und Systeme.

### HTTP Methoden GET, POST, PUT, DELETE
Die HTTP-Methoden GET, POST, PUT und DELETE sind grundlegende Methoden, die in der Kommunikation zwischen Clients (z. B. Webbrowsern) und Servern im World Wide Web verwendet werden. Hier ist eine Erklärung der einzelnen Methoden:

GET: Die GET-Methode wird verwendet, um Daten vom Server abzurufen. Wenn ein Client eine GET-Anfrage sendet, fordert er bestimmte Ressourcen oder Informationen vom Server an. Die Anfrage wird in der Regel über die URL (Uniform Resource Locator) an den Server gesendet. Die Antwort des Servers enthält dann die gewünschten Daten, die an den Client zurückgesendet werden.

POST: Die POST-Methode wird verwendet, um Daten an den Server zu senden und diese Daten zu verarbeiten. Im Gegensatz zur GET-Methode, bei der die Daten in der URL übermittelt werden, werden bei POST die Daten im Body der Anfrage übertragen. POST wird häufig verwendet, wenn Formulardaten oder andere Informationen an den Server gesendet werden, die dort verarbeitet werden sollen, beispielsweise das Speichern von Daten in einer Datenbank.

PUT: Die PUT-Methode wird verwendet, um Daten an eine bestimmte URL zu senden und diese Daten auf dem Server zu aktualisieren oder zu ersetzen. Mit PUT können neue Ressourcen erstellt werden oder bestehende Ressourcen aktualisiert werden. Der Client sendet die Daten, die aktualisiert oder hinzugefügt werden sollen, im Body der Anfrage an den Server. PUT wird häufig in RESTful-APIs verwendet, um Daten zu aktualisieren oder hochzuladen.

DELETE: Die DELETE-Methode wird verwendet, um eine bestimmte Ressource auf dem Server zu löschen. Der Client sendet eine DELETE-Anfrage an den Server, um die angegebene Ressource zu entfernen. Die DELETE-Methode erfordert normalerweise die Angabe der URL der zu löschenden Ressource.

Diese vier HTTP-Methoden (GET, POST, PUT, DELETE) bilden das Grundgerüst für die Interaktion zwischen Clients und Servern im Web. Sie ermöglichen es, Daten abzurufen, Daten zu senden, Daten zu aktualisieren oder zu löschen und spielen eine zentrale Rolle bei der Entwicklung von Webanwendungen und der Kommunikation zwischen verschiedenen Systemen im Internet.

### Funktionsweise eines simplen Web-Servers: 
Ein einfacher Web-Server empfängt HTTP-Anfragen von Clients, verarbeitet sie und sendet die entsprechenden HTTP-Antworten zurück 
an die Clients. Er verwendet das HTTP-Protokoll, um die Kommunikation zwischen dem 
Server und den Clients zu ermöglichen.

### Was ist ein Protokoll? 
Ein Protokoll ist eine Reihe von Regeln und Standards, die den 
Austausch von Daten zwischen Geräten oder Systemen regeln. Es definiert das Format der 
Daten, die während der Kommunikation gesendet werden, sowie die Verfahren und Regeln, 
die befolgt werden müssen, um eine erfolgreiche Kommunikation zu gewährleisten.

### TCP-IP Stack: 
Der TCP/IP-Stack ist ein Referenzmodell für Netzwerkprotokolle, das aus 
verschiedenen Schichten besteht, die jeweils spezifische Funktionen haben. Die wichtigsten 
Schichten sind:
• Anwendungsschicht: Hier finden sich Protokolle wie HTTP, DNS und DHCP, die für den 
Datenaustausch zwischen Anwendungen zuständig sind.
• Transportschicht: Diese Schicht umfasst Protokolle wie TCP (Transmission Control Protocol) 
und UDP (User Datagramm Protocol), die den sicheren und zuverlässigen Transport von 
Daten zwischen Endpunkten ermöglichen.
• Vermittlungsschicht/Internetschicht: Hier arbeitet das IP-Protokoll, das die Adressierung und 
das Routing von Datenpaketen im Internet ermöglicht.
• Physikalische Schicht/Netzzugangsschicht: Diese Schicht behandelt die physische 
Übertragung der Daten über das Netzwerkmedium, z. B. über Ethernet oder WLAN.
### Anwendungsschicht:
• HTTP (Hypertext Transfer Protocol): Protokoll zur Übertragung von Webseiten und anderen 
Daten im Internet.
• DNS (Domain Name System): Protokoll zur Auflösung von Domänennamen (z. B. 
www.example.com) in IP-Adressen.
• DHCP (Dynamic Host Konfiguration Protocol): Protokoll zur automatischen Zuweisung von 
Netzwerkkonfigurationen wie IP-Adressen an Geräte in einem Netzwerk.
### Transportschicht:
• TCP (Transmission Control Protocol): Protokoll, das eine verbindungsorientierte, zuverlässige 
Übertragung von Datenpaketen ermöglicht.
• UDP (User Datagramm Protocol): Protokoll, das eine verbindungslose Übertragung von 
Datenpaketen ermöglicht und weniger zuverlässig ist als TCP, aber geringere Latenzzeiten 
aufweist.
### Vermittlungsschicht/Internetschicht:
• IP (Internet Protocol): Protokoll, das die Adressierung und das Routing von Datenpaketen 
im Internet ermöglicht.
### Aufbau einer IP-Adresse: 
Eine IP-Adresse besteht aus einer Reihe von Zahlen, die zur 
Identifizierung eines Netzwerkgeräts verwendet werden. Sie besteht aus zwei Teilen: der 
Netzwerkadresse und der Hostadresse. Eine IPv4-Adresse besteht aus vier durch Punkte 
getrennten Zahlen, z. B. 192.168.0.1.
• Subnetzmasken: Die Subnetzmaske wird verwendet, um den Teil einer IP-Adresse zu 
identifizieren, der das Netzwerk angibt. Sie trennt die Netzwerkadresse von der 
Hostadresse. Eine Subnetzmaske besteht ebenfalls aus vier durch Punkte getrennten
Zahlen, z. B. 255.255.255.0.
### Subnetze: Subnetze sind Teilnetze innerhalb eines größeren Netzwerks. Durch die 
Verwendung von Subnetzen können große Netzwerke in kleinere, effiziente zu 
verwaltende Teile aufgeteilt werden.
### Private und öffentliche IP-Adressen: Private IP-Adressen sind Adressen, die in lokalen 
Netzwerken verwendet werden und nicht direkt im Internet geroutet werden können. 
Öffentliche IP-Adressen sind eindeutige Adressen, die von Internetdienstanbietern (ISPs) 
zugewiesen werden und den direkten Zugriff auf das Internet ermöglichen.
### Berechnung der Anzahl Netzwerke und Hosts mit der Subnetzmaske: Die Anzahl der 
verfügbaren Netzwerke und Hosts kann mit der Subnetzmaske bestimmt werden. Durch 
die Kombination der Netzwerkteilbits in der Subnetzmaske lässt sich die Anzahl der 
Netzwerke bestimmen, während die verbleibenden Hostteilbits die Anzahl der Hosts pro 
Netzwerk bestimmen.
### Physikalische Schicht/Netzzugangsschicht:
• ARP (Adresse Resolution Protocol): Protokoll, das IP-Adressen in MAC-Adressen auflöst, um 
die Kommunikation auf der physikalischen Schicht zu ermöglichen.
• Aufbau eines IP-Frames: Ein IP-Frame besteht aus einem Header, der Informationen wie 
Quell- und Ziel-IP-Adresse enthält, und einem Payload, der die eigentlichen Daten enthält.
• Aufbau eines Ethernet-Frames: Ein Ethernet-Frame enthält den Header mit Quell- und ZielMAC-Adresse sowie den Payload mit den Daten.
• Aufbau einer MAC-Adresse: Eine MAC-Adresse ist eine eindeutige Kennung, die einem 
Netzwerkgerät zugewiesen ist. Sie besteht aus 48 Bits, die üblicherweise als sechsstellige 
Hexadezimalzahl dargestellt werden.
• Switch vs. Router: Ein Switch verbindet Geräte in einem lokalen Netzwerk und ermöglicht die 
Kommunikation zwischen ihnen auf der Ethernet-Ebene. Ein Router verbindet verschiedene 
Netzwerke und ermöglicht den Datenverkehr zwischen ihnen auf der Netzwerkebene.
• Ablauf ARP: Das Adresse Resolution Protocol (ARP) wird verwendet, um die Zuordnung 
zwischen IP-Adressen und MAC-Adressen zu ermitteln. Es sendet Anfragen im Netzwerk, um 
die MAC-Adresse eines bestimmten Geräts mit einer bekannten IP-Adresse zu ermitteln.
• Switch- und Routing-Tabellen lesen und verstehen: Switch-Tabellen enthalten Informationen 
zur Zuordnung von MAC-Adressen zu Portnummern, während Routing-Tabellen 
Informationen zur Weiterleitung von IP-Paketen enthalten.
• Routing-Tabellen erstellen: Routing-Tabellen werden verwendet, um den Weg für den 
Datenverkehr zwischen verschiedenen Netzwerken festzulegen. Sie enthalten Informationen 
wie Zielnetzwerke und zugehörige Next-Hop-Adressen.
• Netzwerke konfigurieren: Dies beinhaltet die Zuweisung von IP-Adressen, Subnetzmasken, 
Standardgateways und anderen Netzwerkkonfigurationen auf den Geräten.
• Aufgaben von NAT (Network Adresse Translation): NAT ermöglicht die Übersetzung von IPAdressen zwischen öffentlichen und privaten Netzwerken, um den Zugriff auf das Internet für 
Geräte mit privaten IP-Adressen zu ermöglichen.
• Hole Punching: Hole Punching ist eine Technik, bei der eine Verbindung zwischen zwei 
Geräten in unterschiedlichen privaten Netzwerken hergestellt wird, indem temporäre 
Durchgangsöffnungen in den Netzwerkfirewalls erstellt werden. Dadurch können die Geräte 
direkt miteinander kommunizieren, obwohl sie sich hinter NAT befinden