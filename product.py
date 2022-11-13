from model import BaseModel, BaseManager


class Product(BaseModel):
    manager_class = BaseManager
    table_name = "product"
