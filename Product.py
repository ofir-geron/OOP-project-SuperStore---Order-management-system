from  Exceptions import *

class Product :
    def __init__(self, product_id, brand, model, year, price):
        try:
            prod_int=int(product_id)
        except ValueError as e:
            raise IDvalueError()
        self .product_id=product_id
        self.brand = brand
        self.model = model
        self.year=year
        try:
            price_int = int(price)
        except ValueError as e:
            raise PricevalueError()
        self.price = price

    def print_me(self):
        print("product_id: ", self.product_id)
        print("product type: ", type(self).__name__)
        print("model: ", self.model)
        print("year: ", self.year)
        print("price: ", self.price)

    def __str__(self):
        return f"{self.product_id},{type(self).__name__},{self.brand},{self.model},{self.year},{self.price}"

    def __repr__(self):
        return str(self)

    def Is_popular(self):
        if self.year>2017 and self.price<3000:
            return True
        return False






