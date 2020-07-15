import hmac
import hashlib
import json
import time
import requests
from pprint import pprint


def timeit(method):
    """
    Use this decorator to debug running time of any method.
    Usage:
        Add @timeit on top of the function you want to time
    """
    def timed(*args, **kw):
        t_start = time.time()
        result = method(*args, **kw)
        t_end = time.time()
        print('{}: {}ms'.format(method.__name__, (t_end - t_start) * 1000))
        return result
    return timed


class CoinDCX:
    def __init__(self,
                 url='https://api.coindcx.com/',
                 public_url='https://public.coindcx.com/',
                 key='xxxx',
                 secret='xxxx'):
        self.url = url
        self.public_url = public_url
        self.key = key
        self.secret = secret

    def create_signature(self, body_str: str):
        secret_bytes = bytes(self.secret, encoding='utf-8')
        return hmac.new(secret_bytes, body_str.encode(), hashlib.sha256).hexdigest()

    def get_body_str(self, body: dict):
        return json.dumps(body, separators=(',', ':'))

    def get_auth_headers(self, body: dict):
        self.update_with_timestamp(body)
        body_str = self.get_body_str(body)
        signature = self.create_signature(body_str)
        return {
            'Content-Type': 'application/json',
            'X-AUTH-APIKEY': self.key,
            'X-AUTH-SIGNATURE': signature
        }

    def do_get(self, url):
        response = requests.get(url)
        data = response.json()
        # pprint(data)
        return data

    def update_with_timestamp(self, json_data):
        timestamp = int(round(time.time() * 1000))
        json_data['timestamp'] = timestamp

    def do_post(self, url, str_data: str = None, json_data: dict = None):
        headers = self.get_auth_headers(body=json_data)
        body_str = self.get_body_str(json_data)
        response = requests.post(url, data=body_str, headers=headers)
        data = response.json()
        # pprint(data)
        return data

    def get_exchange_ticker(self):
        url = self.url + 'exchange/ticker'
        return self.do_get(url)

    def get_markets(self):
        url = self.url + 'exchange/v1/markets'
        return self.do_get(url)

    def get_market_details(self):
        url = self.url + 'exchange/v1/markets_details'
        return self.do_get(url)

    def get_trade_history(self, market, limit=50):
        url = f'{self.public_url}market_data/trade_history?pair={market}&limit={limit}'
        return self.do_get(url)

    # @timeit
    def get_orderbook(self, market):
        url = self.public_url + 'market_data/orderbook?pair=' + market
        return self.do_get(url)

    def get_balances(self):
        url = self.url + 'exchange/v1/users/balances'
        return self.do_post(url, json_data={})
