import streamlit as st
from data_pipeline import extract_data, transform_data, generate_filename

# Load external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('styles.css')

# App title and description
st.title(" Stock Data Pipeline")
st.write("This application extracts, transforms, loads and downloads a csv file with stock data from Yahoo Finance.")

# Create two columns for inputs
col1, col2 = st.columns(2)


with col1:
    ticker_input = st.text_input(
        "📈 Stock Ticker Symbol",
        value="",
        placeholder="Enter ticker (e.g., AAPL, GOOGL, TSLA, NVDA)",
        help="💡 Popular: AAPL, GOOGL, MSFT, TSLA, NVDA, AMZN, SPY, QQQ"
    )
    
    # Clean and validate input
    ticker = ticker_input.upper().strip()
    
    # Validate ticker: must be 2-10 chars, letters/hyphens/dots only
    if ticker:
        if len(ticker) < 2:
            st.error("⚠️ Ticker symbol must be at least 2 characters")
            ticker = ""
        elif len(ticker) > 10:
            st.error("⚠️ Ticker symbol too long (max 10 characters)")  
            ticker = ""
        elif not ticker.replace('-', '').replace('.', '').isalpha():
            st.error("⚠️ Please enter a valid ticker symbol (letters, hyphens, and dots only)")
            ticker = ""
with col2:
    period = st.selectbox(
        "Select Time Period", 
        ["1y", "2y", "5y", "1mo", "3mo", "6mo", "YTD", "Max"],
        index=0  # Default to 1y
    )

# Action button
analyze_button = st.button(" Get Stock Data", type="primary")

# Connect to pipeline when button is clicked
if analyze_button and ticker:  # Only run if button clicked AND ticker is valid
    with st.spinner(f"📈Fetching data for {ticker}..."):
        # Use our existing pipeline functions
        raw_data = extract_data(ticker, period)
        
        if not raw_data.empty:
            clean_data = transform_data(raw_data)
            st.success(f"💸Successfully loaded {len(clean_data)} days of data!")
            
            # Show basic info for now
            close_col = [col for col in clean_data.columns if 'close' in col.lower()][0]
            st.write(f"**Latest price:** ${clean_data[close_col].iloc[-1]:.2f}")
            st.dataframe(clean_data.head())

            # Add download functionality
            filename = generate_filename(ticker, period)
            csv_data = clean_data.to_csv(index=False)

            st.download_button(
            label="💾 Download Full Dataset (CSV)",
            data=csv_data,
            file_name=filename,
            mime="text/csv",
            type="primary"
)
        else:
            st.error(f"❌ No data found for ticker: {ticker}")



