import plotly.graph_objects as go
import plotly.subplots as ps
import pandas as pd


def plot_tabelle_giocatori_squadre(df, giornata):
    dfGiocatori = df.groupby("Giocatore")[
        "Giornata"].count().sort_values(ascending=False)
    dfGiocatori = pd.DataFrame(dfGiocatori)

    dfSquadre = df.groupby("Squadra")[
        "Giornata"].count().sort_values(ascending=False)
    dfSquadre = pd.DataFrame(dfSquadre)

    fig = ps.make_subplots(rows=1, cols=2,
                           specs=[[{"type": "table"}, {"type": "table"}]],
                           subplot_titles=["Giocatori più utilizzati", "Giocatori utilizzati per Squadra"])
    fig.update_layout(
        title_text=f"Giocatori e Giocatori per Squadra più utilizzati aggiornato alla {giornata}° giornata")

    fig.add_trace(go.Table(header=dict(values=("Giocatore", "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfGiocatori.index[:21], dfGiocatori[:21]])), row=1, col=1)
    fig.add_trace(go.Table(header=dict(values=("Squadra", "N° Giocatori"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfSquadre.index.str.upper(), dfSquadre])), row=1, col=2)
    fig.show()

    print("Plot delle tabelle di utilizzo giocatori\n")


def plot_tabelle_moduli(giornate, competizione, player_name):

    lista_moduli = []

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
        title_text=f"Moduli più utilizzati per Giocatore aggiornato alla {giornate}° Giornata")

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
                                           line_color="darkslategray"),
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
                                       line_color="darkslategray"),
                           cells=dict(values=result)), row=3, col=1)

    # Calcola le percentuali
    tot = result.sum()
    for i in range(len(result)):
        result[i] = f"{round(result[i]/tot*100, 2)}%"

    fig.add_trace(go.Table(header=dict(values=result.index,
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=result)), row=3, col=3)

    print("Plot delle tabelle statistiche sui moduli\n")
    fig.show()


def plot_tabelle_bonus_ruoli(df, giornate):

    # Portieri
    dfPortieri = df[df["Ruolo"] == "P"]
    voto = dfPortieri.groupby("Fantagiocatore")["Voto"].mean().round(2)
    fantavoto = dfPortieri.groupby("Fantagiocatore")[
        "Fantavoto"].mean().round(2)
    dfPortieri = pd.DataFrame(voto)
    dfPortieri["Fantavoto"] = fantavoto
    dfPortieri["Differenza"] = round(fantavoto - voto, 2)
    dfPortieri = dfPortieri.sort_values(by="Fantavoto", ascending=False)

    # Difensori
    dfDifensori = df[df["Ruolo"] == "D"]
    voto = dfDifensori.groupby("Fantagiocatore")["Voto"].mean().round(2)
    fantavoto = dfDifensori.groupby("Fantagiocatore")[
        "Fantavoto"].mean().round(2)
    dfDifensori = pd.DataFrame(voto)
    dfDifensori["Fantavoto"] = fantavoto
    dfDifensori["Differenza"] = round(fantavoto - voto, 2)
    dfDifensori = dfDifensori.sort_values(by="Fantavoto", ascending=False)

    # Centrocampisti
    dfCentrocampisti = df[df["Ruolo"] == "C"]
    voto = dfCentrocampisti.groupby("Fantagiocatore")["Voto"].mean().round(2)
    fantavoto = dfCentrocampisti.groupby("Fantagiocatore")[
        "Fantavoto"].mean().round(2)
    dfCentrocampisti = pd.DataFrame(voto)
    dfCentrocampisti["Fantavoto"] = fantavoto
    dfCentrocampisti["Differenza"] = round(fantavoto - voto, 2)
    dfCentrocampisti = dfCentrocampisti.sort_values(
        by="Fantavoto", ascending=False)

    # Attaccanti
    dfAttaccanti = df[df["Ruolo"] == "A"]
    voto = dfAttaccanti.groupby("Fantagiocatore")["Voto"].mean().round(2)
    fantavoto = dfAttaccanti.groupby("Fantagiocatore")[
        "Fantavoto"].mean().round(2)
    dfAttaccanti = pd.DataFrame(voto)
    dfAttaccanti["Fantavoto"] = fantavoto
    dfAttaccanti["Differenza"] = round(fantavoto - voto, 2)
    dfAttaccanti = dfAttaccanti.sort_values(by="Fantavoto", ascending=False)

    fig = ps.make_subplots(rows=2, cols=2,
                           specs=[[{"type": "table"}, {"type": "table"}],
                                  [{"type": "table"}, {"type": "table"}]],
                           subplot_titles=["Media Voti e Fantavoti per i Portieri",
                                           "Media Voti e Fantavoti per i Difensori",
                                           "Media Voti e Fantavoti per i Centrocampisti",
                                           "Media Voti e Fantavoti per gli Attaccanti"])
    fig.update_layout(
        title_text=f"Media voti e bonus per Ruolo, ordinato per Fantavoto, aggiornato alla {giornate}° Giornata")

    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Voto", "Fantavoto", "Differenza"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfPortieri.index,
                                              dfPortieri["Voto"],
                                              dfPortieri["Fantavoto"],
                                              dfPortieri["Differenza"]]),
                           columnwidth=[2, 1, 1, 1]), row=1, col=1)
    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Voto", "Fantavoto", "Differenza"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfDifensori.index,
                                              dfDifensori["Voto"],
                                              dfDifensori["Fantavoto"],
                                              dfDifensori["Differenza"]]),
                           columnwidth=[2, 1, 1, 1]), row=1, col=2)
    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Voto", "Fantavoto", "Differenza"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfCentrocampisti.index,
                                              dfCentrocampisti["Voto"],
                                              dfCentrocampisti["Fantavoto"],
                                              dfCentrocampisti["Differenza"]]),
                           columnwidth=[2, 1, 1, 1]), row=2, col=1)
    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Voto", "Fantavoto", "Differenza"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfAttaccanti.index,
                                              dfAttaccanti["Voto"],
                                              dfAttaccanti["Fantavoto"],
                                              dfAttaccanti["Differenza"]]),
                           columnwidth=[2, 1, 1, 1]), row=2, col=2)
    fig.show()

    print("Plot delle tabelle con media voti\n")


