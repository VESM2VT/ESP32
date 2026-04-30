## 3. Fjarstýring - Stýrt með hröðunarmæli (10%)

[Mpu6050](https://www.electronicwings.com/storage/PlatformSection/TopicContent/138/icon/MPU6050.jpg) er hröðunarskynjari o.fl. Lestu þér til um hann [hér](https://www.electronicwings.com/sensors-modules/mpu6050-gyroscope-accelerometer-temperature-sensor-module).

### Tengingar.
1. VCC - 3,3V
2. GND - GND
3. SCL - pin nr 16
4. SDA - pin nr 17

Annað á ekki að tengja við MPU6050

Sækið svo skrárnar [imu.py](https://github.com/micropython-IMU/micropython-mpu9x50/blob/master/imu.py) og [vector3d.py](https://github.com/micropython-IMU/micropython-mpu9x50/blob/master/vector3d.py) og hlaðið upp á ESP-inn með Thonny.


Dæmi um notkun á klasanum:
```python
from machine import Pin, I2C
from imu import MPU6050
from time import sleep_ms

i2c_mpu = I2C(sda=Pin(17), scl=Pin(16), freq=400000)
mpu = MPU6050(i2c_mpu)

while True:
    # Hröðun (e. acceleration)
    ax, ay, az = mpu.accel.xyz # skilar hröðuninni sem gildum á milli -1 og 1
    print(f"x: {ax}, y: {ay}, z: {az}")

    # Annað slagið "frýs" MPU-6050 og lýsir það sér þannig 
    # að öll gildin verða 0. Þá þarf að endurræsa MPU-6050
    if ax == ay == az:
        print("Endrræsi MPU-6050")
        mpu = MPU6050(i2c_mpu)

    sleep_ms(100) # gott að hafa smá sleep milli mælinga
```
Keyrðu kóðann hér að ofan í Thonny. Opnaðu Plotter-inn í Thonny (View -> Plotter) og skoðaðu hvernig gildin á x, y og z breytast þegar þú hreyfir MPU6050. 

1. Forritaðu þannig að hröðunargildin eru notuð með fjarstýringunni til að stýra bílnum. 
1. Forritaðu skottakkann á stýripinnnanum þannig að hann virkjar/afvirkjar MPU6050 stýringu (í staðinn fyrir stýripinna).

**Ath:** Það er gott að hafa smá sleep í while lykkjunni t.d. 50 ms.
