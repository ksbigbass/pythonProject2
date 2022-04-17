# -*- coding: utf-8 -*-
from xmlrpc.client import DateTime

import compareSyms

"""
Created on Fri Mar 25 13:53:20 2022

@author: ksbig
"""
import plotly.express as px
import plotly.graph_objects as go
import re
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import alpaca_trade_api as tradeapi
from bs4 import BeautifulSoup
import requests
import csv
import datetime
from datetime import timedelta
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 50)
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
account = api.get_account()

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


  

def sell_list_order(sym):
    qty = api.get_asset(sym)
    print(qty)
    # for stock in lst:
    #     api.submit_order(stock, qty=qty, side='buy', type='market', time_in_force='day')

    # return print(api.list_orders(status='open', limit=len(lst), nested=True))


def  stop_loss_order(lst,qty=10): #We could buy a position and add a stop-loss and a take-profit of 5 %
    

    for stock in lst:

        symbol = 'stock'
        symbol_bars = api.get_bars_iter(symbol, 'minute', 1).df.iloc[0]
        symbol_price = symbol_bars[symbol]['close']

        api.submit_order(
        symbol=symbol,
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc',
        order_class='oto',
        stop_loss={'stop_price': symbol_price * 0.95}
    )
        


def get_active_orders():
    return (print(api.list_orders(status='open', limit=25, nested=True)))


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
        xaxis_title=start + ' ' + end,
        yaxis_title="Price {0}".format(api.get_bars(sym, timeframe)))
    candlestick_fig.show()


def make_order(sym):
    last_price= api.get_latest_trade(sym).price
    bal = float(account.last_equity)
    print(bal)
    qty = bal *.03 // last_price
    position = int(api.get_position(sym).qty)
     
    api.submit_order(sym, qty, side='buy', type='market', time_in_force='day')
    print(f"Balance was {bal} and you just placed a BUY order for {qty} shares of {sym}")

    # return print(api.list_orders(status='open', limit=1, nested=True))

def make_order_lst(lst):
    for sym in lst:

        my_positions = api.list_positions()
        my_positions_df = pd.DataFrame([position._raw for position in my_positions])
        my_positions_df.set_index('symbol', inplace=True)
        
        last_price= api.get_latest_trade(sym).price

        bal = float(account.last_equity)
        qty2 = bal *.03 // last_price
        position = int(api.get_position(sym).qty)

    # Then check if a particular stock is in the index
    if sym in my_positions_df.index:
        qty = float(my_positions_df.at[sym, 'qty'])

    else:
        qty = 0

#     for sym in lst:
#         try:
#             api.submit_order(sym, qty, side='buy', type='market', time_in_force='day')

#         except:
#             print('E')

#         else:
#             print(f"Balance was {bal} and you just placed a BUY order for {qty} shares of {sym}")

  
# make_order_lst(['OILU', 'LXU', 'CRGY', 'BPT',  'SGML',   'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV',   'AR', 'UAN'])




# sym = 'LXU'
# timeframe = '1Day'
# start = '2022-04-05'
# end = '2022-04-06'

# pos = api.get_position(sym)
# print(pos)





# make_order(sym)





# x = api.get_bars(sym, timeframe, start, end).df
# plot_sym(x)
# print(scrapeSyms.strongDf)


# p = api.get_bars("AAPL", TimeFrame.Day, end, end, adjustment='raw').df
#
# print(p.loc[:,'close'])

# test1 =['LXU', 'NRGV', 'SGML', 'SGLY', 'BPT', 'ZETA',   'IPI', 'THRX',  'NRT', 'OILU', 'MYNA', 'BTU' ]
# # stop_loss_order(buys)
# balance_change = float(account.equity) - float(account.last_equity)
# bal = float(account.last_equity)
# print(f'Today\'s portfolio balance change: ${balance_change}')
# print(bal)
# print(scrapeSyms.strong)
# make_order(['OILU', 'LXU', 'CRGY', 'BPT',  'SGML',   'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV',  'AR', 'UAN'])
# # x = api.get_bars(sym, timeframe, start, end).df
# sell_list_order(sym)

 