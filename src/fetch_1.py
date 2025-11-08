from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os
from pprint import pprint

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
        else:
            print("Erro ao obter a cotação do Bitcoin: ", data['status'].get('error_message', 'Erro desconhecido'))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro na requisição: {e}")


consultar_cotacao_bitcoin()