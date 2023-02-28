import pandas as pd

df = pd.read_excel("Input\Calendario_Cocazero111.xlsx")

luca = "Herta mpone"
carli = "??ANKONDORICACIVITASFIDEI??"
leo = "I giordani"
ambro = "Spal Letti"
boz = "Rooney Tunes"
caccia = "Club Atletico Caccias Old Boys"
steppa = "Panita Team"
furia = "Tammy Team"

lucaexp = 0
carliexp = 0
leoexp = 0
ambroexp = 0
bozexp = 0
cacciaexp = 0
steppaexp = 0
furiaexp = 0


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
    elif punti > 98:
        return 9

del df[df.columns[5]]
df = df[2:]
new_header = [1,2,3,4,5,6,7,8,9,10]
df.columns = new_header

for i, row in df.iterrows():
    if row[1] == carli:
        goal = gol(row[2])
        carliexp += punti(goal, row[3])
        print(carliexp)
