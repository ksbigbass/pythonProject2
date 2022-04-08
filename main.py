## -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
from xmlrpc.client import DateTime

"""
Created on Fri Mar 25 13:53:20 2022

@author: ksbig
"""
import plotly.express as px
import plotly.graph_objects as go
# import talib as ta
import re
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import alpaca_trade_api as tradeapi
from bs4 import BeautifulSoup
import requests
import csv
import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os.path
import scrapeSyms

plt.style.use('fivethirtyeight')

base_url = "https://paper-api.alpaca.markets"
# base_url = 'https://data.alpaca.markets/v2'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

API_KEY = 'PKCUQOO80RTR4BF6B6RX'
SECRET_KEY = 'qV55hQoLLxWJhuXWumO9E8v1pTsR5bKKidrMncbZ'

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url, api_version='v2')

weak = scrapeSyms.weak
strong = scrapeSyms.strong


def aplca_data_to_CSV_strong(lst):
    for stock in lst:
        df = api.get_bars(stock, TimeFrame.Day).df

    if os.path.isfile('AlpacaStrongDf.csv') == True:
        df.to_csv('AlpacaStrongDf.csv', index=True, mode='a', header=False)
    else:
        with open('AlpacaStrongDf.csv', 'a') as f:
            df.to_csv('AlpacaStrongDf.csv', mode='a', index=True, header=f.tell() == 0)


def aplca_data_to_CSV_weak(lst):
    for stock in lst:
        df = api.get_bars(stock, TimeFrame.Day).df

    if os.path.isfile('AlpacaWeakDf.csv') == True:
        df.to_csv('AlpacaWeakDf.csv', index=True, mode='a', header=False)
    else:
        with open('AlpacaWeakDf.csv', 'a') as f:
            df.to_csv('AlpacaWeakDf.csv', mode='a', index=True, header=f.tell() == 0)


def make_order(lst, qty=10):
    for stock in lst:
        api.submit_order(stock, qty=qty, side='buy', type='market', time_in_force='day')
        return print(api.list_orders(status='open', limit=len(lst), nested=True))

def get_active_orders():
    return(print(api.list_orders(status='open', limit=25, nested=True)))

def cancel_orders():
    api.cancel_all_orders()


def cancel_specific_order(num):  # ORDER ID Number
    api.cancel_order(num)


def plot_sym(sym):
    candlestick_fig = go.Figure(data=[go.Candlestick(x=sym.index,
                                                     open=sym['open'],
                                                     high=sym['high'],
                                                     low=sym['low'],
                                                     close=sym['close'])])
    candlestick_fig.update_layout(
        title="Candlestick chart for {0}".format(sym),
        xaxis_title= start + ' ' + end,
        yaxis_title="Price {0}".format(api.get_bars(sym,timeframe)))
    candlestick_fig.show()


sym = 'apps'
timeframe = '1Day'
start = '2022-04-05'
end = '2022-04-06'

# x = api.get_bars(sym, timeframe, start, end).df
# plot_sym(x)
# print(strongDf)


p = api.get_bars("AAPL", TimeFrame.Day, end, end, adjustment='raw').df

print(p.loc[:,'close'])

# g = get_active_orders()
# x = cancel_orders()
#
# g = get_active_orders()

# if __name__ == '__main__':
