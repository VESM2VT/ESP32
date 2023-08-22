# Klasar og föll fyrir ESP

from machine import Pin
from time import sleep_ms, sleep_us, ticks_ms, ticks_diff

class SevenSeg():
    """
    SevenSeg klasinn sem um virkni SevenSegment skjásins.
    
    Tengingar (5611AB):

        G F J A B
    
        E D J C P      J = jörð = GND

         aaaa
        f    b
        f    b
        f    b
         gggg 
        e    c
        e    c
        e    c
         dddd  dp
    
    """
    def __init__(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, dp: int, common_cathode: bool = False):

        self.pinnar = [dp, g, f, e, d, c, b, a]
        self.common_cathode = common_cathode

        self.hex_tolur = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]
        if self.common_cathode: self.hex_tolur = [~h & 0xff for h in self.hex_tolur]
        self.dp_maski = 0x7f
        self.hw_pinnar = [Pin(i, Pin.OUT) for i in self.pinnar] 

    def syna_tolu(self, tala, punktur = False):

        if isinstance(tala, str):
            tala = int(tala, 16)
        for i, pinni in enumerate(self.hw_pinnar):
            pinni.value((self.hex_tolur[tala] >> (7 - i) & 1))
        self.hw_pinnar[0].value(not punktur if not self.common_cathode else punktur)

    def allt_kveikt(self):
        for pinni in self.hw_pinnar:
            pinni.value(0)

    def allt_slokkt(self):
        for pinni in self.hw_pinnar:
            pinni.value(1)
            

class FourSevenSeg():
    """
    SevenSeg klasinn sem um virkni 4 stafa SevenSegment skjásins.

    Tengingar á 3461XS

    1 A F 2 3 B

    E D P C G 4

    þar sem bókstafirnir vísa í sneiðar (e. segment) og tölurnar í tölustafina fjóra.

         aaaa
        f    b
        f    b
        f    b
         gggg 
        e    c
        e    c
        e    c
         dddd  dp
    """
    def __init__(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, dp: int, d1: int, d2: int, d3: int, d4: int, common_cathode: bool = False):
       
        self.pinnar = [dp, g, f, e, d, c, b, a]
        self.stafir = [d1, d2, d3, d4]
        self.common_cathode = common_cathode
        self.stafur_on = 1
        self.stafur_off = 0
        if self.common_cathode: self.stafur_on, self.stafur_off = self.stafur_off, self.stafur_on
        self.sneid_on, self.sneid_off = self.stafur_off, self.stafur_on # bara notað þegar allt er kveikt/slökkt -- Endurskrifa!!!!
        self.hex_tolur = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]
        if self.common_cathode: self.hex_tolur = [~h & 0xff for h in self.hex_tolur]
        self.dp_maski = 0x7f
        self.hw_pinnar = [Pin(i, Pin.OUT) for i in self.pinnar] 
        self.hw_stafir = [Pin(i, Pin.OUT) for i in self.stafir]

    def syna_tolu(self, tala: int, stafur: int, punktur: bool = False):

        if isinstance(tala, str):
            tala = int(tala, 16)
        self.allt_slokkt()
        self.hw_stafir[stafur].value(self.stafur_on) # ATH
        for i, pinni in enumerate(self.hw_pinnar):
            pinni.value((self.hex_tolur[tala] >> (7 - i) & 1))
        self.hw_pinnar[0].value(not punktur if not self.common_cathode else punktur)
        #self.hw_stafir[stafur].value(self.common_cathode)
        sleep_us(500)

    def _kveikt_slokkt(self, stafur, ljosgildi):
        pass

    def allt_kveikt(self, stafur: int = 0):
        if stafur:
            self.hw_stafir[stafur - 1].value(self.stafur_on)
        else:
            for s in self.hw_stafir:
                s.value(self.stafur_on)
            
        for pinni in self.hw_pinnar:
            pinni.value(self.sneid_on)

    def allt_slokkt(self, stafur: int = 0):
        if stafur:
            self.hw_stafir[stafur - 1].value(self.stafur_off)
        else:
            for s in self.hw_stafir:
                s.value(self.stafur_off)
            for pinni in self.hw_pinnar:
                pinni.value(self.sneid_off)

    def syna_float(self, tala: float):
        pass

    def syna_streng(self, strengur: str):
        # finna staðsetningu punkts eða punkta
        punktar = [i for i, p in enumerate(strengur) if p in(".,")]
        punktar = [i // 2 for i in punktar]
        assert len(punktar) < 2, f"{strengur} inniheldur {len(strengur)} punkta en má bara innihalda núll eða einn!!!!"
        
        for nr, stafur in enumerate(strengur):
            #self.allt_slokkt()
            #sleep_ms(1)
            self.syna_tolu(stafur, nr)
            #sleep_ms(2)
                

    def syna_int(self, tala: int):
        if tala > 9999: tala = 9999
        thusund = tala // 1000
        hundrad = (tala - thusund * 1000) // 100
        tugur = (tala - thusund * 1000 - hundrad * 100) // 10
        eining = tala - thusund * 1000 - hundrad * 100 - tugur * 10
        for i, t in enumerate([thusund, hundrad, tugur, eining]):
            #self.allt_slokkt()
            #sleep_ms(1)
            self.syna_tolu(t, i)
            #sleep_ms(2)

def varpa(gildi, inn_laggildi, inn_hagildi, ut_laggildi, ut_hagildi):
    return (gildi - inn_laggildi) * (ut_hagildi - ut_laggildi) // (inn_hagildi - inn_laggildi) + ut_laggildi

def klemma(gildi, laggildi, hagildi):
    return max(laggildi, min(gildi, hagildi))

class Sofa(): 
    def __init__(self, svefntimi=1000):
        self.svefntimi = svefntimi
        self.lidinn_timi = ticks_ms()

    def timi_lidinn(self) -> bool:
        timi_nuna = ticks_ms()
        if ticks_diff(timi_nuna, self.lidinn_timi) >= self.svefntimi:
            self.lidinn_timi = timi_nuna
            return True
        return False





