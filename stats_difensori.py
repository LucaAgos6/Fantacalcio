import plotly.graph_objects as go
import plotly.subplots as ps
import pandas as pd

giornate = 26
competizione = "spritecalcio111"

lista_voti_difensori = []
lista_punti_modificatore = []

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
        
        # Salva in una lista NomePlayer, Voto, Fantavoto del difensore
        # Voti sinistra
        if row[0] in player_name:

            for d in range(3,8):
                if df.iloc[i+d][0] == "D":
                    if df.iloc[i+d][3] != "-" and df.iloc[i+d][3]:
                        lista_voti_difensori.append([row[0], df.iloc[i+d][3], df.iloc[i+d][4]])
                    elif df.iloc[i+16][3] != "-":
                        lista_voti_difensori.append([row[0], df.iloc[i+16][3], df.iloc[i+16][4]])
                    elif df.iloc[i+17][3] != "-":
                        lista_voti_difensori.append([row[0], df.iloc[i+17][3], df.iloc[i+17][4]])
            
            if df.iloc[i+22][0] == "Modificatore difesa":
                lista_punti_modificatore.append([row[0], df.iloc[i+22][4]])
            else:
                lista_punti_modificatore.append([row[0], 0])

        # Voti destra
        if row[6] in player_name:
            for d in range(3,8):
                if df.iloc[i+d][6] == "D":
                    if df.iloc[i+d][9] != "-":
                        lista_voti_difensori.append([row[6], df.iloc[i+d][9], df.iloc[i+d][10]])
                    elif df.iloc[i+16][9] != "-":
                        lista_voti_difensori.append([row[6], df.iloc[i+16][9], df.iloc[i+16][10]])
                    elif df.iloc[i+17][9] != "-":
                        lista_voti_difensori.append([row[6], df.iloc[i+17][9], df.iloc[i+17][10]])
        
            if df.iloc[i+22][6] == "Modificatore difesa":
                lista_punti_modificatore.append([row[6], df.iloc[i+22][10]])
            else:
                lista_punti_modificatore.append([row[0], 0])
      
df = pd.DataFrame(lista_voti_difensori, columns=["Nome", "Voto", "Fantavoto"])
voto = df.groupby("Nome")["Voto"].mean().round(2)
fantavoto = df.groupby("Nome")["Fantavoto"].mean().round(2)
df = pd.DataFrame(voto)
df["Fantavoto"] = fantavoto
df["Differenza"] = fantavoto - voto
df = df.sort_values(by='Fantavoto', ascending=False)
print(df)

df = pd.DataFrame(lista_punti_modificatore, columns=["Nome", "Modificatore"])
modificatore = df.groupby("Nome")["Modificatore"].mean().round(2)
df = pd.DataFrame(modificatore)
df["Modificatore"] = modificatore
df = df.sort_values(by='Modificatore', ascending=False)
print(df)
