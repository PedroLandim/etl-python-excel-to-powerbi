import pandas as pd

def corrigir_dados(df):
    df = df.copy()

    df["Amount_spent"] = df["Amount_spent"].clip(lower=0)
    df["Link_clicks"] = df["Link_clicks"].clip(upper=df["Impressions"])
    df["Conversions"] = df["Conversions"].clip(upper=df["Link_clicks"])

    return df
