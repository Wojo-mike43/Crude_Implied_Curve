# Crude_Implied_Curve

This is a small project that calculates an implied forward rate curve using Crude Oil futures for the next two years. This project uses `yfinance`, `pandas`, and `matplotlib`. The goal of this project is to utilize yfinance to visualize the forward rate curve based on the price and expiration of several contracts. 

## How It Works:

- **Contract Tickers:**  
  Tickers are pre-loaded into the code via a Python list.

- **Contract Data:**  
  Using `yfinance`, information about each contract is fetched. Specifically, each contract’s last closing price and expiration date are saved to a dictionary.

- **Forward Rate Calculation:**  
  The dictionary is converted to a `pandas` DataFrame, with each ticker serving as the index. The dates between the current day and the day of expiration are calculated. The implied forward rate curve is constructed using the contracts' last closing prices and their time-to-maturity.

- **Plotting:**  
  `matplotlib` is used to plot the implied rate curve.
