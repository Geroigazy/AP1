from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def print_crypt(coin):
    print(coin['name'], "\ncost:", coin['current_price'], "$\t", "Capitalization", coin['market_cap'], "$\n")


for i in range(1):
    num = int(input("Enter the number: "))
    list = cg.get_coins_markets("usd")[:num]
    for coin in list:
        print_crypt(coin)
