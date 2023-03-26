import plotly.graph_objects as go
import plotly.subplots as ps
import pandas as pd

giornate = 26
competizione = "spritecalcio111"

lista_moduli = []

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

    # Salva in una lista "NomePlayer Modulo"
    for i, row in df.iterrows():
        if row[0] in player_name:
            lista_moduli.append(f"{row[0]} {df.loc[i+1][0]}")
        if row[6] in player_name:
            lista_moduli.append(f"{row[6]} {df.loc[i+1][6]}")


# Dizionario di "NomePlayer Modulo": N° volte
conteggio_elementi = {}
for elemento in lista_moduli:
    if elemento in conteggio_elementi:
        conteggio_elementi[elemento] += 1
    else:
        conteggio_elementi[elemento] = 1

fig = ps.make_subplots(rows=3, cols=4,
                       specs=[[{"type": "table"}, {"type": "table"}, {"type": "table"}, {"type": "table"}],
                              [{"type": "table"}, {"type": "table"}, {
                                  "type": "table"}, {"type": "table"}],
                              [{"type": "table", "colspan": 2}, None, {"type": "table", "colspan": 2}, None]],
                       subplot_titles=player_name + ["Somma totale dei moduli utilizzati", "Percentuale dei moduli utilizzati"])
fig.update_layout(
    title_text=f"Moduli più utilizzati per giocatore aggiornato alla giornata N° {giornate}")

row = 1
col = 1
dftot = pd.DataFrame()

for player in player_name:

    # Filtro per nome del player
    chiavi_filtrate = [
        key for key in conteggio_elementi.keys() if player in key]
    dizionario_filtrato = {
        key: value for key, value in conteggio_elementi.items() if key in chiavi_filtrate}

    tabella = []
    sorted_tuples = sorted(dizionario_filtrato.items(),
                           key=lambda x: x[1], reverse=True)
    for key, value in sorted_tuples:
        key = key[-3:]
        if key[-1] == "-":
            key = "-"
        tabella.append([key, value])

    df = pd.DataFrame(tabella)
    dftot = pd.concat([dftot, df])
    fig.add_trace(go.Table(header=dict(values=("Modulo", "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color='darkslategray'),
                           cells=dict(values=[df[col] for col in df.columns])), row=row, col=col)

    if col < 4 and row == 1:
        col += 1
    elif row == 1:
        col = 1
        row = 2
    else:
        col += 1

# Conta le istanze e le ordina decrescenti
result = dftot.groupby(0)[1].sum().sort_values(ascending=False)

fig.add_trace(go.Table(header=dict(values=result.index,
                                   fill_color="paleturquoise",
                                   line_color='darkslategray'),
                       cells=dict(values=result)), row=3, col=1)

# Calcola le percentuali
tot = result.sum()
for i in range(len(result)):
    result[i] = f"{round(result[i]/tot*100, 2)}%"

fig.add_trace(go.Table(header=dict(values=result.index,
                                   fill_color="paleturquoise",
                                   line_color='darkslategray'),
                       cells=dict(values=result)), row=3, col=3)

print("\nPlot delle tabelle statistiche sui moduli\n")
fig.show()
