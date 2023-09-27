import requests


def basic(Key="a743b2e2fd41482b93949c707d148e03"):
    r = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2023-08-23&sortBy=publishedAt&apiKey={Key}")
    content = r.json()
    articles = content['articles']

    for article in articles:
        print("TITLE\n", article['title'], '\nDESCRIPTION\n', article['description'], '\n\n')


def get_news(topic, from_date, to_date, language='en', api_key="a743b2e2fd41482b93949c707d148e03"):
    req = requests.get(
        f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}")
    content = req.json()
    articles = content['articles']

    for article in articles:
        print("TITLE\n", article['title'], '\nDESCRIPTION\n', article['description'], '\n\n')

    # get_news('apple', '2023-09-22', '2023-09-26')


def get_headlines(country, api_key="a743b2e2fd41482b93949c707d148e03"):
    req = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}")
    content = req.json()
    articles = content['articles']

    for article in articles:
        print("TITLE\n", article['title'], '\nDESCRIPTION\n', article['description'], '\n\n')

    # get_headlines(country='us')


def get_by_country(country):
    API_key = "0b61b2cb1a04f23f1e1f037da7301b27"
    req = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={country}&appid={API_key}")
    content = req.json()
    print(content)

    # get_by_country('Aleppo')


def get_forecast_country(country):
    API_key = "0b61b2cb1a04f23f1e1f037da7301b27"
    req = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={country}&appid={API_key}")
    content = req.json()
    with open('weather_data.txt', 'w') as file:
        file.write("City,Time,Temperature,Condition\n")
    with open('weather_data.txt', 'a') as file:
        for i in content['list']:
            city = country
            times = i["dt_txt"]
            temp = i["main"]["temp"]
            condition = i["weather"][0]['description']
            content = f"{city},{times},{temp},{condition}\n"
            file.write(content)


get_forecast_country("Washington")
