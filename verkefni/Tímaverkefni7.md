# Tímaverkefni 7

- 10% af heildareinkunn
- Einstaklingsverkefni.
- Settu upp verklega.
- Passaðu að þú getir útskýrt fyrir kennara allan kóða sem þú skrifar.

---

## I<sup>2</sup>C samskipti

Kynntu þér hvernig I<sup>2</sup>C samskipti virka með því að lesa [þessa](https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/) grein. Punktar til umhugsunar meðan þú lest greinina:
- Til hvers er *Address Frame* notað?
- Hversu stór (í bitum) er Address fram og af hverju skiptir það máli?
- Hverju stjórnar *read/write bit*? 

## 128X32 Dot matrix LCD

Finndu LCD: 128X32 DOTS ([mynd hér](https://github.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/blob/master/media/2c2645e94a00867ac23e8a022f0a631a.png)) í græna boxinu þínu (ef þú átt ekki græna boxið fylgdu þá *Chapter 20 - LCD1602* í "Bókinni" sem þú finnur í Efni á Innu).

Tengingar:
1. SCL tengist í pinna 4
2. SDA tengist í pinna 5
3. V tengist í 3.3V
4. G tengist í GND

Forritasöfn (e. library) sem þarf:
1. `lcd128_32` sem þú finnur [hér](https://github.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Python/blob/master/2.%20Python_Tutorial/2.%20Python%20Projects/Project%2016：%20I2C%20128×32%20LCD/lcd128_32.py).
2. `lcd128_32_fonts` sem þú finnur [hér](https://github.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Python/blob/master/2.%20Python_Tutorial/2.%20Python%20Projects/Project%2016：%20I2C%20128×32%20LCD/lcd128_32_fonts.py).

Settu upp þennan kóða:
```python
from machine import Pin, SoftI2C
from time import sleep_ms
from lcd128_32 import lcd128_32

i2c_klukkupinni = 4
i2c_gagnapinni = 5
i2c_vistfang_lcd = 0x3f # Addressan á lcd skjánum
i2c_gagnabraut = 0

lcd = lcd128_32(i2c_gagnapinni, i2c_klukkupinni, i2c_gagnabraut, i2c_vistfang_lcd)

lcd.Clear()
lcd.Cursor(0, 6)
lcd.Display("TSKOLI")
lcd.Cursor(2, 7)
lcd.Display("VESM")
lcd.Cursor(3, 0)
lcd.Display("12345678901234567890")
```

### Verkefni 1 (10%)

Breyttu kóðanum hér að ofan þannig að skjárinn birti tvo teljara, annar teljarinn á að teljar frá 0 og upp í 20 en hinn teljarinn að telja frá 20 og niður í 0. Hafðu báða teljarana í sömu línunni. 

## MPU-6050

Mpu6050 er snúðáttaviti (e. gyro compass (hér eftir kallað gyro)), hröðunar og hitaskynjari. Lestu þér til um hann [hér](https://www.electronicwings.com/sensors-modules/mpu6050-gyroscope-accelerometer-temperature-sensor-module).

### Tengingar:
1. VCC - 3,3V
2. GND - GND
3. SCL - pin nr 4
4. SDA - pin nr 5

Annað á ekki að tengja við MPU6050

Sækið svo [þessa](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_ESP32_S3/blob/main/Python/Python_Libraries/mpu6050.py) skrá úr Freenove safninu og hlaðið upp í Thonny.

Dæmi um notkun á klasanum:
```python
from machine import Pin
from mpu6050 import MPU6050
from time import sleep_ms

mpu = MPU6050(4,5) # tengja IIC pin(sclpin,sdapin)
mpu.MPU_Init() # frumstilla MPU6050
sleep_ms(1000) # bið eftir MPU6050 virki stöðugt

gx, gy, gz = mpu.MPU_Get_Gyroscope() # sækir gildin á gíró
ax, ay, az = mpu.MPU_Get_Accelerometer() #sækir gildin á hröðuninni
```

### Verkefni 2 (10%)

Bættu skjánum hér að ofan við rásina og forritaðu þannig að bæði gyro og hröðunargildin skrifist snyrtilega á skjáinn. Bættu við breytingunum á gildunum sem sýnd var í greininni sem þú last um MPU6050. 

ATH: Það er gott að hafa smá sleep í while lykkjunni t.d. 250 ms.

### Verkefni 3 (10%)

Til að gyro hlutinn virki sem best þarf að kvarða (e. calibrate) hann. Það er gert þannig að MPU6050 er látinn liggja flatur á borði og síðan eru teknar margar (eitt þúsund að lágmarki) mælingar og meðaltal þeirra mælinga svo reiknað. Þær tölur sem koma út úr þessari aðgerð eru svo notaðar til að stilla af allar þær mælingar sem á eftir koma (draga kvörðunina frá mælingunni). Þetta þarf að gera fyrir x, y og z gildi mælinganna. Dæmi:

```python
mx, my, mz = 0, 0, 0
fjoldi_kvardana = 1000
for _ in range(fjoldi_kvardana):
    x, y, z = mpu.MPU_Get_Gyroscope()
    mx += x
    my += y
    mz += z
    sleep_us(5)

mx //= fjoldi_kvardana
my //= fjoldi_kvardana
mz //= fjoldi_kvardana

# og svo í lykkjunni
gx, gy, gz = mpu.MPU_Get_Gyroscope()
gx -= mx
gy -= my
gz -= mz
```

Bættu þessu við kóðann þinn. Breyttu svo kóðanum þannig að þú skrifir bæði út leiðréttu gyro gildin og óleiðréttu gildin úr verkefninu hér að ofan.

### Verkefni 4 (60%)

Notaðu nú þekkingu þína á gyro til að láta bílinn keyra beint. Þú getur notað Z ásinn frá gyro til að sjá hvort bíllinn er að beygja og þá brugðist við með því að breyta hraða hjólanna. Hér sýnikóði til að hjálpa þér af stað:
```python

z_sidast = 0

def afram(hradi):
    # allur kóði sem nú þegar er í áfram fallinu þínu
    
    # síðan í stað pwmA.duty(hradi) og pwmB.duty(hradi) kæmi:
    global z_sidast
    _, _, z = mpu.MPU_Get_Gyroscope()
    z /= 131
    if z == z_sidast:
        # keyra beint áfram
        pwmA.duty(hradi)
        pwmB.duty(hradi)
    elif z < z_sidast:
        # beygja til vinstri (eða hægri)
        pwmA.duty(?????)
        pwmB.duty(?????)
    else:
        # beygja til hægri (eða vinstri)
        pwmA.duty(??????)
        pwmB.duty(??????)
    
    z_sidast = z        
``` 

## ADXL345 hröðunarmælir

Kynntu þér ADXL345 hröðunarmælinn með því að lesa þessa [grein](https://how2electronics.com/interfacing-adxl345-accelerometer-with-raspberry-pi-pico/). 

### Verkefni 5 (10%)

Tengdu á eftirfarandi hátt ADXL2345 við ESP-inn:
1. GND tengist í GND
2. 5V - ÓTENGT
3. SDA tengist við pinna 5
4. SCL tengist við pinna 4
5. 3V3 tengist við 3.3V

Settu svo upp fyrri kóðann í greininni en breyttu honum þannig að í stað þess að skrifa út á skjáinn á fartölvunni þinni að þá skrifist á skjáinn úr verkefni 1 hér að ofan.

## Námsmat og skil
- Yfirferð og námsmat á sér stað í tíma. 
- Fyrir hvern lið; gefið er heilt fyrir fullnægjandi lausn, hálft ef lausn er ábótavant, ekkert ef lausn er stórlega ábótavant eða vantar. 
- Skilaðu á Innu öllum kóðalausnum.
