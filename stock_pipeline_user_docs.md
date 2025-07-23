# Stock Data Pipeline - User Guide

## What This Tool Does

This tool downloads historical stock price data from Yahoo Finance and cleans it up for analysis. Instead of manually copying data from websites or paying for expensive data services, you can get months or years of stock information in seconds and save it as a spreadsheet file.

The tool is particularly useful for financial analysis, investment research, academic projects, or any situation where you need clean, organized stock market data.

## What You Get

When you run this tool, you'll receive a CSV file (spreadsheet) containing:

- Daily stock prices (open, high, low, close)
- Trading volume
- Adjusted closing prices (accounts for stock splits and dividends)
- Clean, consistent formatting ready for analysis in Excel, Google Sheets, or other tools

## Before You Start

You need Python installed on your computer along with three additional packages. If you're not sure whether you have Python, open your command prompt or terminal and type:

```
python --version
```

If you see a version number (like Python 3.9.0), you're ready to install the required packages. If not, download Python from python.org first.

### Installing Required Packages

Open your command prompt or terminal and run these commands one at a time:

```
pip install pandas
pip install yfinance
```

The `os` package comes with Python automatically, so you don't need to install it separately.

## How to Use the Tool

1. Save the Python script to a folder on your computer
2. Open your command prompt or terminal
3. Navigate to the folder where you saved the script
4. Run the command: `python filename.py` (replace "filename" with whatever you named the script)

The tool will ask you two questions:

### Stock Ticker Symbol
This is the abbreviation used to identify a company on the stock market. Common examples:
- AAPL (Apple)
- GOOGL (Google/Alphabet)
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)

Enter the ticker symbol when prompted. The tool automatically converts it to uppercase, so "aapl" and "AAPL" work the same way.

### Time Period
Choose how far back you want the data to go:

- **1d**: One day (today's data only)
- **5d**: Five days
- **1mo**: One month
- **3mo**: Three months
- **6mo**: Six months
- **1y**: One year (default if you just press Enter)
- **2y**: Two years
- **5y**: Five years
- **10y**: Ten years
- **ytd**: Year to date (from January 1st to today)
- **max**: All available data (can be decades for established companies)

## Example Session

Here's what a typical session looks like:

```
=== Stock Data Pipeline ===
Welcome! Let's get some stock data.

Enter the stock ticker symbol (e.g., AAPL, GOOGL, TSLA): AAPL

Valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
Enter the period (default is '1y'): 2y

Starting data pipeline for AAPL...
Attempting to extract data for AAPL for the period 2y...
Data Extraction completed.
Starting Data Transformation...
Data Transformation completed.
Attempting to load data to data/AAPL_2y_20231215_143052.csv...
Data Loading completed.
Data pipeline completed successfully.
Data saved to: data/AAPL_2y_20231215_143052.csv
```

## Understanding Your Results

The tool creates a folder called "data" in the same location as the script and saves your results with a unique filename that includes:
- The stock ticker symbol
- The time period you selected  
- The date and time when you ran the script

For example, if you download Apple data for 2 years on December 15, 2023 at 2:30 PM, the file might be named: `AAPL_2y_20231215_143052.csv`

This naming system ensures you never accidentally overwrite previous downloads. You can run the tool multiple times for the same stock or different stocks without losing any data.

### Column Explanations

When you open the CSV file, you'll see these columns:

- **date**: The trading date
- **open**: Price when the market opened that day
- **high**: Highest price during the day
- **low**: Lowest price during the day
- **close**: Price when the market closed
- **adj_close**: Adjusted closing price (accounts for dividends and stock splits)
- **volume**: Number of shares traded that day

For most analysis purposes, use the "adj_close" price rather than "close" because it gives you a more accurate picture of the stock's performance over time.

## Common Use Cases

### Investment Analysis
Download 5-year data for stocks you're considering buying to analyze long-term trends and volatility.

### Academic Research
Get historical data for case studies, financial modeling assignments, or market behavior research.

### Portfolio Tracking
Download data for stocks you own to calculate returns, compare performance, or create charts.

### Business Intelligence
Extract competitor stock data to understand market reactions to industry events or earnings announcements.

## Troubleshooting

### "No data extracted" Message
This usually means:
- The ticker symbol doesn't exist or is misspelled
- The company was not publicly traded during your selected time period
- There's a temporary connection issue with Yahoo Finance

Try double-checking the ticker symbol on a financial website like Yahoo Finance or Google Finance.

### Connection Errors
If you see network-related error messages:
- Check your internet connection
- Try again in a few minutes (Yahoo Finance occasionally has temporary outages)
- Some corporate networks block financial data feeds

### File Permission Errors
If the tool can't save the CSV file:
- Make sure you have write permissions in the folder where you're running the script
- Close any Excel or other programs that might have the CSV file open
- Try running the script from a different folder

### Invalid Period Error
Make sure you're entering one of the valid time periods exactly as listed. The tool is case-sensitive, so use lowercase letters.

## Tips for Better Results

- For very new companies, use shorter time periods (1y or less) as they may not have long trading histories
- Each time you run the tool, it creates a new file with a unique name, so you can safely analyze multiple stocks or time periods without losing previous data
- If you want to compare multiple stocks, consider using the same time period for consistency
- For academic or professional analysis, consider using "max" period to get the complete trading history
- Always verify ticker symbols on financial websites before running the analysis

## Getting Help

If you encounter problems not covered in this guide:
- Double-check that all required packages are installed correctly
- Verify the ticker symbol exists on Yahoo Finance's website
- Make sure you have a stable internet connection
- Try running the script with a different stock or time period to isolate the issue