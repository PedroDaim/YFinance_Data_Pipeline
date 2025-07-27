import pandas as pd
import yfinance as yf
import os
from datetime import datetime
from data_pipeline import generate_filename, extract_data, transform_data, load_data, run_pipeline



#New function to get user input for ticker symbol and period
def get_user_input():
    """
    Gets user input for ticker symbol and period with validation.
    Returns:
        tuple: (ticker_symbol, period)
    """
    # Valid periods for yfinance
    valid_periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    
    print("=== Stock Data Pipeline ===")
    print("Welcome! Let's get some stock data.")
    
    # Get ticker symbol
    while True:
        ticker = input("\nEnter the stock ticker symbol (e.g., AAPL, GOOGL, TSLA): ").strip().upper()
        if ticker:
            break
        else:
            print("Please enter a valid ticker symbol.")
    
    # Get period
    print(f"\nValid periods: {', '.join(valid_periods)}")
    while True:
        period = input("Enter the period (default is '1y'): ").strip().lower()
        if not period:  # If user presses enter without input, use default
            period = '1y'
            break
        elif period in valid_periods:
            break
        else:
            print(f"Invalid period. Please choose from: {', '.join(valid_periods)}")
    
    return ticker, period


# Main entry point for the script
if __name__ == "__main__":
    
    # Get user input for ticker and period
    ticker_symbol, period = get_user_input()

     # Run the pipeline with user-provided values
    run_pipeline(ticker_symbol=ticker_symbol, period=period)