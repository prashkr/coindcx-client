from entry import Entry


class Orderbook:
    def __init__(self):
        self.bids = []
        self.asks = []

    def init(self, dcx_orderbook: dict):
        """
        Initializes bids sorted in desc and asks sorted in asc
            bids: high to low
            asks: low to high
        """
        new_bids = []
        new_asks = []
        bids, asks = dcx_orderbook['bids'], dcx_orderbook['asks']
        for p, q in bids.items():
            new_bids.append(Entry(p, q))

        for p, q in asks.items():
            new_asks.append(Entry(p, q))

        self.bids = sorted(new_bids, key=lambda e: e.price, reverse=True)
        self.asks = sorted(new_asks, key=lambda e: e.price)

    @property
    def spread(self):
        highest_buy_entry, lowest_sell_entry = self.bids[0], self.asks[0]
        return lowest_sell_entry.price - highest_buy_entry.price
