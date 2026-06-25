import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def fetch_daily_data(ticker: str) -> dict:
    """
    Busca dados diários de uma ação na Alpha Vantage.
    Retorna o JSON bruto da API.
    """
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": API_KEY,
        "outputsize": "compact"
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    return response.json()


def save_raw(data: dict, ticker: str) -> str:
    """
    Salva o JSON bruto na camada raw.
    Retorna o caminho do arquivo salvo.
    """
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"data/raw/{ticker}_{today}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Arquivo salvo em: {filename}")
    return filename


if __name__ == "__main__":
    ticker = os.getenv("TICKER", "PETR4.SAO")
    data = fetch_daily_data(ticker)
    save_raw(data, ticker)