import requests


def convert():
    endpoint = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/gbp.json"
    response = requests.get(endpoint)
    data = response.json()
    return data["gbp"]["usdt"]


print(convert())