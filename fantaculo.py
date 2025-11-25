import pandas as pd
import plotly.subplots as ps
import plotly.graph_objects as go

from colors import colorPosizioni, colorPosMeritata, colorPosReale, colorPunti


def punti(punt1, punt2):
    if punt1 > punt2:
        return 3
    if punt1 == punt2:
        return 1
    if punt1 < punt2:
        return 0


def gol(punti):
    if punti < 66:
        return 0
    elif punti < 70:
        return 1
    elif punti < 74:
        return 2
    elif punti < 78:
        return 3
    elif punti < 82:
        return 4
    elif punti < 86:
        return 5
    elif punti < 90:
        return 6
    elif punti < 94:
        return 7
    elif punti < 98:
        return 8
    elif punti < 104:
        return 9
    elif punti >= 104:
        return 10


def makePointsLists(listaGol):
    n = len(listaGol)
    half = n // 2  # metà lista, es. 10 -> 5

    listaExp = [0] * n
    listaPoints = [0] * n

    for j in range(n):
        # punti "attesi" contro tutti gli altri
        for k in range(n):
            if j != k:
                listaExp[j] += punti(listaGol[j], listaGol[k])

        # punti effettivi del match
        if j < half:
            listaPoints[j] = punti(listaGol[j], listaGol[j + half])
        else:
            listaPoints[j] = punti(listaGol[j], listaGol[j - half])

    return listaExp, listaPoints


pd.options.mode.chained_assignment = None

lega = "FantaRotary"
playerName = ["Decimo",
              "PAZzesco FC",
              "El Pika Team",
              "Kephreddo F.a",
              "Berna Risk FC",
              "Panita Traditore",
              "KEAN WE DANCE???",
              "No TORO No PARTY",
              "Ti Faccio Nero FC",
              "Giovane fuoriclasse"]

playerExp = [0] * len(playerName)
playerPoint = [0] * len(playerName)

df = pd.read_excel(f"Input\Calendario_{lega}.xlsx")

del df[df.columns[5]]
df = df[2:]
new_header = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df.columns = new_header

expGiornate = []
pointsGiornate = []
dfExp = []
dfReal = []

