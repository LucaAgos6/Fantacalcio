import os
import json
import requests
import pandas as pd

from dotenv import load_dotenv


# Credenziali dell"utente
load_dotenv()
username = os.getenv("user")
password = os.getenv("password")

# URL della Login API
login_url_post = "https://apileague.fantacalcio.it/onboarding/v1/login"

# Inizializza una sessione
session = requests.Session()

# Header HTTP
headers_post = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Content-Type": "application/json",
                "App_key":"0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a"}

payload_post = {"username": username,
                "password": password}

# Effettua il login
response_post = session.post(login_url_post, headers=headers_post, data=json.dumps(payload_post))


# Inizio GET per scaricare il file del calendario
url_get = "https://leghe.fantacalcio.it/servizi/v1_legheCompetizione/excel?alias_lega=spritecalcio111&id_competizione=268324&nome_competizione=Fantascossi%207ma%20edizione"
params_get = {"alias_lega": "spritecalcio111",
              "id_competizione": "268324","nome_competizione": "Fantascossi%207ma%20edizione"}

# Headers, se il codice non funziona aggiornare Cookie o App_key
headers_get = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
               "App_key": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a",
               "Cookie": "comp_spritecalcio111_FCLeague=0=268324; FCLeague=0=DnsZTDr%2fEDsetODAs9UDRxcw%2bV9dNR8d235Swd2dZBStqhQAm2kxaZ3mTaksHxJndinCJ61p5IjO3HD%2bN%2bbHEF3eIdVpxfRx7VFd2Lab63UAXovuqvybuxOVzpE7a2Yr4sS2IN8E7eurwcp%2frEylZGj1UEdINUZ%2fk0r77%2fiPQniVp%2bfo%2fzMIU41tmYOcIKonkfnYTNreAdMOXE7RDW5Xw%2fUtR53optcQoDgR7uf7WvJsTCeHZfmuqWURiqk9KK7lRf%2bbUGvNm744IbBjGgqeIpWckcUDqlh21hecTmT6q3getSRhhBdv0v0948lA5CxIHHaG4Fuw7RbWF5xOZPqreKKMStEalA7T%2bVtnIGTupxWyMxQtVp14N3%2fajPfWOzHEfCz%2bM0pA11A%3d; AWSALB=1HCbR/a4EXinnL3g328VTz8q2L3MzXBcJLd96mS9bfmCi5iHeF3+9HxoQnYR8ZT8ujB4AZE3rCO+Y4ER1MsPin6jU+tycgJI+0tHBBWT9EPyZ+wX/EIYOj4+0Qye; AWSALBCORS=1HCbR/a4EXinnL3g328VTz8q2L3MzXBcJLd96mS9bfmCi5iHeF3+9HxoQnYR8ZT8ujB4AZE3rCO+Y4ER1MsPin6jU+tycgJI+0tHBBWT9EPyZ+wX/EIYOj4+0Qye"}

# Effettua la richiesta GET
response_get = requests.get(url_get, params=params_get, headers=headers_get)

# Controlla lo stato della risposta
if response_get.status_code == 200:
    print("Richiesta effettuata con successo!")
    # Salva il contenuto in un file, se necessario
    with open("Input/Calendario_Fantascossi.xlsx", "wb") as file:
        file.write(response_get.content)
    print("File salvato come Input/Calendario_Fantascossi.xlsx")
else:
    print(f"Errore nella richiesta: {response_get.status_code}")
    print(f"Dettagli: {response_get.text}")


# Inizio GET per scaricare il file delle giornate
for i in range(38):
    url_get = f"https://leghe.fantacalcio.it/servizi/V1_LegheFormazioni/excel?alias_lega=spritecalcio111&id_competizione=268324&giornata={i+1}&nome_competizione=spritecalcio111&dummy=5"
    params_get = {"alias_lega": "spritecalcio111",
                "id_competizione": "268324","nome_competizione": "Fantascossi%207ma%20edizione"}

    # Headers, se il codice non funziona aggiornare Cookie o App_key
    headers_get = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "App_key": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a",
                "Cookie": "comp_spritecalcio111_FCLeague=0=268324; FCLeague=0=DnsZTDr%2fEDsetODAs9UDRxcw%2bV9dNR8d235Swd2dZBStqhQAm2kxaZ3mTaksHxJndinCJ61p5IjO3HD%2bN%2bbHEF3eIdVpxfRx7VFd2Lab63UAXovuqvybuxOVzpE7a2Yr4sS2IN8E7eurwcp%2frEylZGj1UEdINUZ%2fk0r77%2fiPQniVp%2bfo%2fzMIU41tmYOcIKonkfnYTNreAdMOXE7RDW5Xw%2fUtR53optcQoDgR7uf7WvJsTCeHZfmuqWURiqk9KK7lRf%2bbUGvNm744IbBjGgqeIpWckcUDqlh21hecTmT6q3getSRhhBdv0v0948lA5CxIHHaG4Fuw7RbWF5xOZPqreKKMStEalA7T%2bVtnIGTupxWyMxQtVp14N3%2fajPfWOzHEfCz%2bM0pA11A%3d; AWSALB=1HCbR/a4EXinnL3g328VTz8q2L3MzXBcJLd96mS9bfmCi5iHeF3+9HxoQnYR8ZT8ujB4AZE3rCO+Y4ER1MsPin6jU+tycgJI+0tHBBWT9EPyZ+wX/EIYOj4+0Qye; AWSALBCORS=1HCbR/a4EXinnL3g328VTz8q2L3MzXBcJLd96mS9bfmCi5iHeF3+9HxoQnYR8ZT8ujB4AZE3rCO+Y4ER1MsPin6jU+tycgJI+0tHBBWT9EPyZ+wX/EIYOj4+0Qye"}

    # Effettua la richiesta GET
    response_get = requests.get(url_get, params=params_get, headers=headers_get)

    # Controlla lo stato della risposta
    if response_get.status_code == 200:

        # Verifica il contenuto della cella A1 (prima riga, prima colonna)
        df = pd.read_excel(response_get.content, header=None)
        if df.iloc[0, 0] == "File non disponibile.":
            break
        else:
            # Salva il contenuto in un file, se necessario
            with open(f"Input/Giornate/Formazioni_spritecalcio111_{i+1}_giornata.xlsx", "wb") as file:
                file.write(response_get.content)
            print(f"File salvato come Input/Giornate/Formazioni_spritecalcio111_{i+1}_giornata.xlsx")
    else:
        print(f"Errore nella richiesta: {response_get.status_code}")
        print(f"Dettagli: {response_get.text}")
