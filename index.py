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
    elif punti > 104:
        return 10


del df[df.columns[5]]
df = df[2:]
new_header = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df.columns = new_header

giornate = []

for i, row in df.iterrows():

    # Giornate a sinistra
    if "Giornata" in row[1] and df.loc[i+1][5] != "-":

        numGiornata = row[1].split(" ")[0]
        player1 = df.loc[i+1][1]
        player2 = df.loc[i+2][1]
        player3 = df.loc[i+3][1]
        player4 = df.loc[i+4][1]
        player5 = df.loc[i+1][4]
        player6 = df.loc[i+2][4]
        player7 = df.loc[i+3][4]
        player8 = df.loc[i+4][4]
        goal1 = gol(df.loc[i+1][2])
        goal2 = gol(df.loc[i+2][2])
        goal3 = gol(df.loc[i+3][2])
        goal4 = gol(df.loc[i+4][2])
        goal5 = gol(df.loc[i+1][3])
        goal6 = gol(df.loc[i+2][3])
        goal7 = gol(df.loc[i+3][3])
        goal8 = gol(df.loc[i+4][3])
        exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8 = 0, 0, 0, 0, 0, 0, 0, 0

        # PL1
        for j in range(4):
            exp1 += punti(goal1, gol(df.loc[i+1+j][3]))
        for j in range(3):
            exp1 += punti(goal1, gol(df.loc[i+2+j][2]))

        # PL2
        for j in range(4):
            exp2 += punti(goal2, gol(df.loc[i+1+j][3]))
        for j in range(2):
            exp2 += punti(goal2, gol(df.loc[i+3+j][2]))
        exp2 += punti(goal2, gol(df.loc[i+1][2]))

        # PL3
        for j in range(4):
            exp3 += punti(goal3, gol(df.loc[i+1+j][3]))
        for j in range(2):
            exp3 += punti(goal3, gol(df.loc[i+1+j][2]))
        exp3 += punti(goal3, gol(df.loc[i+4][2]))

        # PL4
        for j in range(4):
            exp4 += punti(goal4, gol(df.loc[i+1+j][3]))
        for j in range(3):
            exp4 += punti(goal4, gol(df.loc[i+1+j][2]))

        players = {player1: round(exp1/7, 2),
                   player2: round(exp2/7, 2),
                   player3: round(exp3/7, 2),
                   player4: round(exp4/7, 2),
                   #    player5: round(exp5/7, 2),
                   #    player6: round(exp6/7, 2),
                   #    player7: round(exp7/7, 2),
                   #    player8: round(exp8/7, 2)
                   }

        giornate.append({numGiornata: players})

    # Giornate a destra
    if "Giornata" in str(row[3]) and df.loc[i+1][10] != "-":

        if row[1].split(" ")[0] == "37ª":
            break

        numGiornata = row[3].split(" ")[0]
        player1 = df.loc[i+1][6]
        player2 = df.loc[i+2][6]
        player3 = df.loc[i+3][6]
        player4 = df.loc[i+4][6]
        player5 = df.loc[i+1][9]
        player6 = df.loc[i+2][9]
        player7 = df.loc[i+3][9]
        player8 = df.loc[i+4][9]
        goal1 = gol(df.loc[i+1][7])
        goal2 = gol(df.loc[i+2][7])
        goal3 = gol(df.loc[i+3][7])
        goal4 = gol(df.loc[i+4][7])
        goal5 = gol(df.loc[i+1][8])
        goal6 = gol(df.loc[i+2][8])
        goal7 = gol(df.loc[i+3][8])
        goal8 = gol(df.loc[i+4][8])
        exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8 = 0, 0, 0, 0, 0, 0, 0, 0

        # PL1
        for j in range(4):
            exp1 += punti(goal1, gol(df.loc[i+1+j][8]))
        for j in range(3):
            exp1 += punti(goal1, gol(df.loc[i+2+j][7]))

        # PL2
        for j in range(4):
            exp2 += punti(goal2, gol(df.loc[i+1+j][8]))
        for j in range(2):
            exp2 += punti(goal2, gol(df.loc[i+3+j][7]))
        exp2 += punti(goal2, gol(df.loc[i+1][7]))

        # PL3
        for j in range(4):
            exp3 += punti(goal3, gol(df.loc[i+1+j][8]))
        for j in range(2):
            exp3 += punti(goal3, gol(df.loc[i+1+j][7]))
        exp3 += punti(goal3, gol(df.loc[i+4][7]))

        # PL4
        for j in range(4):
            exp4 += punti(goal4, gol(df.loc[i+1+j][8]))
        for j in range(3):
            exp4 += punti(goal4, gol(df.loc[i+1+j][7]))

        players = {player1: round(exp1/7, 2),
                   player2: round(exp2/7, 2),
                   player3: round(exp3/7, 2),
                   player4: round(exp4/7, 2),
                   #    player5: round(exp5/7, 2),
                   #    player6: round(exp6/7, 2),
                   #    player7: round(exp7/7, 2),
                   #    player8: round(exp8/7, 2)
                   }

        giornate.append({numGiornata: players})
print(giornate)
