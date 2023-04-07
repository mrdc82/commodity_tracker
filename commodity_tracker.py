import requests
import statistics
from datetime import datetime

symbol = "^GSPC" # symbol for heating oil futures
period1 = "946684800" # January 1, 2000 (in Unix timestamp format)
period2 = "1617753600" # April 7, 2021 (in Unix timestamp format)

url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data?symbol={symbol}&period1={period1}&period2={period2}&frequency=1mo"

headers = {
    "X-RapidAPI-Key": "1ab9b8d3abmsha77579e23194c73p198159jsn024a23c51a17",
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    prices = [d["close"] for d in data["prices"]]
    months = [datetime.fromtimestamp(d["date"]).month for d in data["prices"]]
    monthly_averages = [0] * 12
    monthly_counts = [0] * 12
    for i in range(len(prices)):
        price = prices[i]
        month = months[i]
        monthly_averages[month - 1] += price
        monthly_counts[month - 1] += 1
    for month in range(1, 13):
        if monthly_counts[month - 1] > 0:
            monthly_averages[month - 1] /= monthly_counts[month - 1]
    highest_month = monthly_averages.index(max(monthly_averages)) + 1
    lowest_month = monthly_averages.index(min(monthly_averages)) + 1
    print("Historical average monthly heating oil prices (in USD):\n")
    print("Month\tAverage Price")
    for month in range(1, 13):
        print(f"{month}\t{monthly_averages[month - 1]:.2f}")
    print(f"\nHistorically, the highest average price for heating oil has been in month {highest_month}, and the lowest average price has been in month {lowest_month}.")
else:
    print(f"Error {response.status_code} occurred.")
