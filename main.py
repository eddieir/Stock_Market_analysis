import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas_datareader
import datetime

import pandas_datareader.data as web

start = datetime.datetime(2012,1,1)
end = datetime.datetime.now()

tesla = web.DataReader('TSLA','yahoo',start,end)

print(tesla.head())

ford = web.DataReader('FORD','yahoo',start,end)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print(ford)

GM = web.DataReader('GM','yahoo',start,end)
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print(GM)

#Plot based on the opening prices
"""tesla['Open'].plot(label='Tesla',figsize=(16,8), title="Open price")
ford['Open'].plot(label='FORD')
GM['Open'].plot(label='GM')
plt.legend();
plt.savefig("openPrices.png")


#plot based on the adjuced closing prirces
tesla['Adj Close'].plot(label='Tesla',figsize=(16,8), title="Adj Close price")
ford['Adj Close'].plot(label='FORD')
GM['Adj Close'].plot(label='GM')
plt.legend();
plt.savefig("AdjClosePrices.png")
"""

#put the  volume of stock for every day 
"""tesla['Volume'].plot(label='Tesla',figsize=(16,8), title="Volume")
ford['Volume'].plot(label='FORD')
GM['Volume'].plot(label='GM')
plt.legend();
plt.savefig("Volume.png")
"""
# What are the dates of maximum trading volumes for each?
print(ford['Volume'].idxmax())
print(tesla['Volume'].idxmax())
print(GM['Volume'].idxmax())

#dollars traded for the day 
tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
GM['Total Traded'] = GM['Open'] * GM['Volume']
ford['Total Traded'] = ford['Open'] * ford['Volume']

tesla['Total Traded'].plot(label = 'Tesla' , figsize=(16,8))
ford['Total Traded'].plot(label='ford')
GM['Total Traded'].plot(label='GM')
'''plt.legend()
plt.ylabel('Total Traded')
plt.savefig('TotalTraded.png')
'''
print(tesla['Total Traded'].idxmax())

#Let's plot the moving average
GM['MA50'] = GM['Open'].rolling(50).mean()
GM['MA200'] = GM['Open'].rolling(200).mean()
GM[['Open','MA50','MA200']].plot(label='GM',figsize=(20,15))
plt.savefig('MA_GM.png')


from pandas.plotting import scatter_matrix
car_comp = pd.concat([tesla['Close'],ford['Close'],GM['Close']],axis=1)
car_comp.columns=['Tesla Close','Ford Close','GM Close']
#scatter_matrix(car_comp,figsize=(10,10),alpha=0.1,hist_kwds={'bins':50})
#plt.savefig('scatter_matrix.png')




#Basic financial analysis, by calculating and comparing daily returns, and plotting it to identify relationships.
tesla['returns'] = tesla['Close'].pct_change(1) 
ford['returns'] = ford['Close'].pct_change(1)
GM['returns'] = GM['Close'].pct_change(1)

print(tesla.head())

ford['returns'].hist(bins=100,label='FORD',alpha=0.5)
GM['returns'].hist(bins=100,label='GM',alpha=0.5)
tesla['returns'].hist(bins=100,label='TESLA',alpha=0.5)
#plt.legend()
#plt.savefig("CompareDailyReturns.png")


"""
Cumulative Daily Returns

Daily Return: Daily return is the profit/loss made by the stock compared to the previous day.

Cumulative Return: Cumulative return is computed relative to the day investment is made. If the cumulative return is above one, you are making profits else you are in loss.

The formula for a cumulative daily return is:

df[daily_cumulative_return] = ( 1 + df[pct_daily_return] ).cumprod()
"""
tesla['Cumulative Return'] = (1+tesla['returns']).cumprod()
GM['Cumulative Return'] = (1+GM['returns']).cumprod()
ford['Cumulative Return'] = (1+ford['returns']).cumprod()


tesla['Cumulative Return'].plot(label='Tesla',figsize=(16,8) , title='Cumulative Return')
GM['Cumulative Return'].plot(label='GM')
ford['Cumulative Return'].plot(label='Ford')
plt.legend()
plt.savefig('CumulativeReturn.png')