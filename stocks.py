import datetime as dt
import requests


def getStock(ticker, date):
    params = [int(x) for x in date.split('-')]
    date = dt.datetime(*params)
    payload = {'function':'TIME_SERIES_DAILY',
        'symbol':ticker,
        'apikey': 'HF4EGOIKD6QHSIF3',
    }
    stocks_dict = requests.get('https://www.alphavantage.co/query', params=payload).json()
    weekno = date.weekday()

    if weekno > 4:
        date -=dt.timedelta(days=weekno-4)

    return stocks_dict['Time Series (Daily)'][date.strftime('%Y-%m-%d')]

def main():
    today = '2017-09-22'
    stock = getStock('MSFT', today)
    print(stock)

if __name__=='__main__':
    main()