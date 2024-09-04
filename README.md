# ANALIZA IN PRIMERJAVA HOTELOV IZ SPLETNE STRANI BOOKING

## Uvod
Pri odločanju kam bi se odpravili na dopust pogosto pomembno vlogo predstavlja prenočišče. Ena najbolj znanih spletnih strani, na kateri rezerviramo nastanitev, je Booking. V tej projektni nalogi sem se odločila analizirati in primerjati izključno hotele v Amsterdamu, Splitu in Lizboni, lokacije so bile izbrane naključno. Da bi bila naloga čim bolj primerna za analizo, sem pri določanju parametrov izbrala, da iščem bivanje za dve osebi (ker je to najbolj pogosto) in samo za eno noč, saj ob izbiri več noči nekateri hoteli ponujajo popuste.

## Potrebni programi za zagon
Projekt je izdelan v VS Code (v nadaljevanju VSC), zato je ta potreben za zagon. Uporabljen je jezik Python. 
Pred uporabo naloge se mora uporabnik prepričati, da ima naloženo najnovejšo verzijo Google Chrome (povezava: https://www.google.com/chrome/) in tudi tej ustrezno različico Chrome Driverja (povezava: https://chromedriver.chromium.org/downloads). To dvoje je pomembno za pravilno delovanje knjižnice Selenium. 
Potrebno je tudi naložiti knjižnice:
-jupyter; z njim uporabnik lahko odpre t.i. notebooka 'pridobivanje_podatkov.ipynb' in 'analiza_podatkov.ipynb'
-beautifulsoup4; ta je uporabljena za črpanje želenih podatkov iz html vsebine
-pandas; z njo manipuliramo tabele
-matplotlib; tega uporabimo za risanje grafov in diagramov