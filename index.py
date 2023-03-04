import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel("Input\Calendario_Cocazero111.xlsx")


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

    listaExp = [0, 0, 0, 0, 0, 0, 0, 0]
    listaPoints = [0, 0, 0, 0, 0, 0, 0, 0]

    for j in range(len(listaGol)):
        for k in range(len(listaGol)):
            if j != k:
                listaExp[j] += punti(listaGol[j], listaGol[k])
        if j < 4:
            listaPoints[j] = punti(listaGol[j], listaGol[j+4])
        elif j >= 4:
            listaPoints[j] = punti(listaGol[j], listaGol[j-4])

    return listaExp, listaPoints


del df[df.columns[5]]
df = df[2:]
new_header = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df.columns = new_header

expGiornate = []
pointsGiornate = []

for i, row in df.iterrows():

    # Giornate a sinistra
    if "Giornata" in row[1] and df.loc[i+1][5] != "-":

        numGiornata = row[1].split(" ")[0]

        listaGol = [gol(df.loc[i+1][2]), gol(df.loc[i+2][2]),
                    gol(df.loc[i+3][2]), gol(df.loc[i+4][2]),
                    gol(df.loc[i+1][3]), gol(df.loc[i+2][3]),
                    gol(df.loc[i+3][3]), gol(df.loc[i+4][3])]

        listaExp, listaPoints = makePointsLists(listaGol)

        expPlayers = {}
        pointsPlayers = {}

        for x in range(4):
            expPlayers[df.loc[i+1+x][1]] = round(listaExp[x]/7, 2)
            pointsPlayers[df.loc[i+1+x][1]] = listaPoints[x]
        for x in range(4):
            expPlayers[df.loc[i+1+x][4]] = round(listaExp[x+4]/7, 2)
            pointsPlayers[df.loc[i+1+x][4]] = listaPoints[x+4]

        expGiornate.append({numGiornata: expPlayers})
        pointsGiornate.append({numGiornata: pointsPlayers})

    # Giornate a destra
    if "Giornata" in str(row[3]) and df.loc[i+1][10] != "-":

        if row[1].split(" ")[0] == "37ª":
            break

        numGiornata = row[3].split(" ")[0]

        listaGol = [gol(df.loc[i+1][7]), gol(df.loc[i+2][7]),
                    gol(df.loc[i+3][7]), gol(df.loc[i+4][7]),
                    gol(df.loc[i+1][8]), gol(df.loc[i+2][8]),
                    gol(df.loc[i+3][8]), gol(df.loc[i+4][8])]

        listaExp, listaPoints = makePointsLists(listaGol)

        expPlayers = {}
        pointsPlayers = {}

        for x in range(4):
            expPlayers[df.loc[i+1+x][6]] = round(listaExp[x]/7, 2)
            pointsPlayers[df.loc[i+1+x][6]] = listaPoints[x]
        for x in range(4):
            expPlayers[df.loc[i+1+x][9]] = round(listaExp[x+4]/7, 2)
            pointsPlayers[df.loc[i+1+x][9]] = listaPoints[x+4]

        expGiornate.append({numGiornata: expPlayers})
        pointsGiornate.append({numGiornata: pointsPlayers})

playerName = ["Club Atletico Caccias Old Boys",
              "??ANKONDORICACIVITASFIDEI??",
              "Rooney Tunes",
              "Panita Team",
              "Herta mpone",
              "I giordani",
              "Spal Letti",
              "Tammy Team"]

playerExp = [0, 0, 0, 0, 0, 0, 0, 0]
playerPoint = [0, 0, 0, 0, 0, 0, 0, 0]

for item in expGiornate:
    for keyItem in item:
        for key in item[keyItem]:
            for n in range(len(playerName)):
                if playerName[n] == key:
                    playerExp[n] += item[keyItem][key]

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
dfCl["Posizione reale"] = new_header[:-2]
dfCl.sort_values(by=["Punti meritati"],
                 ascending=False,
                 inplace=True,
                 ignore_index=True)
dfCl.insert(0, "Posizione meritata", new_header[:-2])
dfCl["Posizioni perse/rubate"] = dfCl["Posizione meritata"] - \
    dfCl["Posizione reale"]

print(dfCl)

colorsPunti = []
colorsPosizioni = []
l = "lavender"

for c in dfCl["Punti persi/rubati"]:
    if c > 5:
        colorsPunti.append("#fc0808")
    elif c > 2.5:
        colorsPunti.append("#ff4a4a")
    elif c > 0:
        colorsPunti.append("#faafaf")
    elif c > -2.5:
        colorsPunti.append("#b0faaf")
    elif c > -5:
        colorsPunti.append("#5dfa5a")
    elif c <= -5:
        colorsPunti.append("#06d602")

for c in dfCl["Posizioni perse/rubate"]:
    if c > 2:
        colorsPosizioni.append("#fc0808")
    elif c > 1:
        colorsPosizioni.append("#ff4a4a")
    elif c > 0:
        colorsPosizioni.append("#faafaf")
    elif c == 0:
        colorsPosizioni.append("lavender")
    elif c > -1:
        colorsPosizioni.append("#b0faaf")
    elif c > -2:
        colorsPosizioni.append("#5dfa5a")
    elif c <= -2:
        colorsPosizioni.append("#06d602")


fig = go.Figure(data=[go.Table(header=dict(values=list(dfCl.columns),
                                           fill_color="paleturquoise"),
                               cells=dict(values=[dfCl[col] for col in dfCl.columns],
                                          fill=dict(color=[l, l, l, l, colorsPunti, l, colorsPosizioni])))])
fig.show()
