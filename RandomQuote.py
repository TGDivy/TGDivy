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

    return f"> {quote} ~ {author}"


def read_readme():
    # read the README.md file
    with open("README.md", "r") as f:
        lines = f.readlines()
    return lines


def replace_quote(quote):
    # replace the quote in the README.md file
    lines = read_readme()

    # find the line with the quote, it starts with "> "
    for i, line in enumerate(lines):
        if line.startswith("> "):
            lines[i] = quote
            break

    # write the new README.md file
    with open("README.md", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    quote = get_random_quote()
    replace_quote(quote)
