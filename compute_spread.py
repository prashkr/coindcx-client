from api import CoinDCX
from orderbook import Orderbook


dcx = CoinDCX()


def compute_spread(market):
    dcx_ob = dcx.get_orderbook(market=market)
    ob = Orderbook()
    ob.init(dcx_orderbook=dcx_ob)
    print(f'spread for market: {market} is {ob.spread}')


while True:
    compute_spread(market='I-BTC_INR')
    compute_spread(market='I-ETH_INR')
