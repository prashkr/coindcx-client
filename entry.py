class Entry:
    def __init__(self, price: str, quantity: str):
        self.price = float(price)
        self.quantity = float(quantity)

    def __str__(self):
        return f'(price: {self.price}, quantity: {self.quantity})'
