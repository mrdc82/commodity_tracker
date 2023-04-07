'''
Author: Me and ChatGpt"
Date: 07-April-2023"
Description: An API request to yahoo finance which will collect all historical data for dates specified, and print out the best months
to buy and sell a commodity. Please refer to yahoo finance for correct symbol names.
'''

import requests
import statistics
from datetime import date, datetime
import time

symbol = input("Symbol: ") # symbol to retreive data for, ie. ^XAU

syear = int(input('Enter a start year: '))
smonth = int(input('Enter a start month: '))
sday = int(input('Enter a start day: '))
sd = date(syear, smonth, sday)
period1 = int(time.mktime(sd.timetuple()))

eyear = int(input('Enter a end year: '))
emonth = int(input('Enter a end month: '))
eday = int(input('Enter a end day: '))
ed = date(eyear, emonth, eday)
period2 = int(time.mktime(ed.timetuple()))

url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data?symbol={symbol}&period1={period1}&period2={period2}&frequency=1mo"

headers = {
    "X-RapidAPI-Key": input("enter API-KEY: "),
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
    print("Historical average monthly prices (in USD):\n")
    print("Month\tAverage Price")
    for month in range(1, 13):
        print(f"{month}\t{monthly_averages[month - 1]:.2f}")
    print(f"\nHistorically, the highest average price has been in month {highest_month}, and the lowest average price has been in month {lowest_month}.")
else:
    print(f"Error {response.status_code} occurred.")
>>>>>>> 46441a0a4e75c3a6a80730ac1fd8e5ae27b0cc06
