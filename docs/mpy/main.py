import network
# WLAN als Empfangsstation initialisieren
#
import time
import machine
import ssd1306
# HTTP-Request erstellen
import urequests
from ens import ENS160

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(64, 48, i2c)
ens160 = ENS160(i2c, temperature=22, humidity=35)
ens160.aqi
ens160.tvoc
ens160.eco2
wlan = network.WLAN(network.STA_IF)
# WLAN aktivieren
wlan.active(True)
# verbinden mit dem Netzwerk
wlan.connect('alice im WLANd', 'rabbitShole')
# ist das Netzwerk verbunden?
wlan.isconnected()

while True:
    aqi = ens160.aqi
    tvoc = ens160.tvoc
    eco2 = ens160.eco2
    print(aqi, tvoc, eco2)
    time.sleep(2)
    display.fill(0)
    display.text(f'co2: {eco2[0]}', 0, 0, 1)
    display.text(f'luft: {tvoc}', 0, 20, 1)
    display.text(f'qual: {aqi[0]}', 0, 40, 1)
    display.show()
    data = {'luft: {tvoc}', 'qual: {aqi[0]}'co2: {eco2[0]}'}
    # Datenpaket abschicken
    res = urequests.post('http://node-red-xyzq.onrender.com.proxy.gbsl.website/api/sensor', json=data)
    # Antwort ausgeben
    res.content