# Price Tracker

## Overview
**Price Tracker** is a Python script that fetches historical price movements for a given stock ticker using the Yahoo Finance API. It analyzes the data to determine the best months to buy or sell a listing by calculating optimal averages over a specified period.

## Features
- Fetches historical price data from Yahoo Finance.
- Analyzes price movements to identify ideal buy and sell months.
- Provides average price trends over the period.
- Requires a valid API key from RapidAPI.

## Requirements
The script requires the following Python modules:
- `statistics`
- `requests`
- `getpass`
- `datetime`
- `time`

You can install missing dependencies using:
```bash
pip install requests
```

## Setup
1. Obtain an API key from [RapidAPI](https://rapidapi.com/).
2. Ensure you have the required Python modules installed.
3. Run the script using:
   ```bash
   python price_tracker.py
   ```
4. Enter the stock ticker symbol (refer to the Yahoo Finance website for correct symbol names).
5. Provide the start and end dates for historical data retrieval.
6. Enter your API key when prompted.

## Usage
- The script will fetch historical price data for the given ticker.
- It will analyze the data and suggest the best months to buy and sell.
- Output will include statistical insights based on historical trends.

## Example
```plaintext
Symbol: AAPL
Enter a start year: 2020
Enter a start month: 1
Enter a start day: 1
Enter an end year: 2023
Enter an end month: 12
Enter an end day: 31
Enter API-KEY *hidden from view*: ********

Fetching historical price data...

Historical average monthly prices (in USD):
Month    Average Price
1        145.23
2        150.45
...

Historically, the highest average price has been in month 7, and the lowest average price has been in month 1.
```

## Notes
- Ensure you enter the correct stock ticker as listed on Yahoo Finance.
- API usage may be subject to rate limits depending on your RapidAPI plan.

## License
This project is open-source and available under the MIT License.

## Author
Constantinos (Dino) Charalambous

