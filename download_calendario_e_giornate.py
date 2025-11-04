import os
import io
import json
import requests
import pandas as pd

from dotenv import load_dotenv


# Credenziali dell"utente
load_dotenv()
username = os.getenv("user")
password = os.getenv("password")
payload_post = {"username": username, "password": password}

# Variabili da cambiare ogni anno
id_comp = "329184"
nome_comp = "FantaRotary"
alias_lega = "spritecalcio111"
app_key = "bZ2FAQDZYYBVEehhFuM9pAsJ3waL0Vsg"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
# Cambiare anche i cookie negli header GET se il codice non funziona

# URL della Login API
login_url_post = "https://apileague.fantacalcio.it/onboarding/v1/login"

# Inizializza una sessione
session = requests.Session()

# Header HTTP
headers_post = {"User-Agent": user_agent,
                "Content-Type": "application/json",
                "App_key": app_key}


# Effettua il login
response_post = session.post(login_url_post, headers=headers_post, data=json.dumps(payload_post))


# Inizio GET per scaricare il file del calendario
url_get = f"https://leghe.fantacalcio.it/servizi/v1_legheCompetizione/excel?alias_lega={alias_lega}&id_competizione={id_comp}&nome_competizione={nome_comp}"
params_get = {"alias_lega": alias_lega, "id_competizione": id_comp, "nome_competizione": nome_comp}

# Headers, se il codice non funziona aggiornare Cookie o App_key
headers_get = {"User-Agent": user_agent,
               "App_key": app_key,
               # "Cookie": f"comp_{alias_lega}_FCLeague=0={id_comp}; FCLeague=0=DnsZTDr%2fEDsetODAs9UDRxcw%2bV9dNR8d235Swd2dZBStqhQAm2kxaZ3mTaksHxJndinCJ61p5IjO3HD%2bN%2bbHEF3eIdVpxfRx7VFd2Lab63UAXovuqvybuxOVzpE7a2Yr4sS2IN8E7eurwcp%2frEylZGj1UEdINUZ%2fk0r77%2fiPQniVp%2bfo%2fzMIU41tmYOcIKonkfnYTNreAdMOXE7RDW5Xw%2fUtR53optcQoDgR7uf7WvJsTCeHZfmuqWURiqk9KK7lRf%2bbUGvNm744IbBjGgqeIpWckcUDqlh21hecTmT6q3getSRhhBdv0v0948lA5CxIHHaG4Fuw7RbWF5xOZPqreKKMStEalA7T%2bVtnIGTupxWyMxQtVp14N3%2fajPfWOzHEfCz%2bM0pA11A%3d; AWSALB=1HCbR/a4EXinnL3g328VTz8q2L3MzXBcJLd96mS9bfmCi5iHeF3+9HxoQnYR8ZT8ujB4AZE3rCO+Y4ER1MsPin6jU+tycgJI+0tHBBWT9EPyZ+wX/EIYOj4+0Qye; AWSALBCORS=1HCbR/a4EXinnL3g328VTz8q2L3MzXBcJLd96mS9bfmCi5iHeF3+9HxoQnYR8ZT8ujB4AZE3rCO+Y4ER1MsPin6jU+tycgJI+0tHBBWT9EPyZ+wX/EIYOj4+0Qye",
               "Cookie": "cacheid=1717661202309.54108088919057451; tncid=90dec360-5279-4b93-aec4-8b243e9ab082; _scor_uid=464166d3eb704522976d29a0f8cec349; _ga=GA1.1.1939762914.1754578855; _ga_KVFYCX9ZTZ=GS2.1.s1757431063$o7$g1$t1757432322$j60$l0$h0; euconsent-v2=CQYqYUAQYqYUAFgAGAITB-FsAP_gAAAAABCYLotR_G__bXlr-b736ftkeYxf9_hr7sQxBgbJk24FzLvW_JwX32E7NAzatqYKmRIAu3TBIQNlHJDURVCgKIgVrzDMaEyUoTtKJ6BkiFMRY2NYCFxvm4pjeQCY5vr99ld9mR-N7dr82dzyy6hnv3a9_-S1WJCdIYetDfv8ZBKT-9IE9_x8v4v4_N7pE2-eS1n_tGvp6j9-Yvv_dBnx9_baffzPn__rl_e7X__f_n37v943X77_____f_-7__4LowAACgkAGAAILohoAMAAQXREQAYAAguiKgAwABBdEZABgACC6I6ADAAEF0SEAGAAILokoAMAAQXRKQAYAAguiWgAwABBdEAA.f_wAAAAAAAAA; pubtech-cmp-pcstring=0-111; comp_spritecalcio111_FCLeague2025=0=329184; FCLeague2025=0=DnsZTDr%2fEDsetODAs9UDRxcw%2bV9dNR8d235Swd2dZBStqhQAm2kxaZsXseOYYqmdfYcC5ImN8S54Q27%2bwZqwrtuulwplJ920uty0EKSHbY4Pie7dyiMxV5kjWQ8jWcdXe25h6bQ5W86pgVDPREeVvForzcfLxRYkXWupRRPjhMJ0Ez%2bkpS7vpppJu6iteLQ9WsXRTL7XhOUOXE7RDW5Xw%2fUtR53optcQoDgR7uf7WvJsTCeHZfmuqWURiqk9KK7lRf%2bbUGvNm744IbBjGgqeIpWckcUDqlh21hecTmT6q3getSRhhBdv0v0948lA5CxIHHaG4Fuw7RbWF5xOZPqreKKMStEalA7T%2bVtnIGTupxUF8qlNU0tNkbXX7uZj7CtFxtm8ANC2klsdVEysW%2bnWvMNDf6OKlN4WzVI4%2bqdNt35r87Nir4obqQ%3d%3d; comp_fantamantraciube_FCLeague2025=0=620451; _ga_DVR9V968VW=GS2.1.s1762263754$o19$g1$t1762265157$j59$l0$h0; cto_bundle=sU9kPF9hdFdQRDZ0a01LVWpzVjdnbzNkMjZzZzZCQ2Z3UE1Dd0lRamdlJTJGMm5jZXIlMkJ5UmJ2QlJqeklLMUtjUmxMNCUyQmRQQVRCekslMkJTdUZ0N09YbFNHaGhHMERJciUyQlA4V2xYeDhob0JBUW5yS2pBaXZKRWNIVEJHam5ZZCUyQjAxZkJVUjJLeXhEeXdSMFdtd0p5VzN3Zlc2TTFvaHVMMHFCeWQ0QzBDam5RNVJ2ZkJLellKc0EwaWkwNlZuNUhUaGVHJTJCemNPQkdaSFolMkYlMkJtVEFaUVg0TU92eG44eHpqZ3pNd01UUzU4bzclMkZwQXBkRGlhZ1k4c3p5MWpUbWhVc29pU3oxdTd1YWI2Y0Z5RzZibjFWT0Q0N1RTbUE5JTJCYkElM0QlM0Q; AWSALB=vz0FaLsWoTCgV52Bw/dElkvlGt/RKwoZ/sD0uUP9gQxG43XE9HHRz/IWu7zqVcQje1uCXz+WNKtB6aDgZbFJmlbLcm3c1dXWVouGYINAM23pxcoujPa39J3bf/Ua; AWSALBCORS=vz0FaLsWoTCgV52Bw/dElkvlGt/RKwoZ/sD0uUP9gQxG43XE9HHRz/IWu7zqVcQje1uCXz+WNKtB6aDgZbFJmlbLcm3c1dXWVouGYINAM23pxcoujPa39J3bf/Ua"}

