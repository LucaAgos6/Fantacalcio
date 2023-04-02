import pandas as pd

giornate = 26
competizione = "spritecalcio111"

lista_voti = []
lista_punti_modificatore = []

player_name = ["CLUB ATLETICO CACCIAS OLD BOYS",
               "??ANKONDORICACIVITASFIDEI??",
               "ROONEY TUNES",
               "PANITA TEAM",
               "HERTA MPONE",
               "I GIORDANI",
               "SPAL LETTI",
               "TAMMY TEAM"]
ruoli = ["P", "D", "C", "A"]


# Restituisce NomePlayer, Ruolo, Nome, Squadra, Voto e Fantavoto del giocatore
def player(row, df, i, n, gior):
    return [gior, row[n], df.iloc[i][n], df.iloc[i][n+1], df.iloc[i][n+2].lower(), df.iloc[i][n+3], df.iloc[i][n+4]]


for gior in range(1, giornate+1):

    df = pd.read_excel(
        f"Input\Giornate\Formazioni_{competizione}_{gior}_giornata.xlsx")

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
                lista_punti_modificatore.append([row[0], df.iloc[i+22][4]])
            else:
                lista_punti_modificatore.append([row[0], 0])

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
                lista_punti_modificatore.append([row[6], df.iloc[i+22][10]])
            else:
                lista_punti_modificatore.append([row[0], 0])

# print(lista_voti)

df = pd.DataFrame(lista_voti, columns=[
                  "Giornata", "Fantagiocatore", "Ruolo", "Giocatore", "Squadra", "Voto", "Fantavoto"])

# print(df.loc[(df['Giornata'] == 18) & (df['Ruolo'] == 'C') & (df['Fantagiocatore'] == '??ANKONDORICACIVITASFIDEI??')])
print(df)
df = df.groupby("Giocatore")["Giornata"].count().sort_values(ascending=False)
# print(df[25:50])


# Portieri
# df = pd.DataFrame(lista_voti_portieri, columns=["Nome", "Voto", "Fantavoto"])
# voto = df.groupby("Nome")["Voto"].mean().round(2)
# fantavoto = df.groupby("Nome")["Fantavoto"].mean().round(2)
# df = pd.DataFrame(voto)
# df["Fantavoto"] = fantavoto
# df["Differenza"] = fantavoto - voto
# df = df.sort_values(by='Fantavoto', ascending=False)
# print(df)

# Difensori
# df = pd.DataFrame(lista_voti_difensori, columns=["Nome", "Voto", "Fantavoto"])
# voto = df.groupby("Nome")["Voto"].mean().round(2)
# fantavoto = df.groupby("Nome")["Fantavoto"].mean().round(2)
# df = pd.DataFrame(voto)
# df["Fantavoto"] = fantavoto
# df["Differenza"] = fantavoto - voto
# df = df.sort_values(by='Fantavoto', ascending=False)
# print(df)

# Modificatore
dfMod = pd.DataFrame(lista_punti_modificatore, columns=["Nome", "Modificatore"])
modificatore = dfMod.groupby("Nome")["Modificatore"].mean().round(2)
dfMod = pd.DataFrame(modificatore)
dfMod["Modificatore"] = modificatore
dfMod = dfMod.sort_values(by='Modificatore', ascending=False)
print(dfMod)


# Centrocampisti
# dfC = df[df["Ruolo"] == "C"]
# voto = dfC.groupby("Fantagiocatore")["Voto"].mean().round(2)
# fantavoto = dfC.groupby("Fantagiocatore")["Fantavoto"].mean().round(2)
# dfC = pd.DataFrame(voto)
# dfC["Fantavoto"] = fantavoto
# dfC["Differenza"] = fantavoto - voto
# dfC = dfC.sort_values(by="Fantavoto", ascending=False)
# print(dfC)

