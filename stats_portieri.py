import plotly.graph_objects as go
import plotly.subplots as ps
import pandas as pd

giornate = 26
competizione = "spritecalcio111"

lista_voti_portieri = []

player_name = ["CLUB ATLETICO CACCIAS OLD BOYS",
               "??ANKONDORICACIVITASFIDEI??",
               "ROONEY TUNES",
               "PANITA TEAM",
               "HERTA MPONE",
               "I GIORDANI",
               "SPAL LETTI",
               "TAMMY TEAM"]

for i in range(1, giornate+1):

    df = pd.read_excel(
        f"Input\Giornate\Formazioni_{competizione}_{i}_giornata.xlsx")

    for i, row in df.iterrows():
        
        # Salva in una lista NomePlayer, Voto, Fantavoto del portiere
        # Voti sinistra
        if row[0] in player_name:
            if df.loc[i+2][3] != "-":
                lista_voti_portieri.append([row[0], df.loc[i+2][3], df.loc[i+2][4]])
            elif df.loc[i+14][3] != "-":
                lista_voti_portieri.append([row[0], df.loc[i+14][3], df.loc[i+14][4]])
            elif df.loc[i+15][3] != "-":
                lista_voti_portieri.append([row[0], df.loc[i+15][3], df.loc[i+15][4]])
            else:
                lista_voti_portieri.append([row[0], 0, 0])

            for d in range(6):
                pass

        # Voti destra
        if row[6] in player_name:
            if df.loc[i+2][9] != "-":
                lista_voti_portieri.append([row[6], df.loc[i+2][9], df.loc[i+2][10]])
            elif df.loc[i+14][9] != "-":
                lista_voti_portieri.append([row[6], df.loc[i+14][9], df.loc[i+14][10]])
            elif df.loc[i+15][9] != "-":
                lista_voti_portieri.append([row[6], df.loc[i+15][9], df.loc[i+15][10]])
            else:
                lista_voti_portieri.append([row[0], 0, 0])

        # Salva in una lista NomePlayer, Voto, Fantavoto dei difensori
        

        

df = pd.DataFrame(lista_voti_portieri, columns=["Nome", "Voto", "Fantavoto"])
voto = df.groupby("Nome")["Voto"].mean().round(2)
fantavoto = df.groupby("Nome")["Fantavoto"].mean().round(2)
df = pd.DataFrame(voto)
df["Fantavoto"] = fantavoto
df["Differenza"] = fantavoto - voto
df = df.sort_values(by='Fantavoto', ascending=False)
print(df)
