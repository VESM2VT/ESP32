# Tímaverkefni 5

- 10% af heildareinkunn
- Einstaklingsverkefni.
- Settu upp verklega.
- Passaðu að þú getir útskýrt fyrir kennara allan kóða sem þú skrifar.

---

**Lóðaðu viðnám og víra með male enda við LED perurnar**

## 1. Beygjuljós (20%)
1. Tvö stefnuljós, LED lýsir (ekki blikkandi ljós) þegar bíllinn beygir til hliðar.
2. Beygjuljósperurnar eiga að vera fremst á bílnum á sitthvorri hliðinni.

## 2. Blikkandi lögguljós með `ticks_ms` (30%) 
1. Bíllinn kveikir á blikkandi lögguljós (tvær LEDs) á meðan bíllinn keyrir áfram. 
2. Löggluljósin eiga að vera aftast á bílnum.

## 3. Bakkhljóð og `ticks_ms` (20%)
1. Bakkhljóð með buzzer þegar bíllinn bakkar. 
   
## 4. Notaðu innbyggðu NeoPixel LED peruna (15%)
EPS32-S3 er með eina innbyggða RGB ljósadíóðu sem er tengd við pinna 48. Láttu peruna blikka í takt við ljósin hér að ofan.

```python
from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

# Innbyggða neopixel peran er á pinna 48
neopixel_pinni = Pin(48, Pin.OUT)

# Búum til tilvik af NeoPixel klasanum
# sendum inn pinnann og fjölda rgb pera
rgb = NeoPixel(neopixel_pinni, 1)

# litirnir eru rautt, grænt og blátt og gildin 0 til og með 255
rgb[0] = [255, 0, 0] # rauður

# verðum svo að kalla á write fallið til að skrifa litinn á peruna
rgb.write()

sleep_ms(2000)

rgb[0] = [255, 255, 255] # hvítur
rgb.write()
```

## 5. Aðrar viðbætur sem þér dettur í hug (15%)
1. Annað sem þér dettur í hug til að betrumbæta bílinn í samráði við kennara.
---

## Námsmat og skil
- Yfirferð og námsmat á sér stað í tíma. 
- Fyrir hvern lið; gefið er heilt fyrir fullnægjandi lausn, hálft ef lausn er ábótavant, ekkert ef lausn er stórlega ábótavant eða vantar. 
- Skilaðu á Innu öllum kóðalausnum.