# Effettua la richiesta GET
response_get = requests.get(url_get, params=params_get, headers=headers_get)

# Controlla lo stato della risposta
if response_get.status_code == 200:
    print("Richiesta effettuata con successo!")
    # Salva il contenuto in un file, se necessario
    with open(f"Input/Calendario_{nome_comp}.xlsx", "wb") as file:
        file.write(response_get.content)
    print(f"File salvato come Input/Calendario_{nome_comp}.xlsx")
else:
    print(f"Errore nella richiesta: {response_get.status_code}")
    print(f"Dettagli: {response_get.text}")


# Inizio GET per scaricare il file delle giornate
for i in range(38):
    url_get = f"https://leghe.fantacalcio.it/servizi/V1_LegheFormazioni/excel?alias_lega={alias_lega}&id_competizione={id_comp}&giornata={i+1}&nome_competizione={nome_comp}&dummy=5"
    params_get = {"alias_lega": alias_lega, "id_competizione": id_comp, "nome_competizione": nome_comp}

    # Headers, se il codice non funziona aggiornare Cookie o App_key
    headers_get = {"User-Agent": user_agent,
                   "App_key": app_key,
                   "Cookie": "cacheid=1717661202309.54108088919057451; tncid=90dec360-5279-4b93-aec4-8b243e9ab082; _scor_uid=464166d3eb704522976d29a0f8cec349; _ga=GA1.1.1939762914.1754578855; _ga_KVFYCX9ZTZ=GS2.1.s1757431063$o7$g1$t1757432322$j60$l0$h0; euconsent-v2=CQYqYUAQYqYUAFgAGAITB-FsAP_gAAAAABCYLotR_G__bXlr-b736ftkeYxf9_hr7sQxBgbJk24FzLvW_JwX32E7NAzatqYKmRIAu3TBIQNlHJDURVCgKIgVrzDMaEyUoTtKJ6BkiFMRY2NYCFxvm4pjeQCY5vr99ld9mR-N7dr82dzyy6hnv3a9_-S1WJCdIYetDfv8ZBKT-9IE9_x8v4v4_N7pE2-eS1n_tGvp6j9-Yvv_dBnx9_baffzPn__rl_e7X__f_n37v943X77_____f_-7__4LowAACgkAGAAILohoAMAAQXREQAYAAguiKgAwABBdEZABgACC6I6ADAAEF0SEAGAAILokoAMAAQXRKQAYAAguiWgAwABBdEAA.f_wAAAAAAAAA; pubtech-cmp-pcstring=0-111; comp_spritecalcio111_FCLeague2025=0=329184; comp_fantamantraciube_FCLeague2025=0=620451; cto_bundle=sU9kPF9hdFdQRDZ0a01LVWpzVjdnbzNkMjZzZzZCQ2Z3UE1Dd0lRamdlJTJGMm5jZXIlMkJ5UmJ2QlJqeklLMUtjUmxMNCUyQmRQQVRCekslMkJTdUZ0N09YbFNHaGhHMERJciUyQlA4V2xYeDhob0JBUW5yS2pBaXZKRWNIVEJHam5ZZCUyQjAxZkJVUjJLeXhEeXdSMFdtd0p5VzN3Zlc2TTFvaHVMMHFCeWQ0QzBDam5RNVJ2ZkJLellKc0EwaWkwNlZuNUhUaGVHJTJCemNPQkdaSFolMkYlMkJtVEFaUVg0TU92eG44eHpqZ3pNd01UUzU4bzclMkZwQXBkRGlhZ1k4c3p5MWpUbWhVc29pU3oxdTd1YWI2Y0Z5RzZibjFWT0Q0N1RTbUE5JTJCYkElM0QlM0Q; FCLeague2025=0=DnsZTDr%2fEDsetODAs9UDRxcw%2bV9dNR8d235Swd2dZBStqhQAm2kxaZsXseOYYqmdfYcC5ImN8S54Q27%2bwZqwrtuulwplJ920uty0EKSHbY4Pie7dyiMxV5kjWQ8jWcdXe25h6bQ5W86pgVDPREeVvForzcfLxRYkXWupRRPjhMJ0Ez%2bkpS7vpoddFX8bo5SCbtcAvFOofxAOXE7RDW5Xw%2fUtR53optcQoDgR7uf7WvJsTCeHZfmuqWURiqk9KK7lRf%2bbUGvNm744IbBjGgqeIpWckcUDqlh21hecTmT6q3getSRhhBdv0v0948lA5CxIHHaG4Fuw7RbWF5xOZPqreKKMStEalA7T%2bVtnIGTupxUF8qlNU0tNkbXX7uZj7CtFxtm8ANC2klsdVEysW%2bnWvMNDf6OKlN4WzVI4%2bqdNt35r87Nir4obqQ%3d%3d; _ga_DVR9V968VW=GS2.1.s1762267310$o20$g1$t1762267316$j54$l0$h0; AWSALB=bjmmhmUgpRfTeVXDb0STwrQozDJS/dMiFoRR4L76XGC7U1V95ZdxO/fa6H5VGk6/9EB1oCJqWTbt/EG+hHpo8bU8IRntIXd1xhRd1/zeK3ZSraA/jPlG7AMcGhrZ; AWSALBCORS=bjmmhmUgpRfTeVXDb0STwrQozDJS/dMiFoRR4L76XGC7U1V95ZdxO/fa6H5VGk6/9EB1oCJqWTbt/EG+hHpo8bU8IRntIXd1xhRd1/zeK3ZSraA/jPlG7AMcGhrZ"}

    # Effettua la richiesta GET
    response_get = requests.get(url_get, params=params_get, headers=headers_get)

    # Controlla lo stato della risposta
    if response_get.status_code == 200:

        df = pd.read_excel(io.BytesIO(response_get.content), header=None)
        # Verifica il contenuto della cella A1 (prima riga, prima colonna)
        if df.iloc[0, 0] == "File non disponibile.":
            break
        else:
            # Salva il contenuto in un file, se necessario
            file_path = f"Input/Giornate/Formazioni_{alias_lega}_{i+1}_giornata.xlsx"
            if not os.path.exists(file_path):
                with open(file_path, "wb") as file:
                    file.write(response_get.content)
                print(f"File salvato: {file_path}")
            else:
                print(f"Il file esiste già: {file_path}")
    else:
        print(f"Errore nella richiesta: {response_get.status_code}")
        print(f"Dettagli: {response_get.text}")
