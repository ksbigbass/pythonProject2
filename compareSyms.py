import pandas as pd
import scrapeSyms
import datetime as dt


sell = []
sdf = pd.DataFrame(scrapeSyms.strongDf)

def create_sell_list(lst):
    for stock in lst:
        if stock not in scrapeSyms.strong:
            sell.append(stock)


def create_count():
    try:
        for stock in scrapeSyms.strong:
            if stock in sdf.loc[sdf['sym']]:
                print('x')
              

        else:
            print('pass')

    except:
        print('error')



            
    # for i, row in sdf.iterrows():
    #     val = row[col]
    #     if val == 0:
    #         val +=1
    #         print(val)

sellTestA = ['LXU', 'NRGV', 'SGML', 'SGLY', 'BPT', 'ZETA',   'IPI', 'THRX',  'NRT', 'OILU', 'MYNA', 'BTU','EMBK','TSLA']
sellTestB = ['OILU', 'LXU', 'CRGY', 'BPT',  'SGML', 'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV', 'AR', 'UAN']


# create_sell_list()

# print(sell)

# create_sell_list(sellTestA)
# print('sell',sell)
# create_count()
# print(sdf)
