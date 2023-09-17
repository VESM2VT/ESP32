# Tímaverkefni 6

- 10% af heildareinkunn
- einstaklingsverkefni

---

### Fjarstýring fyrir bíl 
Hannaðu fjarstýringu fyrir bílinn (snúra og þráðlaus möguleiki). Notaðu forrit TinkerCad fyrir 3D prentun. Fjarstýring þarf að vera **rúnuð**, falla vel að höndum og rými þarf að vera vel skipulagt og með lokun. Sýnidæmi [Gamepad](https://www.youtube.com/watch?v=JCrsFxdJXu8)
<!-- [Nunchuck](https://en.wikipedia.org/wiki/Wii_Remote#Nunchuk) -->

#### Íhlutir sem þurfa að vera í fjarstýringunni:
- ESP32-S3
- Rafhlöðuvagga fyrir 18650 rafhlöðu + 18650 rafhlaða
- [Toggle switch](https://ae01.alicdn.com/kf/HTB1m0C1SXXXXXcGXpXXq6xXFXXXc/JOYING-LIANG-SS-12F30-Black-Small-Toggle-Switch-Toy-Switches.jpg) til að kveikja/slökkva á Arduino Nano.
- takka til að kveikja/slökkva á lögguljósum.
- [Stýripinna](https://lastminuteengineers.com/joystick-interfacing-arduino-processing/) sem þarf að aðlaga að fjarstýringu:
    - hýsing fyrir stýripinna [(glært box)](https://www.thingiverse.com/thing:1162200)
    - hýsing fyrir stýripinna Keyestudio [(grænt box)](https://github.com/VESM2VT/Efni/blob/main/Myndir/Fjarstyring.stl). 
- Lítið breadboard fyrir tengingar á GND og 3V.
- Lokið er 3mm á þykkt og skorið út í plexigler, aftan á fjarstýringu og fellt inn.

[Hér](https://github.com/VESM2VT/ESP32/blob/main/myndir/fjarstyring_h23.png) er mynd sem sýnir hvaða íhlutir eiga að vera í fjarstýringunni og hvernig þeir tengjast saman. 

<!--  [MPU-6050 (gyro)](https://lastminuteengineers.com/mpu6050-accel-gyro-arduino-tutorial/) -->
<!-- Toggle switch](https://www.switchelectronics.co.uk/on-off-spst-toggle-switch-250v-ac-15a) -->

#### Fjarstýring þarf að geta framkvæmt amk. eftirfarandi aðgerðir:
- Hraðastilling (hratt, hægt, stopp)
- Beygja til hægri og vinstri 
- Fara áfram, stoppa, bakka.
- slökkva/kveikja á ESP32-S3 (switch takki).
- takki fyrir aðra virkni t.d. kveikja á ljósum eða flauta.

---

### Námsmat og skil
- 60% fyrir grunnhönnun á fjarstýringu (að fylgja eftir kennara).
- 20% aukalega fyrir að gera fjartýringu rúnaða og falla vel að höndum.
- 20% aukalega að láta lokið falla vel inní fjarstýringu.  
- Dregið er niður um 20% fyrir hvern hönnunargalla.
- Skilaðu á Innu fjarstýringu á STL sniðmáti ásamt lengd x breidd á lokinu (plexigler) í athugasemd.
