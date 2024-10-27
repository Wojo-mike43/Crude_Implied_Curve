import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt


contracts = ['CLZ24.NYM', 'CLF25.NYM', 'CLG25.NYM', 'CLH25.NYM', 'CLJ25.NYM', 'CLK25.NYM', 'CLM25.NYM',
           'CLN25.NYM', 'CLQ25.NYM', 'CLU25.NYM', 'CLV25.NYM', 'CLX25.NYM', 'CLZ25.NYM', 'CLF26.NYM', 'CLG26.NYM',
           'CLH26.NYM', 'CLJ26.NYM', 'CLK26.NYM', 'CLM26.NYM', 'CLN26.NYM', 'CLQ26.NYM', 'CLU26.NYM', 'CLV26.NYM']


#Contracts Data
crude_data = {}

for contract in contracts:
    try:
        ticker = yf.Ticker(contract)

        price = ticker.info.get('previousClose')
        expo = dt.datetime.fromtimestamp(ticker.info.get('expireDate'))
        crude_data[contract] = {'quote': price, 'expiration': expo}

    except (KeyError, AttributeError, TypeError) as e:
        print(f"Error for Ticker: {contract} {e} ")

crude_df = pd.DataFrame.from_dict(crude_data, orient='index')

#Solving for Implied Forward Rate Cruve
today = dt.datetime.today()
crude_df['year_diff'] = ((crude_df['expiration'] - today).dt.days) / 365

crude_df['imp_rates'] = ((crude_df['quote'] / crude_df['quote'].shift(1)) **
                         (1 / (crude_df['year_diff'] - crude_df['year_diff'].shift(1)))) - 1

crude_df = crude_df.dropna()


#Plot
plt.plot(crude_df['year_diff'], crude_df['imp_rates'], marker='o', linestyle='-', color='b', label='Implied Forward Rate')
plt.xlabel('Time to Maturity in Years')
plt.ylabel('Implied Forward Rates')
plt.title('Crude Oil - Implied Forward Rates')

plt.grid(True)
plt.legend()
plt.show()
