# ANALIZA IN PRIMERJAVA HOTELOV IZ SPLETNE STRANI BOOKING
Avtor: Mia Čakarova

Datum: 04.09.2024

## Uvod
Pri odločanju kam bi se odpravili na dopust pogosto pomembno vlogo predstavlja prenočišče. Ena najbolj znanih spletnih strani, na kateri rezerviramo nastanitev, je Booking. V tej projektni nalogi sem se odločila analizirati in primerjati izključno hotele v Amsterdamu, Splitu in Lizboni, lokacije so bile izbrane naključno. Da bi bila naloga čim bolj primerna za analizo, sem pri določanju parametrov izbrala, da iščem bivanje za dve osebi (ker je to najbolj pogosto) in samo za eno noč, saj ob izbiri več noči nekateri hoteli ponujajo popuste.

## Potrebni programi za zagon
Projekt je izdelan v VS Code, zato je ta potreben za zagon. Uporabljen je jezik Python. 
Pred uporabo naloge se mora uporabnik prepričati, da ima naloženo najnovejšo verzijo Google Chrome (povezava: https://www.google.com/chrome/) in tudi tej ustrezno različico Chrome Driverja (povezava: https://chromedriver.chromium.org/downloads). To dvoje je pomembno za pravilno delovanje knjižnice selenium. 
Poleg seleniuma je potrebno naložiti tudi knjižnice: 
- jupyter; z njim uporabnik lahko odpre t.i. notebooka 'pridobivanje_podatkov.ipynb' in 'analiza_podatkov.ipynb'
- beautifulsoup4; ta je uporabljena za črpanje želenih podatkov iz html vsebine
- pandas; z njo manipuliramo tabele
- matplotlib; tega uporabimo za risanje grafov in diagramov

Vse omenjene knjižnice mora uporabnik naložiti preko konzole v mapo, kjer bo projekt. To stori tako:

pot/do/mape> pip install ime_knjižnice

## Vodič za datoteke
V repozitoriju so vidne vse datoteke, ki sestavljajo projekt. Najprej moramo zagnati datoteko 'funkcije_za_pridobivanje_podatkov.py'. Ta vsebuje funkcijo 'potegni_hotele', ki potegne html vsebino strani in iz nje izčrpa podatke. Za tem zaženemo datoteko 'funkcije_za_csv.py'. Ta vsebuje  funkciji 'write_csv' in 'zapisi_v_csv', ki izčrpane podatke zapišeta v csv datoteko. 

Sedaj lahko funkcije uporabimo v notebooku 'pridobivanje_podatkov.ipynb'. Tu lahko uporabnik zamenja povezave v primeru, da želi primerjati druge oz. več lokacij. Ko zaženemo to datoteko, nam Python ustvari csv datoteke 'amsterdam.csv', 'split.csv' in 'lizbona.csv' (te tudi vidimo v repozitoriju).

Zdaj ko so csv datoteke pripravljene, jih lahko analiziramo. To storimo v notebooku 'analiza_podatkov.ipynb'.

Razlaga funkcij in korakov je v datotekah.

## Opombe
V repozitoriju lahko opazimo tudi datoteko .gitignore. V njej so zapisane vse datoteke, ki jih avtor ne želi deliti z uporabniki oz. ki uporabniku niso v pomoč.

Jupyter notebook 'pridobivanje_podatkov.ipynb' je ustvarjen znotraj t.i. virtualnega okolja. Zato ga mora uporabnik aktivirati:
1. Klonirajte repozitorij (preko konzole ali terminala v VS Code):

git clone https://povezava_do_repozitorija.git

cd pot_do_mape_projekta

2. Aktivirajte virtualno okolje:

python -m venv venv
source venv/bin/activate     # za Mac/Linux
venv\Scripts\activate        # za Windows

3. Namestite vse potrebne knjižnice:

pip install -r requirements.txt
