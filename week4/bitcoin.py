import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "c38e55f9a327f08474d8a0aaf40032a5bdfb5a1bddc69f46dc53d6e17d3807d0"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    price = float(data["data"]["priceUsd"])

    print(f"${amount * price:,.4f}")

if __name__ == "__main__":
    main()