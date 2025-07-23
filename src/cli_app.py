import pandas as pd
import yfinance as yf
import os
from datetime import datetime

# Define output directory relative to the script's location
# This will create a 'data' folder next to the script if it doesn't exist
output_dir = "../data"
def generate_filename(ticker_symbol: str, period: str) -> str:
    """
    Generates a unique filename based on ticker, period, and timestamp.
    Args:
        ticker_symbol (str): The stock ticker symbol
        period (str): The time period
    Returns:
        str: Full path to the output file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ticker_symbol}_{period}_{timestamp}.csv"
    return os.path.join(output_dir, filename)

def extract_data(ticker_symbol: str, period: str = '1y') -> pd.DataFrame:
    """
    Extracts historical stock data for a given ticker symbol and period using yfinance.
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL').
        period (str): The period to download data for (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
                      Defaults to '1y'.
    Returns:
        pd.DataFrame: A DataFrame containing the downloaded historical stock data.
    """
    print(f"Attempting to extract data for {ticker_symbol} for the period {period}...")
    try:
        df = yf.download(ticker_symbol, period=period)
        if df.empty:
            print(f"No data extracted for {ticker_symbol}. Check the ticker symbol or period.")
        else:
            print("Data Extraction completed.")
        return df
    except Exception as e:
        print(f"Error during data extraction: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the raw financial data.
    Args:
        df (pd.DataFrame): The raw DataFrame from yfinance.
    Returns:
        pd.DataFrame: The cleaned and transformed DataFrame.
    """
    if df.empty:
        print("No data to transform. Skipping transformation.")
        return pd.DataFrame()
    
    print("Starting Data Transformation...")
    
    # Reset index to make 'Date' a regular column
    df_cleaned = df.reset_index()
    
    # Handle potential MultiIndex columns by flattening them
    if isinstance(df_cleaned.columns, pd.MultiIndex):
        # Join the levels of the MultiIndex columns with an underscore
        df_cleaned.columns = ['_'.join(col).strip() for col in df_cleaned.columns.values]
    
    # Apply the cleaning operations (lowercase, replace spaces/dots)
    df_cleaned.columns = [col.strip().lower().replace(" ", "_").replace(".", "") for col in df_cleaned.columns]
    
    # Drop rows with NaN values if any
    df_cleaned = df_cleaned.dropna()
    
    print("Data Transformation completed.")
    return df_cleaned

def load_data(df: pd.DataFrame, output_path: str):
    """
    Loads the transformed data into a CSV file.
    Args:
        df (pd.DataFrame): The transformed DataFrame.
        output_path (str): The path where the CSV file will be saved.
    """
    if df.empty:
        print("No data to load. Skipping data loading.")
        return
    
    print(f"Attempting to load data to {output_path}...")
    try:
        # Ensure the directory exists
        # This will now create the 'data' folder relative to your script
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print("Data Loading completed.")
    except Exception as e:
        print(f"Error during data loading: {e}")

def run_pipeline(ticker_symbol: str, period: str = '1y'):
    """
    Runs the complete data pipeline for extracting, transforming, and loading financial data.
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL').
        period (str): The period to download data for (e.g., '1y', '5y').
    """
    print(f"Starting data pipeline for {ticker_symbol}...")
    
    # Generate unique filename for this run
    output_path = generate_filename(ticker_symbol, period)
    
    df_raw = extract_data(ticker_symbol, period)
    df_cleaned = transform_data(df_raw)
    load_data(df_cleaned, output_path)
    print("Data pipeline completed successfully.")
    print(f"Data saved to: {output_path}")

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

if __name__ == "__main__":
    # Get user input for ticker and period
    ticker_symbol, period = get_user_input()
    
    # Run the pipeline with user-provided values
    run_pipeline(ticker_symbol=ticker_symbol, period=period)