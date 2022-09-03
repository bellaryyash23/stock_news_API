import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "AC69128919a6087e50a0bcd633290d5745"
auth_token = "0ad7e6e2ab9049d238154b5f041feeee"

yesterday = str((datetime.now() - timedelta(1)).date())
day_bfr_yest = str((datetime.now() - timedelta(2)).date())

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = os.environ.get("STOCK_API")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = os.environ.get("NEWS_API")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
day_bfr_yest_close = float(data["Time Series (Daily)"][day_bfr_yest]["4. close"])
stk_change = round(abs(yesterday_close - day_bfr_yest_close) / yesterday_close * 100, 2)

if yesterday_close - day_bfr_yest_close > 0:
    arrow = "🔼"
else:
    arrow = "🔻"

if stk_change < 5:
    parameters = {
        "q": COMPANY_NAME,
        "from": day_bfr_yest,
        "language": "en",
        "apiKey": NEWS_API
    }

    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    data = response.json()
    news_data = data["articles"][:3]

    headlines = [news_data[i]["title"] for i in range(0, len(news_data))]
    brief = [news_data[i]["description"] for i in range(0, len(news_data))]

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{STOCK}: {arrow}{stk_change}\n"
             f"Heading:{headlines[0]}\nBrief:{brief[0]}\n\n"
             f"Heading:{headlines[1]}\nBrief:{brief[1]}\n\n"
             f"Heading:{headlines[2]}\nBrief:{brief[2]}",
        from_='+12675441487',
        to='+918999697807'
    )

    print(message.status)


# Formatted the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or 
"TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
