import csv
from Product import Product
from Laptop import Laptop
from Shirts import Shirts
from Order import Order
from Client import Client
from Exceptions import ClientNotFoundError
from Exceptions import ShirtNotFoundError
from Smartphone import Smartphone

class SuperStore:
    def __init__(self, products_cvs, clients_csv, shirts_csv, orders_csv):
        self.product_list = []
        self.client_list= []
        self.order_list= []
        with open(f"{products_cvs}.csv") as csvfile:
            read = csv.reader(csvfile)
            next(read)  # ignore first line in the csv
            for row in read:
                product_id = int(row[0])
                product_type = row[1]
                brand = row[2]
                model = row[3]
                year = int(row[4])
                price = int(row[5])
                if product_type=="laptop":
                    CPU= row[6]
                    hard_disk= int(row[7])
                    screen=int(row[8])
                    l = Laptop(product_id, brand, model, year, price, CPU, hard_disk, screen)
                    self+=l

                if product_type=="smartphone":
                    cell_net = row[9]
                    num_cores = int(row[10])
                    cam_res = int(row[11])
                    sp = Smartphone(product_id, brand, model, year, price, cell_net, num_cores, cam_res)
                    self+=sp


        with open(f"{shirts_csv}.csv") as csvfile:
            read = csv.reader(csvfile)
            next(read)  # ignore first line in the csv
            for row in read:
                product_id = int(row[0])
                product_name = row[1]
                price = int(row[2])
                units_in_stock = int(row[3])
                sh= Shirts(product_id, product_name, price, units_in_stock)
                self +=sh

        with open(f"{orders_csv}.csv") as csvf:
            read = csv.reader(csvf)
            next(read)  # ignore first line in the csv
            for row in read:
                order_id = int(row[0])
                client_id = int(row[1])
                product_id = int(row[2])
                quantity = int(row[3])
                o = Order(order_id, client_id, product_id, quantity)
                self.order_list.append(o)

        with open(f"{clients_csv}.csv") as cs:
            read = csv.reader(cs)
            next(read)  # ignore first line in the csv
            for row in read:
                client_id = int(row[0])
                name = row[1]
                email = row[2]
                address = row[3]
                phone_number = row[4]
                gender = row[5]
                c = Client(client_id, name, email, address, phone_number, gender)
                self.add_client(c)

    def print_product(self):
        for product in self.product_list:
            print(product)

    def get_product(self, idProd):
        for product in self.product_list:
            if product.product_id == idProd:
                return product
        return None

    def get_shirt(self, idShirt):
        for product in self.product_list:
            if product.product_id == idShirt:
                return product
        return None


    #
    # def add_product(self, prod):
    #     for product in self.product_list:
    #         if product.product_id == prod.product_id:
    #             return False
    #     self.product_list.append(prod)
    #     return True


    def __iadd__(self, other):
        for product in self.product_list:
            if product.product_id == other.product_id:
                return self
        self.product_list.append(other)
        return self


    def add_client(self, new_client):
        for client in self.client_list:
            if client.client_id == new_client.client_id:
                return False
        self.client_list.append(new_client)
        return True


    def remove_product(self, delete_prod_id):
        for product in self.product_list:
            if product.product_id == delete_prod_id:
                self.product_list.remove(product)
                return True
        return False

    def remove_client(self, delete_client_id):
        for client in self.client_list:
            if client.client_id == delete_client_id:
                self.client_list.remove(client)
                return True
        return False

    def print_client(self):
        for client in self.client_list:
            print(client)

    def get_client(self, id_client):
        for client in self.client_list:
            if client.client_id== id_client:
                return client
        return None

    def get_all_my_brand(self, comp_name):
        company=[]
        for product in self.product_list:
            if product.brand == comp_name:
                company.append(product)
        return company

    def get_all_by_price_under(self,maxPrice):
        low_from_max = []
        for product in self.product_list:
            if product.price < maxPrice:
                low_from_max.append(product)
        return low_from_max

    def get_most_expensive_product(self):
        max_price = self.product_list[0]
        for product in self.product_list:
            if product.price >= max_price.price:
                max_price = product
        return max_price

    def get_max_order_id(self):
        order_max=0
        for order in self.order_list:
            if order.order_id>=order_max:
                order_max=order.order_id
        return order_max

    def add_order(self, cl_id, prod_id, quant):

        order_id=self.get_max_order_id()+1
        if self.get_client(cl_id) is None:
            raise ClientNotFoundError("client not exists")
        if self.get_product(prod_id) is None or self.get_shirt(prod_id) is None:
            raise ShirtNotFoundError("product(smartphone/laptop/shirt not exists")

        if type(self.get_product(prod_id))!= Shirts:
            if quant>1:
                raise ValueError("quantity of laptop/smartphone bigger then units in stock!!")
        if type(self.get_product(prod_id))== Shirts:
            if self.get_shirt(prod_id).units_in_stock< quant:
                raise ValueError("quantity of shirt bigger then units in stock!!")
        new_order=Order(order_id,cl_id,prod_id,quant)
        self.order_list.append(new_order)
        print("order added!!")
        # order_id=self.get_max_order_id()+1
        # if self.get_client(cl_id) is None:
        #     raise ClientNotFoundError("client not exists")
        # if self.get_product(prod_id) is None or self.get_shirt(prod_id) is None:
        #     raise ShirtNotFoundError("product(smartphone/laptop/shirt not exists")
        #
        # laptop_id_list=[]
        # phons_id_list=[]
        # shirts_id_list=[]
        # for i in self.get_all_laptops():
        #     laptop_id_list.append(i.product_id)
        # for j in self.get_all_phones():
        #     phons_id_list.append(j.product_id)
        # for k in self.get_all_shirt():
        #     shirts_id_list.append(k.product_id)
        #
        # for prod in self.product_list:
        #     if prod_id in laptop_id_list :
        #         if quant>1:
        #             raise ValueError("quantity of laptop bigger then units in stock!!")
        #
        #     if prod_id in phons_id_list:
        #         if quant>1:
        #             raise ValueError("quantity of smartphone bigger then units in stock!!")
        #
        #     if prod_id in shirts_id_list:
        #         if type(prod)== Shirts and prod.product_id==prod_id:
        #             if quant> prod.units_in_stock:
        #                 raise ValueError("quantity of shirt bigger then units in stock!!")
        # self.order_list+= [Order(order_id, cl_id,prod_id,quant)]
        # print("order added!!")



    # newwwwwww
    def get_all_phones(self):
        phone_lst=[]
        for product in self.product_list:
            if type(product)==Smartphone:
                 phone_lst.append(product)
        return phone_lst

    def get_all_laptops(self):
        laptops_lst = []
        for product in self.product_list:
            if type(product) == Laptop:
                laptops_lst.append(product)
        return laptops_lst

    def get_all_shirt(self):
        shirts_lst = []
        for product in self.product_list:
            if type(product) == Shirts:
                shirts_lst.append(product)
        return shirts_lst

    def print_orders(self):
        for order in self.order_list:
            print(order)



    def phone_average_price(self):
        sum=0
        count=0
        for product in self.product_list:
            if type(product) is Smartphone:
                sum+=product.price
                count+=1
        return sum/count

    def get_max_screen(self):
        max_is=self.product_list[0].screen
        for product in self.product_list:
            if type(product) is Laptop:
                if product.screen > max_is:
                    max_is=product.screen
        return max_is

    def get_common_cam(self):
        phone_lst=[]
        for product in self.product_list:
            if type(product) is Smartphone:
                phone_lst.append(product.cam_res)
        return max(set(phone_lst), key=phone_lst.count)


    def list_popular(self):
        popular_lst=[]
        for product in self.product_list:
            if product.Is_popular():
                popular_lst.append(product)
        return popular_lst



