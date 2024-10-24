import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "4ee4c1cf3922496d9aa55bebdf5f3d7a"
TWILIO_SID = "ACd52fbc760e8a7f41b2bb29dc473b4e57"
TWILIO_AUTH_TOKEN = "0e86ba05bed3174ec8287620d1dbf683"


news_parameters = {
    "q": STOCK,
    "qInTitle": COMPANY_NAME,
    "apiKey": "4ee4c1cf3922496d9aa55bebdf5f3d7a",

}


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":"IBM",
    "apikey": "I0IF6LHG2UY1B9VG",

}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
previous_close_price = float(stock_data["Time Series (Daily)"]["2024-10-14"]["4. close"])
today_close_price = float(stock_data["Time Series (Daily)"]["2024-10-07"]["4. close"])

change_in_price = abs(today_close_price - previous_close_price)

percentage_change = (change_in_price/previous_close_price) * 100

# STEP 1: Use https://newsapi.org/docs/endpoints/everything

if percentage_change > 3 or percentage_change < 3:
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_article = news_response.json()["articles"]

    three_articles = news_article[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for each_article in formatted_articles:
        message = client.messages.create(
            body=each_article,
            from_="+19252332841",
            to = "+255679384924"
        )




# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

