import alpaca_trade_api as tradeapi
import pandas as pd

base_url = "https://paper-api.alpaca.markets"
# base_url = 'https://data.alpaca.markets/v2'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

API_KEY = 'PKCUQOO80RTR4BF6B6RX'
SECRET_KEY = 'qV55hQoLLxWJhuXWumO9E8v1pTsR5bKKidrMncbZ'

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url, api_version='v2')

class AlpacaTrader(object):
    def __init__(self):
        # API authentication keys can be taken from the Alpaca dashboard.
        # https://app.alpaca.markets/paper/dashboard/overview
        self.key_id = API_KEY
        self.secret_key = SECRET_KEY
        self.base_url = 'https://paper-api.alpaca.markets'
        self.account = api.get_account()


        # The symbol we will be trading
        self.symbol = 'TSLA'
        # When this variable is not None, we have an order open
        self.current_order = None

        # The closing price of the last aggregate we saw
        self.last_price = api.get_latest_trade(self.symbol).price

        # The connection to the Alpaca API
        self.api = tradeapi.REST(
            self.key_id,
            self.secret_key,
            self.base_url
        )
        
        # Get our starting position, in case we already have one open
        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            # No position exists
            self.position = 0

        try:
            self.balance = float(self.account.last_equity)
        except:
            self.balance = 0.00

    def set_symbol(self,symbol):
        self.symbol = symbol

    def get_symbol(self):
        return print(self.symbol)         

    def send_order(self, target_qty):
        if self.position == 0:
            api.submit_order(self.symbol, target_qty, side='buy', type='market', time_in_force='day')
            return print ('made order')

         
    def postion_size(self):
        target_qty = self.balance *.03 // self.last_price
        self.send_order(target_qty)

       

        
           
if __name__ == '__main__':
    trader = AlpacaTrader()
    trader.set_symbol('GE')
    trader.get_symbol()
  
    trader.postion_size()
   
