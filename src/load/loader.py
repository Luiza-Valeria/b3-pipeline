import pandas as pd
import os
from datetime import datetime

def load_trusted(ticker: str) -> pd.DataFrame:
    """
    Carrega o parquet da camada trusted.
    """
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"data/trusted/{ticker}_{today}.parquet"
    return pd.read_parquet(filename)

def transform_refined(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega e enriquece os dados para análise.
    """
    df["variation_pct"] = ((df["close"] - df["open"]) / df["open"] * 100).round(2)
    df["amplitude"] = (df["high"] - df["low"]).round(2)
    df["ma_7"] = df["close"].rolling(window=7).mean().round(2)
    df["ma_21"] = df["close"].rolling(window=21).mean().round(2)

    return df

def save_refined(df: pd.DataFrame, ticker: str) -> str:
    """
    Salva os dados enriquecidos na camada refined como CSV.
    """
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"data/refined/{ticker}_{today}.csv"
    df.to_csv(filename)
    print(f"Arquivo salvo em: {filename}")
    return filename

if __name__ == "__main__":
    ticker = "PETR4.SAO"
    df = load_trusted(ticker)
    df = transform_refined(df)
    save_refined(df, ticker)
    print(df.tail())