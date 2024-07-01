import requests

def fetch_random_stock_freeapi():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"

    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        stock_data = data["data"]
        Name = stock_data["Name"]
        Symbol = stock_data["Symbol"]
        return Name, Symbol
    else:
        raise Exception("Failed to fetch user data!")

def main():
    try:
        Name, Symbol = fetch_random_stock_freeapi()
        print(f"Name:{Name} \nSymbol:{Symbol}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
