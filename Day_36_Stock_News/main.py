import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = ""
STOCK_URL = "https://www.alphavantage.co/query"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def last_days_date(num):
    # get date of last 2 days
    tod = datetime.datetime.today()
    yesterday_date = (tod - datetime.timedelta(days=num+1)).strftime("%Y-%m-%d")
    day_before_yesterday_date = (tod - datetime.timedelta(days=num+2)).strftime("%Y-%m-%d")
    return yesterday_date, day_before_yesterday_date


def get_stocks_change():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(STOCK_URL, params=params)
    response.raise_for_status()

    stock_data = response.json()
    stock_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
    # print(stock_list)
    yesterday_stock = stock_list[0]["4. close"]
    day_before_yesterday_stock = stock_list[1]["4. close"]
    #calculate percentage of stock change in last two days
    percentage_change = round(
        (abs(float(yesterday_stock) - float(day_before_yesterday_stock)) / float(yesterday_stock)) * 100, 2)
    print(percentage_change)
    # if percentage change more than 2% return true
    if percentage_change > 2:
        return True


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWS_API_KEY = ""
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def get_news():
    last_two_days_date = last_days_date(100)
    params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "from": last_two_days_date[1],
        "apiKey": NEWS_API_KEY,
        "pageSize": "2"
    }
    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    news_list = response.json()
    print(f"total_articles : {news_list['totalResults']}")
    for news in news_list["articles"]:
        print(f'source: {news["source"]["name"]} \n'
              f'author: {news["author"]} \n'
              f'title: {news["title"]} \n'
              f'description: {news["description"]} \n'
              )


# if get_stocks_change():
get_news()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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
