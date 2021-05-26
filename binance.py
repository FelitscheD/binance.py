import os
from binance.client import Client
import json
import pprint
from os import system
from tabulate import tabulate
import requests
from requests_toolbelt.utils import dump
system('clear')

#Binance API
api_key = 'your api key'
api_secret = 'your api secret'
client = Client(api_key, api_secret)

#Farben
color_red='\033[1;31;40m'
color_green='\033[1;32;40m'
color_yellow='\033[1;33;40m'
color_dark_gray='\033[1;30;40m'
color_purple='\033[1;35;40m'
color_blue='\033[1;34;40m'
color_cyan='\033[1;36;40m'
reset='\033[0m'

#Datum und Uhrzeit
import datetime
d = datetime.datetime.today()
dateTimeNow = d.strftime("%d-%B-%Y %H:%M:%S")
#print(dateTimeNow,)
#print("------------------------------")
#Kurse

btc_price=client.get_symbol_ticker(symbol="BTCEUR")
btc_preis=float(btc_price["price"])
#print(color_yellow)
#print("Bitcoin", round(btc_preis, 2),"€",reset)
#print(" ")
eth_price=client.get_symbol_ticker(symbol="ETHBTC")
eth_preis=float(eth_price["price"])
eth_eur=round(eth_preis * btc_preis, 2)
#print("Ethereum", round(eth_preis, 2),"BTC")

iota_price=client.get_symbol_ticker(symbol="IOTABTC")
iota_preis=float(iota_price["price"])
iota_eur=round(iota_preis * btc_preis, 2)
#print("IOTA", round(iota_preis, 2),"BTC")

bnb_price=client.get_symbol_ticker(symbol="BNBBTC")
bnb_preis=float(bnb_price["price"])
bnb_eur=round(bnb_preis * btc_preis, 2)
#print("Binance Coin", round(bnb_preis, 2),"BTC")

doge_price=client.get_symbol_ticker(symbol="DOGEBTC")
doge_preis=float(doge_price["price"])
doge_eur=round(doge_preis * btc_preis, 2)
#print("Dogecoin", round(doge_preis, 2),"BTC")

ada_price=client.get_symbol_ticker(symbol="ADABTC")
ada_preis=float(ada_price["price"])
ada_eur=round(ada_preis * btc_preis, 2)
#print("Dogecoin", round(doge_preis, 2),"BTC")

#Wallet
btc_account=client.get_asset_balance(asset='BTC')
btc_guthaben=float(btc_account["free"])
btc_euro=round(btc_guthaben * btc_preis, 2)

eth_account=client.get_asset_balance(asset='ETH')
eth_guthaben=float(eth_account["free"])
eth_btc=eth_guthaben * eth_preis
eth_euro=round(eth_btc * btc_preis, 2)
#print("ETH"," ",round(eth_eur, 2),"€","  ", round(eth_euro, 2), "€")

iota_account=client.get_asset_balance(asset='IOTA')
iota_guthaben=float(iota_account["free"])
iota_btc=iota_guthaben * iota_preis
iota_euro=round(iota_btc * btc_preis, 2)
#print("IOTA"," ",round(iota_eur, 2),"€","  ", round(iota_euro, 2), "€")

bnb_account=client.get_asset_balance(asset='BNB')
bnb_guthaben=float(bnb_account["free"])
bnb_btc=bnb_guthaben * bnb_preis
bnb_euro=round(bnb_btc * btc_preis, 2)
#print("BNB"," ",round(bnb_eur, 2),"€","  ", round(bnb_euro, 2), "€")

doge_account=client.get_asset_balance(asset='DOGE')
doge_guthaben=float(doge_account["free"])
doge_btc=doge_guthaben * doge_preis
doge_euro=round(doge_btc * btc_preis, 2)
#print("DOGE"," ",round(doge_eur, 2),"€","  ", round(doge_euro, 2), "€")

ada_account=client.get_asset_balance(asset='ADA')
ada_guthaben=float(ada_account["free"])
ada_btc=ada_guthaben * ada_preis
ada_euro=round(ada_btc * btc_preis, 2)

#Binance Ticker

#Bitcoin 24h ticker
btc_price_change=requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=BTCEUR')
btc_price_change_data=btc_price_change.json()
btc_24hr=round(float(btc_price_change_data["priceChangePercent"]), 2)

#Ethereum 24h ticker
eth_price_change=requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=ETHEUR')
eth_price_change_data=eth_price_change.json()
eth_24hr=round(float(eth_price_change_data["priceChangePercent"]), 2)

#Iota 24h ticker
iota_price_change=requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=IOTABTC')
iota_price_change_data=iota_price_change.json()
iota_24hr=round(float(iota_price_change_data["priceChangePercent"]), 2)

#Binance Coin 24h ticker
bnb_price_change=requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=BNBEUR')
bnb_price_change_data=bnb_price_change.json()
bnb_24hr=round(float(bnb_price_change_data["priceChangePercent"]), 2)

#Dogecoin 24h ticker
doge_price_change=requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=DOGEEUR')
doge_price_change_data=doge_price_change.json()
doge_24hr=round(float(doge_price_change_data["priceChangePercent"]), 2)

#ADA 24h ticker
ada_price_change=requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=ADAEUR')
ada_price_change_data=ada_price_change.json()
ada_24hr=round(float(ada_price_change_data["priceChangePercent"]), 2)

#Tabelle
d = [ ["BTC", btc_preis, btc_euro, btc_24hr],
     ["ETH", eth_eur, eth_euro, eth_24hr],
     ["IOTA", iota_eur, iota_euro, iota_24hr],
     ["BNB", bnb_eur, bnb_euro, bnb_24hr],
     ["DOGE", doge_eur, doge_euro, doge_24hr],
     ["ADA", ada_eur, ada_euro, ada_24hr]]

print(tabulate(d, headers=["Kry/€", "Kurs", "Asset", "%"]))

#print(" ")
print("----------------------------------")
#print(" ")
gesamt=round((btc_euro + eth_euro + iota_euro + bnb_euro + doge_euro + ada_euro), 2)
zins=round(gesamt-2600.00, 2)
zins_percent=round((zins/gesamt)*100, 2)

print
if gesamt < 2600:
        print(color_red)
        print("Σ", gesamt,"€","|",zins, "€","|",zins_percent,"%",reset)
elif gesamt > 2600:
        print(color_green)
        print("Σ", gesamt,"€","|","+",zins, "€","|",zins_percent,"%",reset)