for i, row in df.iterrows():

    # Giornate a sinistra
    if "Giornata" in str(row[1]) and df.loc[i+1][5] != "-" and pd.notna(df.loc[i+1, 5]):

        numGiornata = row[1].split(" ")[0]

        listaGol = [gol(df.loc[i + j, col]) for col in [2, 3] for j in range(1, len(playerName)//2 + 1)]

        listaExp, listaPoints = makePointsLists(listaGol)

        expPlayers = {}
        pointsPlayers = {}

        for x in range(5):
            expPlayers[df.loc[i+1+x][1]] = round(listaExp[x]/(len(playerName) - 1), 2)
            pointsPlayers[df.loc[i+1+x][1]] = listaPoints[x]
        for x in range(5):
            expPlayers[df.loc[i+1+x][4]] = round(listaExp[x+len(playerName)//2]/(len(playerName) - 1), 2)
            pointsPlayers[df.loc[i+1+x][4]] = listaPoints[x+len(playerName)//2]

        expGiornate.append({numGiornata: expPlayers})
        dfExp.append(expPlayers)
        pointsGiornate.append({numGiornata: pointsPlayers})
        dfReal.append(pointsPlayers)

    # Giornate a destra
    if "Giornata" in str(row[1]) and df.loc[i+1][10] != "-" and pd.notna(df.loc[i+1, 10]):

        if row[1].split(" ")[0] == "37ª":
            break

        numGiornata = row[3].split(" ")[0]

        listaGol = [gol(df.loc[i + j, col]) for col in [7, 8] for j in range(1, len(playerName)//2 + 1)]

        listaExp, listaPoints = makePointsLists(listaGol)

        expPlayers = {}
        pointsPlayers = {}

        for x in range(5):
            expPlayers[df.loc[i+1+x][6]] = round(listaExp[x]/(len(playerName) - 1), 2)
            pointsPlayers[df.loc[i+1+x][6]] = listaPoints[x]
        for x in range(5):
            expPlayers[df.loc[i+1+x][9]] = round(listaExp[x+len(playerName)//2]/(len(playerName) - 1), 2)
            pointsPlayers[df.loc[i+1+x][9]] = listaPoints[x+len(playerName)//2]

        expGiornate.append({numGiornata: expPlayers})
        dfExp.append(expPlayers)
        pointsGiornate.append({numGiornata: pointsPlayers})
        dfReal.append(pointsPlayers)


# Calcola gli expected points
for item in expGiornate:
    for keyItem in item:
        for key in item[keyItem]:
            for n in range(len(playerName)):
                if playerName[n] == key:
                    playerExp[n] += item[keyItem][key]

# Calcola i punti reali
for item in pointsGiornate:
    for keyItem in item:
        for key in item[keyItem]:
            for n in range(len(playerName)):
                if playerName[n] == key:
                    playerPoint[n] += item[keyItem][key]


dfCl = pd.DataFrame({"Classifica meritata": playerName,
                     "Punti meritati": playerExp,
                     "Punti reali": playerPoint})
dfCl["Punti meritati"] = round(dfCl["Punti meritati"], 2)
dfCl["Punti persi/rubati"] = dfCl["Punti reali"] - dfCl["Punti meritati"]
dfCl["Punti persi/rubati"] = round(dfCl["Punti persi/rubati"], 2)
dfCl.sort_values(by=["Punti reali"],
                 ascending=False,
                 inplace=True,
                 ignore_index=True)
dfCl["Posizione reale"] = new_header
dfCl.sort_values(by=["Punti meritati"],
                 ascending=False,
                 inplace=True,
                 ignore_index=True)
dfCl.insert(0, "Posizione meritata", new_header)
dfCl["Posizioni perse/rubate"] = dfCl["Posizione meritata"]-dfCl["Posizione reale"]

colorsPunti = colorPunti(dfCl)
colorsPosizioni = colorPosizioni(dfCl)
colorsClassReale = colorPosReale(dfCl)
colorsClassMeritata = colorPosMeritata(dfCl)
l = "lavender"

fig = ps.make_subplots(rows=2, cols=1,
                       specs=[[{"type": "scatter"}],
                              [{"type": "table"}]])
fig.update_layout(title_text=f"Statistiche della {numGiornata} Giornata del Fantacalcio {lega}",
                  xaxis1_title_text="Giornata N°",
                  yaxis1_title_text="Indice del culo",
                  bargap=0.2)
fig.add_trace(go.Table(columnwidth=[4, 10, 4, 4, 4, 4, 4],
                       header=dict(values=list(dfCl.columns),
                                   fill_color="paleturquoise",
                                   line_color='darkslategray'),
                       cells=dict(values=[dfCl[col] for col in dfCl.columns],
                                  fill=dict(color=[colorsClassMeritata,
                                                   l, l, l,
                                                   colorsPunti,
                                                   colorsClassReale,
                                                   colorsPosizioni]),
                                  line_color='darkslategray')), row=2, col=1)


dfExp = pd.DataFrame(dfExp)
dfExp["Giornata"] = 1
for x in range(1, len(dfExp)):
    dfExp.iloc[x] += dfExp.iloc[x-1]

    dfExp.loc[x, "Giornata"] = x + 1

dfReal = pd.DataFrame(dfReal)
dfReal["Giornata"] = 1
for x in range(1, len(dfReal)):
    dfReal.iloc[x] += dfReal.iloc[x-1]
    dfReal.loc[x, "Giornata"] = x + 1

dfDif = dfReal - dfExp
for x in range(0, len(dfDif)):
    dfDif.loc[x, "Giornata"] = x + 1


for i in range(len(playerName)):
    fig.add_trace(go.Scatter(x=dfDif["Giornata"], y=dfDif[playerName[i]],
                  name=playerName[i], mode="lines+markers"), row=1, col=1)

fig.show()

print("\nPlot del grafico fantaculo\n")
