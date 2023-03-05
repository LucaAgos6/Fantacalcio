def colorPunti(df):
    l = "lavender"
    colorsPunti = []
    for c in df["Punti persi/rubati"]:
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
    return colorsPunti
 
def colorPosizioni(df):
    l = "lavender"
    colorsPosizioni = []
    for c in df["Posizioni perse/rubate"]:
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