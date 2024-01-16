### Blink og takki með LED
1. Tengdu rauða LED og láttu hana blikka með 500ms millibili. 
1. Tengdu græna LED sem þú kveikir á með takka.
1. Notaðu eftirfarandi kóða og prófaðu takkann, er eitthvað athugavert?

```python
from machine import Pin
from time import sleep_ms

red = Pin(10, Pin.OUT)
green = Pin(12, Pin.OUT)
takki = Pin(14, Pin.IN, Pin.PULL_UP)

green_kveikt = False  
takki_stada_adur = 1    # geymir stöðu á takka í síðustu umferð

while True:
    # látum rautt LED blikka á 500ms fresti
    red.value(1)
    sleep_ms(500)
    red.value(0)
    sleep_ms(500)

    # kveikjum á grænt LED með takka 
    takki_stada = takki.value()    
    if takki_stada == 0 and takki_stada_adur == 1:
        green_kveikt = not green_kveikt
    green.value(green_kveikt)
    takki_stada_adur = takki_stada  # uppfærum stöðu fyrir næstu umferð
```

Þetta virkar ekki vel. Ástæðan fyrir því er sú að `sleep_ms` stoppar forritið í ákveðinn tíma og ekkert annað gerist á meðan. <br> Við getum leyst þetta betur með að beita `ticks_ms` sem gengur út á að spyrja hvort ákveðinn tími er liðinn og þá keyra kóðabút, á meðan getur annar kóði keyrt í forritinu. 

### Blink og takki með LED með `ticks_ms`

Breyttu nú forritinu þannig að það verði svona:

```python
from machine import Pin
from time import ticks_ms # `ticks_ms` gefur okkur fjölda millisekúnda sem liðnar eru frá því kveikt var að ESP32. 

red = Pin(10, Pin.OUT)
green = Pin(12, Pin.OUT)
takki = Pin(14, Pin.IN, Pin.PULL_UP)

red_kveikt = False 
green_kveikt = False  
takki_stada_adur = 1    

bidtimi = 500                      # ætlum að bíða í 500ms 
timi_lidinn =  ticks_ms()          # skráum upphafspunktinn

while True:
# látum rautt LED blikka
    timi_nuna = ticks_ms()              # skráum hversu langt er síðan ESP ræsti
    if (timi_nuna - timi_lidinn) >= bidtimi:    # True á 500ms fresti 
        red_kveikt = not red_kveikt     # víxlum gildið á boolean
        timi_lidinn = timi_nuna         # uppfærum lidinn tíma í tímann núna fyrir næsta samanburð
    red.value(red_kveikt)               # kveikja/slökkva

# kveikjum á grænt LED með takka 
    takki_stada = takki.value()    
    if takki_stada == 0 and takki_stada_adur == 1:
        green_kveikt = not green_kveikt
    green.value(green_kveikt)
    takki_stada_adur = takki_stada  
```
