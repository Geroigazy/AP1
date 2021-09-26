from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


num = int(input("Enter the number: "))
list = cg.get_coins_markets("usd")[:num] 
n=0
while n < len(list):
    coin = list[n]
    print(coin['name'], "\ncost:", coin['current_price'], "$\t", "Capitalization", coin['market_cap'], "$\n")
    n = n+1
