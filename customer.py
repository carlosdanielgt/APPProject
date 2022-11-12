from model import BaseModel, BaseManager


class Customer(BaseModel):
    manager_class = BaseManager
    table_name = "customer"
