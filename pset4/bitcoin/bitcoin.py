import requests
import sys

try:
    if len(sys.argv) == 2 :
        n = float(sys.argv[1])
    else:
        raise ValueError

except ValueError:
    sys.exit("Missing command-line argument")

while True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        break
    except requests.RequestException:
        pass

rate = response["bpi"]["USD"]["rate_float"]

print(f"${rate * n:,.4f}")