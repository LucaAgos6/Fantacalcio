import plotly.graph_objects as go
import plotly.subplots as ps
import pandas as pd

from utils import utils_bonus_ruoli, add_trace_bonus_ruoli
from utils import utils_modificatore, add_trace_modificatore
from utils import utils_migliori_giocatori, add_trace_migliori_giocatori


def plot_tabelle_giocatori_squadre(df, giornata):
    dfGiocatori = df.groupby("Giocatore")["Giornata"].count().sort_values(ascending=False)
    dfGiocatori = pd.DataFrame(dfGiocatori)

    dfSquadre = df.groupby("Squadra")["Giornata"].count().sort_values(ascending=False)
    dfSquadre = pd.DataFrame(dfSquadre)

    fig = ps.make_subplots(rows=1, cols=2,
                           specs=[[{"type": "table"}, {"type": "table"}]],
                           subplot_titles=["Giocatori più utilizzati",
                                           "Giocatori utilizzati per Squadra"])
    fig.update_layout(title_text=f"Giocatori e Giocatori per Squadra " +
                                 f"più utilizzati aggiornato alla {giornata}° giornata")

    fig.add_trace(go.Table(header=dict(values=("Giocatore", "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfGiocatori.index[:21], 
                                              dfGiocatori[:21]])), row=1, col=1)
    fig.add_trace(go.Table(header=dict(values=("Squadra", "N° Giocatori"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[dfSquadre.index.str.upper(), 
                                              dfSquadre])), row=1, col=2)
    fig.show()

    print("Plot delle tabelle di utilizzo giocatori\n")


def plot_tabelle_moduli(giornate, competizione, player_name):

    lista_moduli = []

    for i in range(1, giornate+1):

        df = pd.read_excel(f"Input\Giornate\Formazioni_{competizione}_{i}_giornata.xlsx")

        # Salva in una lista "NomePlayer Modulo"
        for i, row in df.iterrows():
            if row.iloc[0] in player_name:
                lista_moduli.append(f"{row.iloc[0]} {df.iloc[i + 1, 0]}")
            if row.iloc[6] in player_name:
                lista_moduli.append(f"{row.iloc[6]} {df.iloc[i + 1, 6]}")

    # Dizionario di "NomePlayer Modulo": N° volte
    conteggio_elementi = {}
    for elemento in lista_moduli:
        if elemento in conteggio_elementi:
            conteggio_elementi[elemento] += 1
        else:
            conteggio_elementi[elemento] = 1

    fig = ps.make_subplots(rows=3, cols=5,
                           specs=[[{"type": "table"}] * 5,
                                  [{"type": "table"}] * 5,
                                  [{"type": "table", "colspan": 2}, None, None,
                                   {"type": "table", "colspan": 2}, None]],
                           subplot_titles=player_name + ["Somma totale dei moduli utilizzati",
                                                         "Percentuale dei moduli utilizzati"])
    fig.update_layout(
        title_text=f"Moduli più utilizzati per Giocatore aggiornato alla {giornate}° Giornata")

    row = 1
    col = 1
    dftot = pd.DataFrame()

    for player in player_name:

        # Filtro per nome del player
        chiavi_filtrate = [key for key in conteggio_elementi.keys() if player in key]
        dizionario_filtrato = {key: value for key, value in conteggio_elementi.items() if key in chiavi_filtrate}

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

        if col < 5 and row == 1:
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
    result = result.astype(str)

    for i in range(len(result)):
        result.iloc[i] = f"{round(int(result.iloc[i])/tot*100, 2)}%"

    fig.add_trace(go.Table(header=dict(values=result.index,
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=result)), row=3, col=4)

    print("Plot delle tabelle statistiche sui moduli\n")
    fig.show()


def plot_tabelle_bonus_ruoli(df, giornate):

    # Creo i 4 dataframe
    dfPortieri = utils_bonus_ruoli(df, "P")
    dfDifensori = utils_bonus_ruoli(df, "D")
    dfCentrocampisti = utils_bonus_ruoli(df, "C")
    dfAttaccanti = utils_bonus_ruoli(df, "A")

    fig = ps.make_subplots(rows=2, cols=2,
                           specs=[[{"type": "table"}, {"type": "table"}],
                                  [{"type": "table"}, {"type": "table"}]],
                           subplot_titles=["Media Voti e Fantavoti per i Portieri",
                                           "Media Voti e Fantavoti per i Difensori",
                                           "Media Voti e Fantavoti per i Centrocampisti",
                                           "Media Voti e Fantavoti per gli Attaccanti"])
    fig.update_layout(title_text=f"Media voti e bonus per Ruolo, " +
                                 f"ordinato per Fantavoto, aggiornato alla {giornate}° Giornata")
    fig = add_trace_bonus_ruoli(fig, dfPortieri, 1, 1)
    fig = add_trace_bonus_ruoli(fig, dfDifensori, 1, 2)
    fig = add_trace_bonus_ruoli(fig, dfCentrocampisti, 2, 1)
    fig = add_trace_bonus_ruoli(fig, dfAttaccanti, 2, 2)
    fig.show()

    print("Plot delle tabelle con media voti\n")


def plot_tabelle_modificatore(lista_mod, giornate):

    # Modificatore totale
    dfMod = utils_modificatore(lista_mod)
    list_players = dfMod.index.tolist()

    # Modificatore filtrato per quando la difesa è a 4 o a 5
    lista_mod_filt1 = [lst for lst in lista_mod if
                       str(lst[2]).startswith("4") or
                       str(lst[2]).startswith("5")]
    dfModFilt1 = utils_modificatore(lista_mod_filt1)
    missing_names = [name for name in list_players if name not in dfModFilt1.index]
    if missing_names:
        df_missing = pd.DataFrame({"Modificatore": [0.0] * len(missing_names),
                                   "Giornate": [0] * len(missing_names)}, index=missing_names)
        dfModFilt1 = pd.concat([dfModFilt1, df_missing])

    # Modificatore filtrato per quando è > 0
    lista_mod_filt2 = [lst for lst in lista_mod if lst[1] > 0]
    dfModFilt2 = utils_modificatore(lista_mod_filt2)
    missing_names = [name for name in list_players if name not in dfModFilt2.index]
    if missing_names:
        df_missing = pd.DataFrame({"Modificatore": [0.0] * len(missing_names),
                                   "Giornate": [0] * len(missing_names)}, index=missing_names)
        dfModFilt2 = pd.concat([dfModFilt2, df_missing])

    # Modificatore filtrato per quando è = 0
    lista_mod_filt3 = [lst for lst in lista_mod if
                       str(lst[2]).startswith("4") or
                       str(lst[2]).startswith("5")]
    lista_mod_filt3 = [lst for lst in lista_mod_filt3 if lst[1] == 0]
    dfModFilt3 = utils_modificatore(lista_mod_filt3)
    missing_names = [name for name in list_players if name not in dfModFilt3.index]
    if missing_names:
        df_missing = pd.DataFrame({"Modificatore": [0.0] * len(missing_names),
                                   "Giornate": [0] * len(missing_names)}, index=missing_names)
        dfModFilt3 = pd.concat([dfModFilt3, df_missing])
    dfModFilt3 = dfModFilt3.sort_values(by="Giornate", ascending=False)

    fig = ps.make_subplots(rows=2, cols=2,
                           specs=[[{"type": "table"}, {"type": "table"}],
                                  [{"type": "table"}, {"type": "table"}]],
                           subplot_titles=["Media del Modificatore per tutte le Giornate",
                                           "Media del Modificatore per le Giornate in cui la difesa è a 4 o 5",
                                           "Media del Modificatore per le Giornate in cui è > 0",
                                           "Numero di Giornate in cui il Modificatore è = 0 e la difesa è a 4 o 5"])
    fig.update_layout(title_text=f"Media del Modificatore aggiornato alla {giornate}° Giornata")

    fig = add_trace_modificatore(fig, dfMod, 1, 1)
    fig = add_trace_modificatore(fig, dfModFilt1, 1, 2)
    fig = add_trace_modificatore(fig, dfModFilt2, 2, 1)
    fig = add_trace_modificatore(fig, dfModFilt3, 2, 2)
    fig.show()

    print("Plot delle tabelle statistiche sul modificatore\n")


def plot_tabelle_migliori_giocatori(df, giornate):

    # Crea i 4 Dataframe con presenze minime dei giocatori
    presenze_minime = 5
    dfPortieri = utils_migliori_giocatori(df, "P", presenze_minime)
    dfDifensori = utils_migliori_giocatori(df, "D", presenze_minime)
    dfCentrocampisti = utils_migliori_giocatori(df, "C", presenze_minime)
    dfAttaccanti = utils_migliori_giocatori(df, "A", presenze_minime)

    fig = ps.make_subplots(rows=1, cols=4,
                           specs=[[{"type": "table"}, {"type": "table"}, {
                               "type": "table"}, {"type": "table"}]],
                           subplot_titles=["Portieri", "Difensori",
                                           "Centrocampisti", "Attaccanti"])
    fig.update_layout(title_text="Media Fantavoto dei migliori Giocatori con " +
                      f"almeno 5 presenze nella Lega, aggiornato alla {giornate}° Giornata")
    fig = add_trace_migliori_giocatori(fig, dfPortieri, 1, 1)
    fig = add_trace_migliori_giocatori(fig, dfDifensori, 1, 2)
    fig = add_trace_migliori_giocatori(fig, dfCentrocampisti, 1, 3)
    fig = add_trace_migliori_giocatori(fig, dfAttaccanti, 1, 4)
    fig.show()

    print("Plot delle tabelle migliori giocatori\n")
