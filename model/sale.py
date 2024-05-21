import datetime
from dataclasses import dataclass

from model.product import Product


@dataclass
class Sale:
    Retailer_code : int
    Product_number : int
    Order_method_code : int
    Date : datetime.date
    Quantity : int
    Unit_price : float
    Unit_sale_price : float

    #retailer : Retailer = None
    product : Product = None

    def __hash__(self):
        return hash(self.Retailer_code,self.Product_number,self.Order_method_code)
