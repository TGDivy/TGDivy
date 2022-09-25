import requests
import os
import json


# QUOTES_API_KEY = os.environ["QUOTES_API_KEY"]
URL = "https://zenquotes.io/api/today/"

## function that gets the random quote
def get_random_quote():

    querystring = {"mode": "random"}

    response = requests.request(
        "GET",
        URL,
        params=querystring,
    )

    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]

    print("# Quote of the Day ")
    print("*Using GitHub Actions Chron Job*")
    print(f"> {quote} ~ {author}")


get_random_quote()
