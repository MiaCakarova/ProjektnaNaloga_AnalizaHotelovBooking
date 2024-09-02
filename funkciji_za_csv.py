# Po obdelavi podatkov jih bomo shranili v .csv datoteke, da bodo bolj pregledni in da jih bo lažje analizirati.
# Pri tem bomo potrebovali paketa 'os' in 'csv'.
import csv
import os

# Definirajmo funkcijo, ki bo v csv datoteko vnesla podatke z imeni stolpcev 'fieldnames' in vrednostmi iz 'rows'.
# Datoteko csv bo poimenovala 'filename' in jo shranila v mapo 'directory'.
def write_csv(fieldnames, rows, directory, filename):
    if directory != "":
        os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return


# Spodnja funkcija bo ustvarila csv datoteko iz seznama 'oglasi'. Funkcija bo predpostavila, da so ključi vseh slovarjev seznama 'oglasi' enaki in 
# da je ta seznam neprazen.
def zapisi_v_csv(oglasi, directory, filename):
    assert oglasi and (all(j.keys() == oglasi[0].keys() for j in oglasi))
    fieldnames = ['lokacija', 'ime', 'cena', 'ocena gostov', 'število zvezdic']
    
    write_csv(fieldnames, oglasi, directory, filename)