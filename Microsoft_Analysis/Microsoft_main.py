from stocker import Stocker

microsoft = Stocker('MSFT')
#MSFT Stocker Initialized. Data covers 1986-03-13 to 2018-01-16.
stock_history = microsoft.stock
print(stock_history.tail())


import matplotlib.pyplot as plt
microsoft.plot_stock()
"""
Maximum Adj. Close = 96.77 on 2018-03-12 00:00:00.
Minimum Adj. Close = 0.06 on 1986-03-24 00:00:00.
Current Adj. Close = 89.47 on 2018-03-27 00:00:00.
"""

microsoft.plot_stock(start_date = '2000-01-03',  end_date = '2018-01-16',  stats = ['Daily Change', 'Adj. Volume'],  plot_type='pct')
"""
Maximum Daily Change = 2.08 on 2008-10-13.
Minimum Daily Change = -3.34 on 2017-12-04.
Current Daily Change = -1.75.

Maximum Adj. Volume = 591052200.00 on 2006-04-28.
Minimum Adj. Volume = 7425503.00 on 2017-11-24.
Current Adj. Volume = 35945428.00.
"""

microsoft.buy_and_hold(start_date='1986-03-13', 
                       end_date='2018-01-16', nshares=100)

"""
MSFT Total buy and hold profit from 1986-03-13 00:00:00 to 2018-01-16 00:00:00 for 100 shares = $8829.11
"""

microsoft.buy_and_hold(start_date='1999-01-05', 
                      end_date='2002-01-03', nshares=100)
                      
"""
MSFT Total buy and hold profit from 1999-01-05 to 2002-01-03 for 100 shares = $-56.92
"""

model, model_data = microsoft.create_prophet_model()

# model and model_data are from previous method call
model.plot_components(model_data)

plt.show()


print(microsoft.weekly_seasonality)
microsoft.weekly_seasonality = True
print(microsoft.weekly_seasonality)


microsoft.changepoint_date_analysis()
"""
Changepoints sorted by slope rate of change (2nd derivative):

          Date  Adj. Close     delta
48  2015-03-30   38.238066  2.580296
337 2016-05-20   48.886934  2.231580
409 2016-09-01   55.966886 -2.053965
72  2015-05-04   45.034285 -2.040387
313 2016-04-18   54.141111 -1.936257
"""

# same method but with a search term
microsoft.changepoint_date_analysis(search = 'Microsoft profit')
"""
Top Related Queries: 

                  query  value
0  microsoft non profit    100
1      microsoft office     55
2                 apple     30
3         microsoft 365     30
4  microsoft office 365     20

 Rising Related Queries: 

                   query  value
0          microsoft 365    120
1   microsoft office 365     90
2  microsoft profit 2014     70
"""
microsoft.changepoint_date_analysis(search = 'Microsoft Office')



# specify number of days in future to make a prediction
model, future = microsoft.create_prophet_model(days=180)
#Predicted Price on 2018-07-15 = $97.67