# AI IoT Kunskapskontroll 2: Intelligent Klimatkontroll 🌡️

[cite_start]Detta projekt är en del av kursen **AI IoT** och syftar till att modellera ett komplett IoT-flöde från lokal datainsamling via sensorer till molnbaserad kommunikation, lagring och prediktiv analys med Machine Learning.

## 📋 Projektöversikt
Målet med projektet är att skapa ett intelligent system för rumsoptimering. [cite_start]Genom att mäta temperatur och luftfuktighet tränas en AI-modell för att förutsäga när en fläkt eller klimatanläggning behöver startas (förkonditionering) för att hålla rummet inom optimala gränser[cite: 49, 51].

**Målvärden för rumsklimat:**
* **Temperatur:** $20^{\circ}C$ till $23^{\circ}C$
* **Luftfuktighet:** $< 60\%$

---

## 🛠️ Systemarkitektur & Material
[cite_start]Systemet följer ett strukturerat IoT-flöde[cite: 35]:
1. [cite_start]**Edge-enhet:** Raspberry Pi Pico W[cite: 37].
2. [cite_start]**Programmering:** MicroPython[cite: 38].
3. [cite_start]**Kommunikation:** MQTT-protokollet via **HiveMQ Cloud** (Broker)[cite: 46].
4. [cite_start]**Lagring:** Python-script (Subscriber) som lagrar data i en **CSV-fil**[cite: 47].
5. [cite_start]**Analys:** AI-modellering utförd i VSCode[cite: 18].

### [cite_start]Komponentlista [cite: 33]
* 1x Raspberry Pi Pico W
* 1x Temperature & Humidity Module (DHT11/22)
* 1x RGB LED Module (för visuell status)
* 1x Large Microphone Module (användes i testfas)
* Kopplingsdäck (Breadboard) och Jumperkablar

---

## 🚀 Implementering

### 1. Datainsamling (Edge)
[cite_start]Inledningsvis genomfördes funktionstester för att säkerställa hårdvarans funktionalitet, inklusive "Hello World" (blinkande LED) och styrning av RGB-modulen[cite: 39]. 

För huvuduppgiften samlas data in med en **granularitet på varannan sekund**, med datum och tid, temperatur och luftfuktighet samt en klassificering (temp_status).  

### 2. EDA & Affärslogik
Den insamlade datan kategoriseras enligt följande regler:

**Temperaturkontroll:**
* $T < 20$ $\rightarrow$ Mode: `heat`
* $T > 23$ $\rightarrow$ Mode: `cool`
* $20 \le T \le 23$ $\rightarrow$ Mode: `off`

**Luftfuktighetskontroll:**
* $H > 60$ $\rightarrow$ Drymode: `on`
* $H \le 60$ $\rightarrow$ Drymode: `off`

### 3. AI-analys & Prediktion
[cite_start]För att förutse behovet av förkonditionering används en **RandomForest-modell**[cite: 49].
* **Data Augmentation:** Insamlade data har utökats för att ge modellen ett bredare träningsunderlag.
* [cite_start]**Mål:** Identifiera mönster i temperaturfall/stigning för att aktivera fläkt/värme innan gränsvärdena nås[cite: 57].

---

## 📊 Resultat & Visualisering
Resultatet presenteras i en BI-lösning/Dashboard med:
* [cite_start]Visualisering av insamlade data[cite: 55].
* [cite_start]Prediktioner från AI-modellen som visar när systemet bör agera proaktivt[cite: 56].

---

## 📂 Filstruktur i Repository
* `/src` - Koden för uppgiften.
* [cite_start]`/data` - Insamlad data i CSV-format[cite: 6].
* `/model` - Tränad RandomForest-modell och AI-script.
* `README.md` - Denna projektrapport.

[cite_start]**IoT-eliten:** Elin Molvig, My Tistelberg, Linus Staffas och Michael Broström [cite: 3]
**Datum:** 21 april 2026