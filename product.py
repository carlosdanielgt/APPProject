import json
from model import BaseModel, BaseManager
from decorators.responsedecorators import jsonresponse_decorator
from utils import Condition


class Product(BaseModel):
    manager_class = BaseManager
    table_name = "product"

    @jsonresponse_decorator
    def getAllProducts():
        products = Product.objects.select(
            'id', 'name', 'price', 'image_link')
        json_string = json.loads(str(products))
        return json_string

    def getProductById(productId):
        product = Product.objects.select(
            'id', 'name', 'price', 'image_link', condition=Condition(id__eq=productId))
        return product
