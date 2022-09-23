import requests

## function that gets the random quote
def get_random_quote():
    print("# Quote of the Day")
    print("*Using GitHub Actions Chron Job*")
    try:
        response = requests.get(
            "https://quote-garden.herokuapp.com/api/v3/quotes/random"
        )
        if response.status_code == 200:
            json_data = response.json()
            data = json_data["data"]

            print(f"> {data[0]['quoteText']} ~ {data[0]['quoteAuthor']}")

        else:
            print("> Error while getting quote")
    except:
        print("> Something went wrong! Try Again!")


get_random_quote()
