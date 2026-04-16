# Stock Market Dashboard

## Authors
- Zaki Sheikh

## Project Description
This project is a stock market dashboard built in Python that allows users to look up and explore historical stock data for any publicly traded company. The goal is to make it easy to search for a stock ticker and see how that stock has performed over a selected time period. The program uses the Yahoo Finance API to pull real data from the internet without requiring an API key. The data is saved locally as CSV files so it can be analyzed without having to re-fetch it every time. The final result is a visual interface where users can interact with the data through charts and statistics generated with Matplotlib.

## Project Outline/Plan

### Interface Plan
- Tkinter GUI with a main home screen and a popup window for displaying charts
- Text box to enter a stock ticker symbol (e.g. AAPL, TSLA)
- Dropdown menu to select a date range (1 month, 3 months, 6 months, 1 year)
- Button to fetch and load the stock data
- Popup window that displays the chart and key statistics (high, low, average)

### Data Collection and Storage Plan
- Use the `yfinance` library to pull historical stock price data from Yahoo Finance
- Data will include open, close, high, low prices and volume for each trading day
- Retrieved data will be saved locally as CSV files organized by ticker symbol and date range
- If a CSV file already exists for the selected ticker and range, it will be loaded directly instead of re-fetching

### Data Analysis and Visualization Plan
- Load the CSV data into Python using Pandas for cleaning and structuring
- Use NumPy to calculate moving averages and overall price trends
- Use Matplotlib to generate a time series plot of closing prices
- Display summary statistics (average price, highest price, lowest price) in the popup window
- The chart will update dynamically based on the user's selected ticker and date range

## Installation
```
pip install yfinance pandas numpy matplotlib
```
Then run:
```
python main.py
```

## Future Improvements
- Add support for comparing multiple stocks on the same chart
- Include volume as a secondary plot below the price chart
- Add technical indicators such as RSI or Bollinger Bands
- Allow users to export the chart as an image file
- Add a watchlist feature to save favorite tickers
