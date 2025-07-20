import pandas as pd
import yfinance as yf
import os

# Define output directory relative to the script's location
# This will create a 'data' folder next to your script if it doesn't exist
output_dir = "data"
output_path = os.path.join(output_dir, "CleanedFinancialData.csv")
# --- END CHANGE ---

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

    # Now, apply the cleaning operations (lowercase, replace spaces/dots)
    df_cleaned.columns = [col.strip().lower().replace(" ", "_").replace(".", "") for col in df_cleaned.columns]

    # You might want to drop rows with NaN values if any, though yfinance data is usually clean
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
    df_raw = extract_data(ticker_symbol, period)
    df_cleaned = transform_data(df_raw)
    load_data(df_cleaned, output_path)
    print("Data pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline(ticker_symbol='TSLA', period='5y')