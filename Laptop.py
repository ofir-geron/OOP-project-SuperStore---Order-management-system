from Product import Product
from  Exceptions import *


class Laptop(Product):
    def __init__(self, product_id, brand, model, year, price, CPU, hard_disk, screen):
        super().__init__(product_id, brand, model, year, price)
        self.CPU=CPU
        try:
            hardDisk_int = int(hard_disk)
        except ValueError as e:
            raise HardDiskError
        self.hard_disk=hard_disk
        try:
            screen_int = int(screen)
        except ValueError as e:
            raise ScreenError
        self.screen=screen


    def print_me(self):
        super().print_me()
        print("cpu: ", self.CPU)
        print("hard disk: ", self.hard_disk)
        print("screen: ", self.screen)

    def __str__(self):
        prod_msg=super().__str__()
        return f"{prod_msg},{self.CPU},{self.hard_disk},{self.screen}"

    def __repr__(self):
        return str(self)
