from prefect import flow, task
from src.ingestion.extractor import fetch_daily_data, save_raw
from src.transformation.transformer import load_raw, transform, save_trusted
from src.load.loader import load_trusted, transform_refined, save_refined
import os
from dotenv import load_dotenv

load_dotenv()

@task(name="Extrair dados da API")
def extract(ticker: str):
    data = fetch_daily_data(ticker)
    save_raw(data, ticker)
    return ticker

@task(name="Transformar dados brutos")
def transform_data(ticker: str):
    data = load_raw(ticker)
    df = transform(data, ticker)
    save_trusted(df, ticker)
    return ticker

@task(name="Carregar dados refinados")
def load_data(ticker: str):
    df = load_trusted(ticker)
    df = transform_refined(df)
    save_refined(df, ticker)
    return ticker

@flow(name="Pipeline B3 - PETR4")
def pipeline(ticker: str = "PETR4.SAO"):
    ticker = extract(ticker)
    ticker = transform_data(ticker)
    ticker = load_data(ticker)
    print(f"Pipeline finalizado com sucesso para {ticker}")

if __name__ == "__main__":
    ticker = os.getenv("TICKER", "PETR4.SAO")
    pipeline(ticker)