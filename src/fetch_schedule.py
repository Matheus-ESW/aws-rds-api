from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os
import schedule
import time
import csv

load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'symbol': 'BTC',
    'convert': 'BRL'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY'),
}

session = Session()
session.headers.update(headers)

def persist_data_csv():

    csv_path = "csv_data/bitcoin.csv"

    # Verifica se já existe (para decidir se escreve o cabeçalho)
    arquivo_existe = os.path.exists(csv_path)

    with open(csv_path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=brl_quote.keys())

        # Se o arquivo não existia, escreve o cabeçalho
        if not arquivo_existe:
            writer.writeheader()

        # Escreve uma linha com os dados da cotação
        writer.writerow(brl_quote)

    print("Linha adicionada ao CSV!")
            


def consultar_cotacao_bitcoin():

    try:
        response = session.get(url=url, params=parameters)
        data = json.loads(response.text)

        if 'data' in data and 'BTC' in data['data']:

            btc_data = data["data"]["BTC"]
            brl_quote = btc_data["quote"]["BRL"]

            print(f"Última cotação do Bitcoin: ${brl_quote["price"]:.2f} BRL")
            print(f"Volume 24H: ${brl_quote["volume_24h"]:.2f} BRL")
            print(f"Market Cap: ${brl_quote["market_cap"]:.2f} BRL")
            print(f"Última atualização: {brl_quote["last_updated"]}")

            persist_data_csv()

        else:
            print("Erro ao obter a cotação do Bitcoin: ", data['status'].get('error_message', 'Erro desconhecido'))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro na requisição: {e}")

schedule.every(15).seconds.do(consultar_cotacao_bitcoin)

print("Iniciando o agendamento para consultar a API a cada 15 segundos..")
while True:
    schedule.run_pending()
    time.sleep(1)