# 📈 YFinance Data Pipeline
[**English**](https://github.com/PedroDaim/YFinance_Data_Pipeline/blob/main/README.md)| [**Português**](https://github.com/PedroDaim/YFinance_Data_Pipeline/blob/main/README_pt.md)

A professional financial data extraction and analysis tool built with Python and Streamlit. Extract, transform, and download clean stock data from Yahoo Finance with a beautiful web interface.

## 🚀 [Live Demo](https://yfinancestockpipeline.streamlit.app/)

![App Screenshot](https://github.com/user-attachments/assets/8b0f8558-43c3-490f-9479-13927d4a4e41)

## ✨ Features

- **Web Interface**: Clean, professional Streamlit dashboard
- **CLI Tool**: Command-line interface for developers and automation
- **Data Pipeline**: ETL process with proper error handling
- **Multiple Time Periods**: 1 day to maximum historical data
- **CSV Export**: Download clean, analysis-ready datasets
- **Custom Styling**: Dark theme with professional design
- **Input Validation**: Handles invalid tickers and edge cases

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web interface
- **yfinance** - Yahoo Finance API
- **Pandas** - Data manipulation
- **Custom CSS** - Professional styling

## 📦 Installation

### Option 1: Use the Web App

Visit the [live demo](https://yfinancestockpipeline.streamlit.app/) - no installation required!

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://https://github.com/PedroDaim/YFinance_Data_Pipeline
cd yfinance-data-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run src/streamlit_app.py

# Or use the CLI
python src/cli_app.py

```

## 🎯 Usage

### Web Interface

1. Enter a stock ticker (e.g., AAPL, GOOGL, TSLA)
2. Select your desired time period
3. Click "Get Stock Data"
4. View the data preview and download the full CSV

### Command Line

```bash
python src/cli_app.py
# Follow the prompts to enter ticker and period

```

### API Integration

```python
from src.data_pipeline import extract_data, transform_data

# Extract raw data
raw_data = extract_data("AAPL", "1y")

# Clean and transform
clean_data = transform_data(raw_data)

```

## 📁 Project Structure

```
stock-data-pipeline/
├── src/
│   ├── streamlit_app.py     # Web interface
│   ├── cli_app.py          # Command-line tool
│   ├── data_pipeline.py    # Core ETL logic
│   └── styles.css          # Custom styling
├── data/                   # Output directory (git-ignored)
├── requirements.txt        # Dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules

```

## 🔧 Development

### Local Development

```bash
# Install in development mode
pip install -e .

# Run tests (if implemented)
pytest tests/

# Run the Streamlit app with hot reload
streamlit run src/streamlit_app.py

```

### Data Pipeline Architecture

1. **Extract**: Fetch data from Yahoo Finance API
2. **Transform**: Clean column names, handle missing data, type conversion
3. **Load**: Save to timestamped CSV files

## 📊 Supported Data

- **Stock Prices**: Open, High, Low, Close, Adjusted Close
- **Volume Data**: Trading volume information
- **Time Periods**: 1d, 5d, 1mo, 3mo, Ytd, 1y, 5y, Max
- **Markets**: All Yahoo Finance supported exchanges

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](license) file for details.

## 🙏 Acknowledgments

- Yahoo Finance for providing free financial data
- Streamlit team for the amazing web framework
- The Python data science community

## 📧 Contact

Pedro Daim - pdaim.analytics@gmail.com

Project Link: https://github.com/PedroDaim/YFinance_Data_Pipeline

---

⭐ **Star this repo if you found it helpful!**
