import pandas as pd
import scrapeSyms

sell = []
sdf = pd.DataFrame(scrapeSyms.strongDf)

def create_sell_list(lst):
    for stock in lst:
        if stock not in scrapeSyms.strong:
            sell.append(stock)


# def create_count(df):
#     for label, content in df.items():
#        print(f'label: {label}')
#        print(f'content: {content}', sep='\n')
sellTestA = ['LXU', 'NRGV', 'SGML', 'SGLY', 'BPT', 'ZETA',   'IPI', 'THRX',  'NRT', 'OILU', 'MYNA', 'BTU','EMBK','TSLA' ]
sellTestB = ['OILU', 'LXU', 'CRGY', 'BPT',  'SGML', 'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV', 'AR', 'UAN']


# create_sell_list(sellTestA)

# print(sell)

create_sell_list(sellTestB)
# print(sell)

