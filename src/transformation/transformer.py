import pandas as pd
import json
import os
from datetime import datetime

def load_raw(ticker: str) -> dict:
    """
    Carrega o JSON bruto da camada raw.
    """
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"data/raw/{ticker}_{today}.json"

    with open(filename, "r") as f:
        return json.load(f)

def transform(data: dict, ticker: str) -> pd.DataFrame:
    """
    Transforma o JSON bruto em DataFrame limpo e tipado.
    """
    time_series = data.get("Time Series (Daily)", {})

    df = pd.DataFrame.from_dict(time_series, orient="index")

    df.index = pd.to_datetime(df.index)
    df.index.name = "date"
    df = df.sort_index()

    df.columns = ["open", "high", "low", "close", "volume"]

    df = df.astype({
        "open": float,
        "high": float,
        "low": float,
        "close": float,
        "volume": int
    })

    df["ticker"] = ticker

    return df

def save_trusted(df: pd.DataFrame, ticker: str) -> str:
    """
    Salva o DataFrame limpo na camada trusted como parquet.
    """
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"data/trusted/{ticker}_{today}.parquet"

    df.to_parquet(filename)
    print(f"Arquivo salvo em: {filename}")
    return filename

if __name__ == "__main__":
    ticker = "PETR4.SAO"
    data = load_raw(ticker)
    df = transform(data, ticker)
    save_trusted(df, ticker)
    print(df.head())
    print(df.dtypes)