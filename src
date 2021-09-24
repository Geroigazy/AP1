from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def print_crypt(coin):
    print(coin['name'], "\ncost:", coin['current_price'], "$")


for i in range(1):
    b = int(input("Enter the number: "))
    list = cg.get_coins_markets("usd")[:b]
   
    for coin in list:
        print_crypt(coin)
