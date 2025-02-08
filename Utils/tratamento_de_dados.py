import pandas as pd
from typing import Union


def filtra_dados(df: pd.DataFrame, estado: str, produto: str):
    if isinstance(estado, str):
        estado = str.upper(estado)
    if isinstance(produto, str):
        produto = str.upper(produto)

    
    df_filtrado = df[df['ESTADO'] == estado]
    df_filtrado = df_filtrado[df_filtrado['PRODUTO'] == produto]


    return df_filtrado

def seleciona_features(df: pd.DataFrame, features: Union[str, list[str]]):

    df_filtrado = df[features]
    return df_filtrado

def trata_datas(df: pd.DataFrame, feature_temporal: Union[str, list[str]]):
    df_filtrado = df.copy()
    if isinstance(feature_temporal, list):
        for feature in feature_temporal:
            df_filtrado[feature] = pd.to_datetime(df[feature])

    if isinstance(feature_temporal, str):
            df_filtrado[feature_temporal] = pd.to_datetime(df[feature_temporal])



    return  df_filtrado


def cria_df_serie_temporal(df: pd.DataFrame):
    df_serie_temporal = df.drop(["NÚMERO DE POSTOS PESQUISADOS","PRODUTO","ESTADO"], axis=1)
    
    df_serie_temporal = df_serie_temporal.rename({"DATA INICIAL":"Data",
                                                  "PREÇO MÉDIO REVENDA": "preco"}, axis=1)
    
    df_serie_temporal = df_serie_temporal.set_index("Data")
    return df_serie_temporal
