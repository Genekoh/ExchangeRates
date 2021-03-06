from dotenv import load_dotenv
import utils
import os
import requests

load_dotenv()  # Load Environment Variables from .env file

API_URL = "http://api.exchangeratesapi.io/v1/"
API_KEY = os.environ["API_KEY"]

# General use function for sending requests to API in a specific format
def sendRequest(endpoint, params={}):
    params["access_key"] = API_KEY
    print(params)
    r = requests.get(f"{API_URL}{endpoint}", params=params)
    return r


# Get all the currencies three letter symbols
def getCurrencySymbols():
    endpoint = "symbols"
    r = sendRequest(endpoint)
    symbols_dict = r.json()["symbols"]

    return symbols_dict.keys()


# Get all the full names of currencies
def getCurrencyNames():
    endpoint = "symbols"
    r = sendRequest(endpoint)
    symbols_dict = r.json()["symbols"]

    return symbols_dict.values()


# Get the exchange rates of a list of symbols
def getExchangeRates(symbols):
    endpoint = "latest"

    symbols_string = (
        utils.listToCommaSepString(symbols) if (isinstance(symbols, list)) else symbols
    )

    print("hi", symbols_string)

    r = sendRequest(endpoint, params={"symbols": symbols_string})
    print(r.json())
    rates = r.json()["rates"]

    return rates


# Convert Rates of two currencies using EUR for comparison
def convertRates(base, to):
    r = getExchangeRates([base, to])

    baseRate = r[base] if (base != "EUR") else 1
    toRate = r[to] if (to != "EUR") else 1

    finalRate = round(toRate / baseRate, 2)
    return finalRate
