from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import re


# Da ne bi naenkrat nalagali prevelike vsebine, lahko HTML razdelimo na več delov, ki morajo biti disjunktni 
# (t.j. noben oglas se ne sme pojaviti v več delih). En takih filtrov, ki ga lahko uporabimo je število zvezdic, saj ne more en hotel imeti 
# različno število zvezdic. Ravno zaradi tega razloga smo na začetku definirali URL-je s hoteli z različnim številom zvezdic.
# Ker pa bomo primerjali hotele tudi po drugih lokacijah, bomo med kategorije dodali tudi lokacijo.

# Funkcija bo zato kot argumente sprejela URL, število zvezdic hotelov in lokacijo.
def potegni_hotele(url, zvezdice, lokacija):

    chrome_options = Options()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get(url)

    # Pomaknimo se na dno strani
    for _ in range(30):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1) # Počakamo 1 sekundo da se podatki naložijo


    # Poskusimo poiskati gumb "Naloži več rezultatov"
    try:
        button = driver.find_element(
            By.XPATH, "//button[@class='dba1b3bddf e99c25fd33 ea757ee64b f1c8772a7d ea220f5cdc f870aa1234']"
        )
        button.click() # Kliknemo na gumb
    except Exception:
        # Če gumb ni prisoten (kar se zgodi, ko je oglasov dovolj za na eno stran), ga preskočimo. Funkcija naj izpiše 'Gumba ni'.
        print("Gumba ni")
        
    time.sleep(5)
    

# Ko je vse naloženo, lahko potegnemo HTML vsebino
    html_vsebina = driver.page_source 

    driver.quit()

    # HTML kodo bomo obdelali z BeautifulSoup
    soup = BeautifulSoup(html_vsebina, 'html.parser')

    # V tem primeru smo se odločili, da nas zanimajo cene, ocene gostov ter število zvezdic hotelov. 
    # Na spletni strani od Bookinga si lahko s pomočjo orodja 'inspect' ogledamo HTML vsebino in pogledamo kako so elementi strukturirani. Običajno so
    # z obeh strani obdani s posebnimi 'oznakami' (npr. <div>, <span>), vmes pa je zapisana enolična koda oz. atribut, ki identificira določeno lastnost.
    # Ko najdemo in razpoznamo strukture elementov, jih povemu Pythonu, da bo lahko iz njih izluščil potrebne informacije.
    naslovi_struktura = soup.select('div[data-testid="title"]')
    cene_struktura = soup.select('span[data-testid="price-and-discounted-price"]')
    ocene_struktura = soup.select('div[data-testid="review-score"]')

    # Ustvarimo prazen seznam za shranjevanje lastnosti hotelov
    hoteli = []



# Z zanko se sprehodimo po hotelih in si zapisujemo njihove lastnosti
    for i in range(len(naslovi_struktura)):
        hotel_ime = naslovi_struktura[i].text
        hotel_cena = cene_struktura[i].text.strip().replace('\xa0', ' ')
        hotel_ocena = ocene_struktura[i].text
    
        # Ocena se pokaže malo drugače kot želeno, zato jo izluščimo
        vzorec = r'(\d),(\d)'
        match = re.search(vzorec, hotel_ocena)
        if match:
            hotel_ocena = f"{match.group(1)},{match.group(2)}"
        else:
            hotel_ocena = "Ni ocene"


        # Elementi seznama bodo slovarji, katerih ključi bodo kategorije
        hoteli.append({'lokacija': lokacija, 'ime': hotel_ime, 'cena': hotel_cena, 'ocena gostov': hotel_ocena, 'število zvezdic': zvezdice})


    return hoteli