def plot_tabelle_modificatore(lista_mod, giornate):

    # Modificatore totale
    dfMod = pd.DataFrame(lista_mod, columns=["Nome", "Modificatore", "Modulo"])
    modificatore = dfMod.groupby("Nome")["Modificatore"].mean().round(2)
    num = dfMod.groupby("Nome")["Modificatore"].count()
    dfMod = pd.DataFrame(modificatore)
    dfMod["Modificatore"] = modificatore
    dfMod["Giornate"] = num
    dfMod = dfMod.sort_values(by="Modificatore", ascending=False)

    # Modificatore filtrato per quando la difesa è a 4 o a 5
    lista_mod_filt1 = [lst for lst in lista_mod if str(
        lst[2]).startswith("4") or str(lst[2]).startswith("5")]
    dfModFilt1 = pd.DataFrame(lista_mod_filt1, columns=[
                              "Nome", "Modificatore", "Modulo"])
    modificatore = dfModFilt1.groupby("Nome")["Modificatore"].mean().round(2)
    num = dfModFilt1.groupby("Nome")["Modificatore"].count()
    dfModFilt1 = pd.DataFrame(modificatore)
    dfModFilt1["Modificatore"] = modificatore
    dfModFilt1["Giornate"] = num
    dfModFilt1 = dfModFilt1.sort_values(by="Modificatore", ascending=False)

    # Modificatore filtrato per quando è > 0
    lista_mod_filt2 = [lst for lst in lista_mod if lst[1] > 0]
    dfModFilt2 = pd.DataFrame(lista_mod_filt2, columns=[
                              "Nome", "Modificatore", "Modulo"])
    modificatore = dfModFilt2.groupby("Nome")["Modificatore"].mean().round(2)
    num = dfModFilt2.groupby("Nome")["Modificatore"].count()
    dfModFilt2 = pd.DataFrame(modificatore)
    dfModFilt2["Modificatore"] = modificatore
    dfModFilt2["Giornate"] = num
    dfModFilt2 = dfModFilt2.sort_values(by="Modificatore", ascending=False)

    # Modificatore filtrato per quando è = 0
    lista_mod_filt3 = [lst for lst in lista_mod if str(
        lst[2]).startswith("4") or str(lst[2]).startswith("5")]
    lista_mod_filt3 = [lst for lst in lista_mod_filt3 if lst[1] == 0]
    dfModFilt3 = pd.DataFrame(lista_mod_filt3, columns=[
                              "Nome", "Modificatore", "Modulo"])
    modificatore = dfModFilt3.groupby("Nome")["Modificatore"].mean().round(2)
    num = dfModFilt3.groupby("Nome")["Modificatore"].count()
    dfModFilt3 = pd.DataFrame(modificatore)
    dfModFilt3["Modificatore"] = modificatore
    dfModFilt3["Giornate"] = num
    dfModFilt3 = dfModFilt3.sort_values(by="Giornate", ascending=False)

    fig = ps.make_subplots(rows=2, cols=2,
                           specs=[[{"type": "table"}, {"type": "table"}],
                                  [{"type": "table"}, {"type": "table"}]],
                           subplot_titles=["Media del Modificatore per tutte le Giornate",
                                           "Media del Modificatore per le Giornate in cui la difesa è a 4 o 5",
                                           "Media del Modificatore per le Giornate in cui è > 0",
                                           "Media del Modificatore per le Giornate in cui è = 0"])
    fig.update_layout(
        title_text=f"Media del Modificatore aggiornato alla {giornate}° Giornata")

    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Media Modificatore", "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(
                               values=[dfMod.index, dfMod["Modificatore"], dfMod["Giornate"]]),
                           columnwidth=[2, 1]), row=1, col=1)
    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Media Modificatore", "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(
                               values=[dfModFilt1.index, dfModFilt1["Modificatore"], dfModFilt1["Giornate"]]),
                           columnwidth=[2, 1]), row=1, col=2)
    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Media Modificatore", "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(
                               values=[dfModFilt2.index, dfModFilt2["Modificatore"], dfModFilt2["Giornate"]]),
                           columnwidth=[2, 1]), row=2, col=1)
    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Media Modificatore", "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(
                               values=[dfModFilt3.index, dfModFilt3["Modificatore"], dfModFilt3["Giornate"]]),
                           columnwidth=[2, 1]), row=2, col=2)
    fig.show()

    print("Plot delle tabelle statistiche sul modificatore\n")
