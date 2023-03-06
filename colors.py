def colorPunti(df):
    l = "lavender"
    colorsPunti = []
    for c in df["Punti persi/rubati"]:
        if c > 5:
            colorsPunti.append("#cf0226")
        elif c > 2.5:
            colorsPunti.append("#FF6347")
        elif c > 0:
            colorsPunti.append("#FFC0CB")
        elif c > -2.5:
            colorsPunti.append("#90EE90")
        elif c > -5:
            colorsPunti.append("#63ff52")
        elif c <= -5:
            colorsPunti.append("#02cf0c")
    return colorsPunti
 
def colorPosizioni(df):
    l = "lavender"
    colorsPosizioni = []
    for c in df["Posizioni perse/rubate"]:
        if c > 2:
            colorsPosizioni.append("#cf0226")
        elif c > 1:
            colorsPosizioni.append("#FF6347")
        elif c > 0:
            colorsPosizioni.append("#FFC0CB")
        elif c == 0:
            colorsPosizioni.append("lavender")
        elif c > -1:
            colorsPosizioni.append("#b0faaf")
        elif c > -2:
            colorsPosizioni.append("#63ff52")
        elif c <= -2:
            colorsPosizioni.append("#02cf0c")
    return colorsPosizioni

def colorPosReale(df): 
    l = "lavender"
    colorsClassReale = []
    for c in df["Posizione reale"]:
        if c == 1:
            colorsClassReale.append("#FFD700")
        elif c == 2:
            colorsClassReale.append("#b4c2c2")
        elif c == 3:
            colorsClassReale.append("#cd7f32")
        else:
            colorsClassReale.append(l)
    return colorsClassReale

def colorPosMeritata(df):
    l = "lavender"
    colorsClassMeritata = []
    for c in df["Posizione meritata"]:
        if c == 1:
            colorsClassMeritata.append("#FFD700")
        elif c == 2:
            colorsClassMeritata.append("#b4c2c2")
        elif c == 3:
            colorsClassMeritata.append("#cd7f32")
        else:
            colorsClassMeritata.append(l)
    return colorsClassMeritata