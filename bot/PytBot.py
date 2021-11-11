import json
from binance.client import Client
from binance.enums import ORDER_TYPE_TAKE_PROFIT
import pandas as pd
import re
from colorama import init, Fore
init()

datajson = {}

client = Client('STxr02bhTKkhYIDfUcfBONn55IS5zroXmL08SFyyRJPiE8R66U1hmPFp3gPBYnHd'
,'PncjNDFluWKxGKwMO2ibYaIFkxZc3tcJGJup6XrMXyShOa3XSSqaJzEGjE3MOz88', tld = 'com')


def busd_par_filter():
    BUSD_PARES = []
    info = client.get_all_tickers()
    for i in range(len(info)):
        result = str((info[i].get('symbol', 'aa'))).find("USDT")
        if result > -1 :
            BUSD_PARES.append((str((info[i].get('symbol', 'aa')))))
        else:
            pass
        i = i+1

    return(BUSD_PARES)


def sma_1H(periodo, ticker):

    data_historical = client.get_historical_klines(ticker, Client.KLINE_INTERVAL_1HOUR,'203 hour ago UTC ')

    #print ("cantidad de velas: ", len(data_historical))

    sumatoria = 0
    if len(data_historical) < 200:
        print("PAR INVALIDO")

    elif len(data_historical) == 200:
        print("se obtuvieron las velas correctamente")
        for i in range((200 - periodo ), 200):
            #print(data_historical[i])
            sumatoria += float(data_historical[i][4])
        sma = (sumatoria/ periodo)
        print("SMA: " + ticker + " Periodo: " + str(periodo) + " " + str(sma) )

        return(sma)

    else:
        pass


BUSD_PARES = busd_par_filter()
#print(BUSD_PARES)

for i in range(len(BUSD_PARES)):

    sma4 = sma_1H(4,BUSD_PARES[i])
    sma9 = sma_1H(9,BUSD_PARES[i])
    sma18 = sma_1H(18,BUSD_PARES[i])
    
    if sma4 == None or sma9 == None or sma18 == None:
       print("Par de datos no valido " + BUSD_PARES[i])

    elif sma4 > sma9 and sma4 > sma18:
        print(Fore.GREEN + "triple cruce detectado en el par " + str(BUSD_PARES[i]) + Fore.RESET)
        datajson[i] = (BUSD_PARES[i])

        with open('data.json', 'w') as file:
            json.dump(datajson, file, indent=4)
    else:
        pass
    i = i+1

    