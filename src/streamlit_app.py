import streamlit as st
import plotly.express as px
from data_pipeline import extract_data, transform_data, generate_filename

# Load external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('styles.css')

# App title and description
st.title(" YFinance Stock Pipeline")
st.write("This application extracts, transforms, loads and downloads a csv file with stock data from Yahoo Finance.")

# Create two columns for inputs
col1, col2 = st.columns(2)


with col1:
    ticker_input = st.text_input(
        "📈 Stock Ticker Symbol",
        value="",
        placeholder="Enter ticker (e.g., AAPL, GOOGL, TSLA, NVDA)",
        #help="💡 Popular: AAPL, GOOGL, MSFT, TSLA, NVDA, AMZN, SPY, QQQ"
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
        [ "1d", "5d", "1mo", "6mo", "YTD", "1y", "5y", "Max"],
        index=0  # Default to 1y
    )

# Action button
analyze_button = st.button(" Get Stock Data", type="primary")

# Connect to pipeline when button is clicked
if analyze_button:
    if not ticker or len(ticker) == 0:
        st.error("❌ Please enter a valid ticker symbol before analyzing")
    else:
        with st.spinner(f"📈 Fetching data for {ticker}..."):
            # Use our existing pipeline functions
            raw_data = extract_data(ticker, period)
            
            if not raw_data.empty:
                clean_data = transform_data(raw_data)
                st.success(f"💸Successfully loaded {len(clean_data)} days of data!")
                
                # Get column names
                close_col = [col for col in clean_data.columns if 'close' in col.lower()][0]
                date_col = [col for col in clean_data.columns if 'date' in col.lower()][0]
                
            
                # Show latest price with metric display
                latest_price = clean_data[close_col].iloc[-1]
                st.markdown(f'<p style="color: #f8f9fa; font-size: 18px; font-weight: bold;">💰 Latest price: ${latest_price:.2f}</p>', unsafe_allow_html=True)
                
                #After price, before dataframe
                st.subheader(f"📈 {ticker} Stock Price")
                chart_data = clean_data.set_index(date_col)[close_col]
                st.area_chart(chart_data, color="#1f77b4")
                
                st.write(f"**CSV Preview:**")

                # Data preview
                st.dataframe(clean_data.head())

                # Download functionality
                filename = generate_filename(ticker, period)
                csv_data = clean_data.to_csv(index=False)

                st.download_button(
                label="💾 Download Full Dataset (CSV)",
                data=csv_data,
                file_name=filename,
                mime="text/csv",
                type="primary"
    )
st.markdown(
    """
    <hr style='margin: 40px 0 20px 0; border: 1px solid #dee2e6;'>
    <div style='text-align: center; color: #6c757d; padding: 20px 0;'>
        Made with ❤️ by Pedro Daim   |   
        <a href='https://github.com/PedroDaim/YFinance_Data_Pipeline' style='color: #db4a07; text-decoration: none;'>
            View on GitHub
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)