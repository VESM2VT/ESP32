# Tímaverkefni 3 

- 10% af heildareinkunn
- Einstaklingsverkefni.
- Settu upp verklega með brauðbretti og íhlutum.
- Passaðu að þú getir útskýrt fyrir kennara allan kóða sem þú skrifar.

---

## HC-SR04 Ultrasonic Sensor

Kynntu þér hvernig HC-SR04 Ultrasonic Sensor virkar með því að lesa [þessa grein](https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/) (lestu **að** *Wiring – Connecting HC-SR04 to Arduino Uno*).
Tengdu HC-SR04 við ESP32 og skoðaðu kóðann hér fyrir neðan:

![ultrasonic](https://raw.githubusercontent.com/VESM2VT/ESP32/main/myndir/ultrasonic.png)

```python
from machine import Pin
from time import sleep_ms, sleep_us, ticks_us, ticks_diff

echo = Pin(47, Pin.IN)
trig = Pin(48, Pin.OUT)

def maela_fjarlaegd():
    # Sendum 10 míkrosekúndna púls
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    
    # Bíðum eftir að svarpúlsinn byrji
    while not echo.value(): # eða echo.value() == 0
        pass # Ekkert að gera nema bíða
    
    # Svarpúlsinn er byrjaður að berast þannig að við setjum skeiðklukku í gang
    upphafstimi = ticks_us()
    
    # Bíðum eftir að svarpúlsinn endi
    while echo.value(): # eða echo.value() == 1
        pass # Ekkert að gera nema bíða
    
    # Svarpúlsinn er ekki lengur að berast þannig að við stoppum skeiðklukkuna
    endatimi = ticks_us()
    
    # Reiknum muninn á upphafs og endatímanum
    heildartimi = ticks_diff(endatimi, upphafstimi)
    
    # Notum svo helildartímann til að reikna út fjarlægðina skv. jöfnunni fjarlægð = hraði * tími
    # byrjum á að helminga heildartímann (merkið fer fram og til baka)
    heildartimi /= 2
    # Hljóðhraðinn er 340 m/s (34000 cm/s) og svo deilum við með 1000000 til að fá cm á míkrósekúndur.
    hljodhradi = 34000 / 1000000
    # Reiknum loks fjarlægðina í cm
    fjarlaegd = heildartimi * hljodhradi
    
    # Skilum svo fjarlægðinni sem heiltölu sem er næg nákvæmni
    return int(fjarlaegd)
    

while True:
    fjarlaegd = maela_fjarlaegd()
    print(f"Mæld fjarlægð: {fjarlaegd}")
    sleep_ms(500)
```

## Verkefni 1 (50%) - Nálægðarskynjari

Settu upp rás með Ultrasonic skynjaranum, þremur LED og hátalara (active buzzer, hægt að meðhöndla eins og LED peru nema það þarf ekki viðnám). Skrifaðu svo forrit fyrir rásina sem útfærir virknina í töflunni hér að neðan:

Fjarlægð í cm. | LED 1 | LED 2 | LED 3 | Hátalari
---: | --- | --- | --- | --- 
100 eða meira | slökkt | slökkt | slökkt | ekkert hljóð
80 - 100 | kveikt | slökkt | slökkt  | ekkert hljóð
60 - 80 | kveikt | kveikt | slökkt  | ekkert hljóð
40 - 60 | kveikt | kveikt | kveikt  | ekkert hljóð
minna en 40 | kveikt | kveikt | kveikt  | hljóð

## Verkefni 2 (50%) - Rafrænt málband með minni

Settu upp rásina sem þú gerðir í [lið 3](https://github.com/VESM2VT/ESP32/blob/main/verkefni/Timaverkefni1.md#3-7-segment-fjórir-tölustafir-10) í Tímaverkefni 1. Bættu Ultrasonic skynjaranum við rásina forritaðu rásina svo þannig að fjarlægðin sem skynjarinn mælir sé birt í sentimetrum á SevenSegment skjánum. Mældu fjarlægðina á 100 ms. fresti (nota `ticks_ms`). Bættu takka við rásina, þegar ýtt er á hann frýs mælingin þar til aftur er ýtt á takkann (muna eftir *debounce*). Þegar ýtt er á takkann til að frysta mælinguna á sú tala sem mælingin sýnir að bætast í lista og þegar fimm mælingar eru komnar í listann á að skrifa listann snyrtilega á skjáinn á fartölvunni þinni (með `print`) og listinn á að tæmast. Passaðu að mælingin skráist bara í listann þegar mælingin er fryst en ekki þegar hún er af-fryst. Dæmi um úttak:

```
Mæling nr. 1: 134 cm.
Mæling nr. 2: 123 cm.
Mæling nr. 3: 47 cm.
Mæling nr. 4: 156 cm.
Mæling nr. 5: 39 cm.
```

---

## Námsmat og skil

- Yfirferð og námsmat á sér stað í tíma. 
- Fyrir hvern lið er gefið heilt fyrir fullnægjandi lausn, hálft ef lausn er ábótavant, ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnum.
