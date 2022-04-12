import pandas as pd
import scrapeSyms

sell = []
sdf = pd.DataFrame(scrapeSyms.strongDf)

def create_sell_list(lst):
    for stock in lst:
        if stock not in lst:
            sell.append(stock)


# def create_count(df):
#     for label, content in df.items():
#        print(f'label: {label}')
#        print(f'content: {content}', sep='\n')
