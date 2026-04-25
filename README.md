# California Housing Market Dashboard

## Author
- Zaki Sheikh

## Project Description
This project is a California Housing Market Dashboard built in Python that allows users to explore historical housing price data across different regions of California. The program uses the FRED API (Federal Reserve Economic Data) to pull real housing market data directly from the internet. Users can select a region and date range to view how median home prices have changed over time. The data is saved locally as CSV files so it can be analyzed without re-fetching every time. The results are displayed in an interactive Tkinter GUI with charts and statistics generated using Matplotlib.

## Project Outline/Plan

### Interface Plan
- Tkinter GUI with a main home screen and a popup window for displaying charts
- Dropdown menu to select a California region (e.g. San Francisco, Los Angeles, San Diego)
- Dropdown menu to select a date range (1 year, 5 years, 10 years)
- Button to fetch and load the housing data
- Popup window that displays the price trend chart and key statistics (average, min, max price)

### Data Collection and Storage Plan
- Use the FRED API to pull median home price data for California regions
- Data will include monthly median home prices over the selected date range
- Retrieved data will be saved locally as CSV files organized by region and date range
- If a CSV file already exists for the selected region and range, it will be loaded directly instead of re-fetching

### Data Analysis and Visualization Plan
- Load the CSV data into Python using Pandas for cleaning and structuring
- Use NumPy to calculate price trends, moving averages, and percent change over time
- Use Matplotlib to generate a time series plot of median home prices
- Display summary statistics (average price, highest price, lowest price, overall change) in the popup window
- The chart updates dynamically based on what the user selects

## Installation
```
pip install fredapi pandas numpy matplotlib
```
Then run:
```
python main.py
```

## Future Improvements
- Add support for comparing multiple California regions on the same chart
- Include mortgage rate data alongside home prices
- Add a map visualization showing price differences by region
- Allow users to export charts as image files
- Add affordability index based on median income vs median home price
