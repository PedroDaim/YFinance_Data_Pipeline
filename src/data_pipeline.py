#Import necessary libraries
import pandas as pd
import yfinance as yf
import os
from datetime import datetime
import time

# Define output directory relative to the script's location
# --- START CHANGE ---
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script location
project_root = os.path.dirname(script_dir)              # Go up one level to project root
output_dir = os.path.join(project_root, "data")         # Join with 'data' folder
# --- END CHANGE ---
# Script starts here. Functions are defined below.
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
        time.sleep(3) # Wait for 3 seconds after each download
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
    
    # Convert 'date' column to datetime objects
    if 'date' in df_cleaned.columns:
        df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])
    print("Converted 'date' column to datetime.")
    
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
        print(f"DEBUG: Created directory: {os.path.dirname(output_path)}")  
        print(f"DEBUG: Full output path: {os.path.abspath(output_path)}")   
        df.to_csv(output_path, index=False)
        print("Data Loading completed.")
    except Exception as e:
        print(f"Error during data loading: {e}")