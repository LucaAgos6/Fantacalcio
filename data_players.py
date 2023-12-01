import os
import subprocess
import pandas as pd

from plot_tabelle import plot_tabelle_giocatori_squadre, plot_tabelle_moduli
from plot_tabelle import plot_tabelle_bonus_ruoli, plot_tabelle_modificatore
from plot_tabelle import plot_tabelle_migliori_giocatori

# Import automatico dei file

# Conta il numero di file salvati nella cartella Giornate
giornate = len([f for f in os.listdir("Input/Giornate")
                if os.path.isfile(os.path.join("Input/Giornate", f))])
competizione = "spritecalcio111"
player_name = ["LA FAXIO",
               "FC EL TORO",
               "SPAL LETTI",
               "HOFFENHEIMER",
               "LA PACCO GANG",
               "PANITA TRADITORE",
               "NEWCASTELLETTO UTD",
               "??ANKONDORICACIVITASFIDEI??"]
ruoli = ["P", "D", "C", "A"]
lista_voti = []
lista_punti_modificatore = []
print()

# Restituisce NomePlayer, Ruolo, Nome, Squadra, Voto e Fantavoto del giocatore
def player(row, df, i, n, gior):
    return [gior, row[n], df.iloc[i][n],
            df.iloc[i][n+1], df.iloc[i][n+2].lower(),
            df.iloc[i][n+3], df.iloc[i][n+4]]

# Crea il Dataframe di tutti i dati tabellari
for gior in range(1, giornate+1):

    df = pd.read_excel(
        f"Input\Giornate\Formazioni_{competizione}_{gior}_giornata.xlsx")
    print(f"Input\Giornate\Formazioni_{competizione}_{gior}_giornata.xlsx")

    for i, row in df.iterrows():

        # Salva in una lista Giornata, NomePlayer, Ruolo, Nome, Squadra, Voto e Fantavoto del centrocampista
        # Voti Fantagiocatore di sinistra
        if row[0] in player_name:

            for p in range(2, 13):
                if df.iloc[i+p][3] != "-" and df.iloc[i+p][0] in ruoli:
                    lista_voti.append(player(row, df, i+p, 0, gior))
                elif df.iloc[i+p][0] == "P":
                    if df.iloc[i+14][3] != "-":
                        lista_voti.append(player(row, df, i+14, 0, gior))
                    elif df.iloc[i+15][3] != "-":
                        lista_voti.append(player(row, df, i+15, 0, gior))
                    else:
                        lista_voti.append([gior, row[0], "P", "-", "-", 0, 0])
                elif df.iloc[i+p][0] == "D":
                    if df.iloc[i+16][3] != "-" and player(row, df, i+16, 0, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+16, 0, gior))
                    elif df.iloc[i+17][3] != "-" and player(row, df, i+17, 0, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+17, 0, gior))
                    else:
                        lista_voti.append([gior, row[0], "D", "-", "-", 0, 0])
                elif df.iloc[i+p][0] == "C":
                    if df.iloc[i+18][3] != "-" and player(row, df, i+18, 0, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+18, 0, gior))
                    elif df.iloc[i+19][3] != "-" and player(row, df, i+19, 0, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+19, 0, gior))
                    else:
                        lista_voti.append([gior, row[0], "C", "-", "-", 0, 0])
                elif df.iloc[i+p][0] == "A":
                    if df.iloc[i+20][3] != "-" and player(row, df, i+20, 0, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+20, 0, gior))
                    elif df.iloc[i+21][3] != "-" and player(row, df, i+21, 0, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+21, 0, gior))
                    else:
                        lista_voti.append([gior, row[0], "A", "-", "-", 0, 0])

            if df.iloc[i+22][0] == "Modificatore difesa":
                lista_punti_modificatore.append([row[0], df.iloc[i+22][4], df.iloc[i+1][0]])
            else:
                lista_punti_modificatore.append([row[0], 0, df.iloc[i+1][0]])

        # Voti Fantagiocatore di destra
        if row[6] in player_name:

            for p in range(2, 13):
                if df.iloc[i+p][9] != "-" and df.iloc[i+p][6] in ruoli:
                    lista_voti.append(player(row, df, i+p, 6, gior))
                elif df.iloc[i+p][6] == "P":
                    if df.iloc[i+14][9] != "-":
                        lista_voti.append(player(row, df, i+14, 6, gior))
                    elif df.iloc[i+15][9] != "-":
                        lista_voti.append(player(row, df, i+15, 6, gior))
                    else:
                        lista_voti.append([gior, row[6], "P", "-", "-", 0, 0])
                elif df.iloc[i+p][6] == "D":
                    if df.iloc[i+16][9] != "-" and player(row, df, i+16, 6, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+16, 6, gior))
                    elif df.iloc[i+17][9] != "-" and player(row, df, i+17, 6, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+17, 6, gior))
                    else:
                        lista_voti.append([gior, row[6], "D", "-", "-", 0, 0])
                elif df.iloc[i+p][6] == "C":
                    if df.iloc[i+18][9] != "-" and player(row, df, i+18, 6, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+18, 6, gior))
                    elif df.iloc[i+19][9] != "-" and player(row, df, i+19, 6, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+19, 6, gior))
                    else:
                        lista_voti.append([gior, row[6], "C", "-", "-", 0, 0])
                elif df.iloc[i+p][6] == "A":
                    if df.iloc[i+20][9] != "-" and player(row, df, i+20, 6, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+20, 6, gior))
                    elif df.iloc[i+21][9] != "-" and player(row, df, i+21, 6, gior) not in lista_voti:
                        lista_voti.append(player(row, df, i+21, 6, gior))
                    else:
                        lista_voti.append([gior, row[6], "A", "-", "-", 0, 0])

            if df.iloc[i+22][6] == "Modificatore difesa":
                lista_punti_modificatore.append([row[6], df.iloc[i+22][10], df.iloc[i+1][6]])
            else:
                lista_punti_modificatore.append([row[6], 0, df.iloc[i+1][6]])

df = pd.DataFrame(lista_voti, columns=["Giornata", "Fantagiocatore",
                                       "Ruolo", "Giocatore", "Squadra",
                                       "Voto", "Fantavoto"])

subprocess.call(["python", "fantaculo.py"])
plot_tabelle_moduli(giornate, competizione, player_name)
plot_tabelle_giocatori_squadre(df, giornate)
plot_tabelle_bonus_ruoli(df, giornate)
plot_tabelle_modificatore(lista_punti_modificatore, giornate)
plot_tabelle_migliori_giocatori(df, giornate)