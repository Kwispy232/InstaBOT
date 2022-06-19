from pip import main
import requests

def getTextQuote():
    url = 'https://quotes.rest/qod'
    response = requests.get(url)
    quotes = response.json()['contents']['quotes'][0]
    return quotes["quote"], quotes["author"]
