import pandas as pd
import scrapeSyms
import datetime as dt


sell = []
sdf = pd.DataFrame(scrapeSyms.strongDf)

def create_sell_list(lst):
    for stock in lst:
        if stock not in scrapeSyms.strong:
            sell.append(stock)


def create_count(lst):
    try:
        for stock in lst:
            if stock in scrapeSyms.strong:
                print(stock)
                
        
          

    except:
        print('error')



    


lst = ['OILU', 'LXU', 'CRGY', 'BPT', 'CHKEL', 'SGML', 'CHKEZ', 'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV', 'CHKEW', 'AR', 'UAN']

# create_sell_list()

# print(sell)

# create_sell_list(sellTestA)
