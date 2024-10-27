# Crude_Implied_Curve
This is a small project that calculates an implied forward rate curve using Crude Oil futures for the next two years. This project requires yfinance, pandas, and matplotlib. The goal of this project is to utilize yfinance to visualize the forward rate curve based on the price and expiration of several contracts. 

**How it works:**
Contract Tickers: Tickers are pre-loaded into the code via a Python list.
Contract Data: Using yfinance, information about each contract is fetched, specifically each contract’s last closing price and expiration date are saved to a dictionary.
Forward Rate Calculation: The dictionary is then converted to a pandas data frame, with each ticker serving as the index. In this datafame, the dates between the current day and the day of expiration are calculated. The Implied forward rate curve is constructed for the contracts using their last closing price and time-to-maturity.
Plotting: Matplotlib is used to plot the rate curve.
