import pandas as pd

import alpaca_interface
import scrapeSyms

sell = []
sdf = pd.DataFrame
sdf = scrapeSyms.strongDf.merge
    # (scrapeSyms.strongDf,columns=['date','sym','count'])

def create_sell_list(lst):
    for stock in lst:
        if stock not in scrapeSyms.strong:
            sell.append(stock)



def add_to_dataframe():

    # sdf.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

