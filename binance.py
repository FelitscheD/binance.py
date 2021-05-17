import os
from binance.client import Client
import json
import pprint
from os import system
from tabulate import tabulate
system('clear')

#Binance API
api_key = 'dein_api_key'
api_secret = 'deinapi_secret'
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

#Tabelle
d = [ ["BTC/EUR", btc_preis, btc_euro],
     ["ETH/EUR", eth_eur, eth_euro],
     ["IOTA/EUR", iota_eur, iota_euro],
     ["BNB/EUR", bnb_eur, bnb_euro],
     ["DOGE/EUR", doge_eur, doge_euro]]

print(tabulate(d, headers=["Krypto", "Kurs", "Asset"]))

print(" ")
print("------------------------------")
#print(" ")
gesamt=round((btc_euro + eth_euro + iota_euro + bnb_euro + doge_euro), 2)
print("Gesamt", gesamt, "€")
