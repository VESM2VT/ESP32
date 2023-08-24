# Tímaverkefni 1
- 10% af heildareinkunn.
- Einstaklingsverkefni.
- Settu upp verklega með brauðbretti og íhlutum.
- Passaðu að þú getir útskýrt fyrir kennara allan kóða sem þú skrifar.

---

## 1. Teljari (10%)

Kynntu þér hvernig 7-Segment virkar með því að lesa [þessa grein](https://lastminuteengineers.com/seven-segment-arduino-tutorial/), lestu **að** kaflanum *Wiring a 7-Segment Display to an Arduino*.
Til umhugsunar: Hvort er þitt 7-Segment Display *common anode* eða *common cathode*? Hver er munurinn á þessu tvennu?

1. Settu [þessa](https://raw.githubusercontent.com/VESM2VT/ESP32/main/myndir/7seg.png) rás upp á brauðbretti. 
1. Settu svo þennan kóða inn (Þú finnur TSkoli safnið [hér](https://github.com/VESM2VT/ESP32/blob/main/kodi/TSkoli.py) en þú þarft að setja það inn á ESP-inn.):
    ```python
    from TSkoli import SevenSeg
    from time import sleep_ms

    COMMON_ANODE = True # Breyta í False ef þinn SevSeg er common cathode
    seg = SevenSeg(36, 35, 12, 11, 10, 37, 38, 13, COMMON_ANODE)

    teljari = 1
    while True:
        seg.syna_tolu(teljari)
        teljari += 1
        sleep_ms(1000)
    ```

---

## 2. Teningur (40%)

1. Bættu núna takka við rásina úr lið eitt og forritaðu svo tenging. Þegar ýtt er í takkann á að koma upp tala sem valin er af handahófi (e. random). Talan á svo að standa á 7-Segment skjánum þar til ýtt er aftur á takkan og þá á ný tala að birtast.

---

## 3. 7-Segment fjórir tölustafir (10%)

Kynntu þér hvernig 7-Segment með fjórum tölustöfum virkar með horfa á þetta stutta myndband [How 4 Digit 7 Segment Displays Work](https://youtu.be/fYAlE1u5rno)

1. Settu upp á brauðbretti [þessa](https://raw.githubusercontent.com/VESM2VT/ESP32/main/myndir/4sevseg.png) rás.
1. Settu svo þennan kóða inn:
   - Muna eftir TSkoli safninu.
   - Muna eftir common anode eða common cathode.
    ```python
    from TSkoli import FourSevenSeg
    from time import sleep_ms

    COMMON_ANODE = True # Breyta í False ef þinn 4SevSeg er common cathode
    seg = FourSevenSeg(40, 38, 11, 9, 8, 39, 12, 10, 35, 36, 37, 13, COMMON_ANODE)

    while True:
        seg.syna_int(1234)
    ```
1. Þetta virkar allt ágætlega en við sjáum vandamál ef við ætlum að birta aðra tölu líka á sipaðan hátt og við gerðum í teljara verkefninu hér að ofan.
1. Breyttu forritinu þannig að það verði svona:
    ```python
    from TSkoli import FourSevenSeg
    from time import sleep_ms

    COMMON_ANODE = True # Breyta í False ef þinn 4SevSeg er common cathode
    seg = FourSevenSeg(40, 38, 11, 9, 8, 39, 12, 10, 35, 36, 37, 13, COMMON_ANODE)

    teljari = 1
    while True:
        seg.syna_int(teljari)
        teljari += 1
        sleep_ms(1000)
    ```
2. Þetta virkar ekki vel. Ástæðan fyrir því er að `sleep_ms` stoppar forritið í ákveðinn tíma og við viljum ekki að forritið okkar stoppi. Við verðum því að nota einhverja aðra aðferð. Sú aðferð gengur út á að í stað þess að bíða í t.d. eina sekúndu eins og gert er hér þá spyrjum við hvort ein sekúnda er liðin frá því að við gerðu eitthvað síðast. Breittu nú forritinu þannig að það verði svona:
    ```python
    from TSkoli import FourSevenSeg
    from time import ticks_ms 
    # ticks_ms() gefur okkur fjölda millisekúnda 
    # sem liðnar efur frá því kveikt var að ESP

    COMMON_ANODE = True # Breyta í False ef þinn 4SevSeg er common cathode
    seg = FourSevenSeg(40, 38, 11, 9, 8, 39, 12, 10, 35, 36, 37, 13, COMMON_ANODE)

    bidtimi = 1000 # ætlum að bíða í 1000 msek
    timi_lidinn = 0 # tíminn sem er liðinn frá því við hækkuðum teljarann síðast

    teljari = 1
    while True:
        # skráum í breytuna hversu langt er síðan ESP ræsti
        timi_nuna = ticks_ms()
        # Ef tíminn núna að frádregnum tímanum sem við erum búin 
        # að bíða er stærri eða sama sem biðtíminn
        if (timi_nuna - timi_lidinn) >= bidtimi:
            # þá hækkum við teljarann
            teljari += 1
            # og uppfærum lidinn tíma í tímann núna
            timi_lidinn = timi_nuna
        seg.syna_int(teljari)
    ```
---

## 4. BOBA (40%)

1. Skrifaðu forrit fyrir niðurteljara sem virkar með 4 stafa 7-Segment-inu. Niðurteljarinn á að byrja á 60 sekúndum og telja niður í núll. [Sýnidæmi](https://www.youtube.com/watch?v=b7yCvvrDPSw)
1. Til að stöðva teljara þarf að klippa ákveðinn lit af vír, var það rauði eða kannski blái vírinn?
1. Ef klippt er á rangan vír þá verður niðutalningin tvöfalt hraðari. 

---

## Námsmat og skil
- Yfirferð og námsmat á sér stað í tíma. 
- Fyrir hvern lið; gefið er heilt fyrir fullnægjandi lausn, hálft ef lausn er ábótavant, ekkert ef lausn er stórlega ábótavant eða vantar. 
- Skilaðu á Innu öllum kóðalausnum.
