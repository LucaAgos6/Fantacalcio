import plotly.graph_objects as go
import pandas as pd


def utils_bonus_ruoli(df, ruolo):

    df1 = df[df["Ruolo"] == ruolo]
    voto = df1.groupby("Fantagiocatore")["Voto"].mean().round(2)
    fantavoto = df1.groupby("Fantagiocatore")["Fantavoto"].mean().round(2)
    df1 = pd.DataFrame(voto)
    df1["Fantavoto"] = fantavoto
    df1["Differenza"] = round(fantavoto - voto, 2)
    df1 = df1.sort_values(by="Fantavoto", ascending=False)

    return df1


def add_trace_bonus_ruoli(fig, df, row, col):

    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore", "Voto",
                                               "Fantavoto", "Differenza"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(values=[df.index,
                                              df["Voto"],
                                              df["Fantavoto"],
                                              df["Differenza"]]),
                           columnwidth=[2, 1, 1, 1]), row=row, col=col)

    return fig


def utils_modificatore(lista):

    df1 = pd.DataFrame(lista, columns=["Nome", "Modificatore", "Modulo"])
    modificatore = df1.groupby("Nome")["Modificatore"].mean().round(2)
    num = df1.groupby("Nome")["Modificatore"].count()
    df1 = pd.DataFrame(modificatore)
    df1["Modificatore"] = modificatore
    df1["Giornate"] = num
    df1 = df1.sort_values(by="Modificatore", ascending=False)

    return df1


def add_trace_modificatore(fig, df, row, col):

    fig.add_trace(go.Table(header=dict(values=("Fantagiocatore",
                                               "Media Modificatore",
                                               "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(
                               values=[df.index,
                                       df["Modificatore"],
                                       df["Giornate"]]),
                           columnwidth=[2, 1]), row=row, col=col)

    return fig


def utils_migliori_giocatori(df, ruolo, pres):

    df1 = df[df["Ruolo"] == ruolo]
    fantavoto = df1.groupby(["Giocatore"])["Fantavoto"].mean()
    fantavoto = fantavoto.sort_values(ascending=False).round(2)
    num = df1.groupby("Giocatore")["Fantavoto"].count()
    df1 = pd.DataFrame(fantavoto)
    df1["Fantavoto"] = fantavoto
    df1["Giornate"] = num
    df1 = df1[df1["Giornate"] >= pres]
    df1 = df1[:28]

    return df1


def add_trace_migliori_giocatori(fig, df, row, col):

    fig.add_trace(go.Table(header=dict(values=("Giocatore",
                                               "Fantamedia",
                                               "N° Giornate"),
                                       fill_color="paleturquoise",
                                       line_color="darkslategray"),
                           cells=dict(
                               values=[df.index,
                                       df["Fantavoto"],
                                       df["Giornate"]]),
                           columnwidth=[2, 1, 1.3]), row=row, col=col)

    return fig
