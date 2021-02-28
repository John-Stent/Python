import json
import urllib.request


def crypto_price(coin):
    x = urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym={C}&tsyms=USD".format(C=coin))
    x = x.read()
    x = x.decode()
    X = json.loads(x)
    return X["USD"]


with open("./Wallet.txt") as f:
    wallet = f.read()

A = json.loads(wallet)

print(type(A))

for x in A:
    print("You currently have", A[x], "of", x, "which translates to", A[x]*crypto_price(x), "dollars in the current price:", crypto_price(x))
