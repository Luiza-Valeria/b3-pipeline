import pytest
import pandas as pd
from src.transformation.transformer import transform

# Dado falso simulando o retorno da API
MOCK_DATA = {
    "Meta Data": {
        "2. Symbol": "PETR4.SAO"
    },
    "Time Series (Daily)": {
        "2026-06-25": {
            "1. open": "38.1200",
            "2. high": "38.6700",
            "3. low": "37.9200",
            "4. close": "38.4500",
            "5. volume": "25132000"
        },
        "2026-06-24": {
            "1. open": "38.9000",
            "2. high": "38.9800",
            "3. low": "38.1300",
            "4. close": "38.2900",
            "5. volume": "59191400"
        }
    }
}

def test_transform_retorna_dataframe():
    df = transform(MOCK_DATA, "PETR4.SAO")
    assert isinstance(df, pd.DataFrame)

def test_transform_colunas_corretas():
    df = transform(MOCK_DATA, "PETR4.SAO")
    colunas_esperadas = ["open", "high", "low", "close", "volume", "ticker"]
    assert list(df.columns) == colunas_esperadas

def test_transform_tipos_corretos():
    df = transform(MOCK_DATA, "PETR4.SAO")
    assert df["open"].dtype == float
    assert df["volume"].dtype == int

def test_transform_ordenado_por_data():
    df = transform(MOCK_DATA, "PETR4.SAO")
    assert df.index[0] < df.index[1]

def test_transform_ticker_correto():
    df = transform(MOCK_DATA, "PETR4.SAO")
    assert df["ticker"].unique()[0] == "PETR4.SAO"