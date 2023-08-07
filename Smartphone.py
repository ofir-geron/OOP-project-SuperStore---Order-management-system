from Product import Product
from  Exceptions import *


class Smartphone(Product):
    def __init__(self, product_id, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, brand, model, year, price)
        self.cell_net = cell_net
        try:
            numCor_int = int(num_cores)
        except ValueError as e:
            raise NumCError
        self.num_cores=num_cores
        try:
            camRes_int = int(cam_res)
        except ValueError as e:
            raise CamRError
        self.cam_res = cam_res

    def print_me(self):
        super().print_me()
        print("cell net: ", self.cell_net)
        print("num cores: ", self.num_cores)
        print("cam res: ", self.cam_res)

    def __str__(self):
        prod_msg=super().__str__()
        return f"{prod_msg},{self.cell_net},{self.num_cores},{self.cam_res}"

    def __repr__(self):
        return str(self)

