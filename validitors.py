from SuperStore import SuperStore
from Exceptions import *

store = SuperStore(products_cvs='products_supply', clients_csv='clients', shirts_csv='shirts', orders_csv='orders')

VALID_YEARS = list(range(2023, 2034))

def validate_ID(product_id):
    if store.get_product(product_id) is not None:
        raise IDNotFoundError(f"product id exists! [{product_id}]")

    return product_id
