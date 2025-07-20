Markdown

# Simple Financial Data Pipeline

This project implements a simple, modular data pipeline to extract historical stock data using `yfinance`, transform it, and load it into a CSV file. The pipeline is designed to be easily runnable locally or within a Docker container.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Output Data Format](#output-data-format)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

* **Data Extraction:** Fetches historical stock data (Open, High, Low, Close, Volume, Adj Close) for a specified ticker symbol and period using the `yfinance` library.
* **Data Transformation:**
    * Cleans column names (lowercase, replaces spaces/dots with underscores).
    * Ensures price-related columns are in decimal (float) format.
    * Formats the 'Volume' column into millions (e.g., "1.5M") for readability.
    * Handles potential `yfinance` MultiIndex columns gracefully.
* **Data Loading:** Saves the transformed data into a CSV file.
* **Containerized Execution:** Supports execution via Docker for isolated and reproducible environments.

## Project Structure

Simple_Data_Pipeline/
├── app/
│   └── pipeline.py       # Main Python script containing the ETL pipeline functions
├── Dockerfile            # Defines the Docker image for the application
└── requirements.txt      # Lists Python dependencies
└── README.md             # This file


## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine or within a Docker container.

### Prerequisites

* **Python 3.9+** (for local setup)
* **pip** (Python package installer)
* **Docker Desktop** (or Docker Engine for Linux)

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Simple_Data_Pipeline.git](https://github.com/YourUsername/Simple_Data_Pipeline.git)
    cd Simple_Data_Pipeline
    ```
    *(Remember to replace `YourUsername` with your actual GitHub username and adjust the repository name if it's different)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the pipeline:**
    ```bash
    python app/pipeline.py
    ```
    The output CSV file `CleanedFinancialData.csv` will be saved in a `data/` subdirectory created next to your `pipeline.py` file (`Simple_Data_Pipeline/data/`).

### Docker Setup

1.  **Ensure you are in the root directory of the project** (where `Dockerfile` is located):
    ```bash
    cd Simple_Data_Pipeline
    ```

2.  **Build the Docker image:**
    ```bash
    docker build -t financial-pipeline-image .
    ```
    This command builds a Docker image named `financial-pipeline-image` using your `Dockerfile`.

3.  **Run the Docker container and mount a volume for data persistence:**
    This command will run the pipeline inside a container and save the output CSV to a directory on your host machine.

    * **Create a local directory** on your host machine where you want the output data to be saved (e.g., `C:\my_stock_data` on Windows, or `~/my_stock_data` on Linux/macOS).

    * **Execute the Docker run command:**
        ```bash
        # On Windows:
        docker run -v C:\path\to\your\local\data_output:/app/data financial-pipeline-image

        # On macOS/Linux:
        docker run -v /path/to/your/local/data_output:/app/data financial-pipeline-image
        ```
        Replace `C:\path\to\your\local\data_output` or `/path/to/your/local/data_output` with the **absolute path** to the directory you created on your host machine.

        The `CleanedFinancialData.csv` file will be created inside this specified host directory.

## Usage

The pipeline is configured to download data for 'AAPL' (Apple Inc.) for a '5y' (5-year) period by default.

To change the ticker symbol or period, modify the `run_pipeline` call at the bottom of `app/pipeline.py`:

```python
if __name__ == "__main__":
    # Example usage: Get 5 years of data for Tesla (TSLA)
    run_pipeline(ticker_symbol='TSLA', period='5y')
Output Data Format
The CleanedFinancialData.csv file will contain columns similar to:

Column Name	Description	Format
date	Trading date	YYYY-MM-DD
open	Opening price	Decimal
high	Highest price of the day	Decimal
low	Lowest price of the day	Decimal
close	Closing price	Decimal
adj_close	Adjusted closing price (accounts for dividends)	Decimal
volume	Volume of shares traded	e.g., "1.23M"

Export to Sheets
Troubleshooting
AttributeError: 'tuple' object has no attribute 'strip': This indicates an issue with column name processing, likely due to yfinance returning MultiIndex columns. Ensure your transform_data function includes logic to flatten MultiIndex columns (as updated during our discussions).

File not found/saved where expected (e.g., /data directory):

Local: Ensure your output_path in pipeline.py is relative (e.g., output_dir = "data"; output_path = os.path.join(output_dir, "CleanedFinancialData.csv")).

Docker: Confirm you are using a Docker volume (-v flag) in your docker run command, mapping a host directory to /app/data inside the container.

JSONDecodeError / 429 Too Many Requests:

This typically means Yahoo Finance's API is rate-limiting your requests.

Solution: Wait for a period (e.g., 5-15 minutes, or longer if persistent) and try again. Repeated requests, especially from the same public IP, can trigger this. If using a VPN or shared network, consider temporarily disabling VPN or changing networks if possible.

Diagnostic Steps (if issue persists in Docker):

Run docker run -it --rm financial-pipeline-image bash

apt-get update && apt-get install -y iputils-ping curl

ping 8.8.8.8 (check basic connectivity)

ping google.com (check DNS)

curl -v https://query2.finance.yahoo.com/v8/finance/chart/TSLA?range=5y&interval=1d > curl_output.txt 2>&1 (check API response)

Then exit the container and docker cp <container_id>:/app/curl_output.txt . to get the full response.

Dockerfile parse error on line 2: FROM requires either one or three arguments: This happens if you place a comment on the same line as the FROM instruction, immediately after the image name. Move the comment to its own line.

bash: ping: command not found or bash: curl: command not found in Docker: slim Docker images don't include these by default. You need to apt-get install -y iputils-ping curl inside the running container for debugging, or add these to your Dockerfile if you always need them (though this increases image size).

E: The repository 'http://deb.debian.org/debian buster Release' does not have a Release file.: Your Docker base image is likely outdated. Update your Dockerfile to use a newer Debian version, e.g., FROM python:3.11-slim-bullseye.

Contributing
Feel free to fork this repository, open issues, or submit pull requests with improvements.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
