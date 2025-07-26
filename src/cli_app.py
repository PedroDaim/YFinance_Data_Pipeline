from data_pipeline import extract_data, transform_data, generate_filename, load_data

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