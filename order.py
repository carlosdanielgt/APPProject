from model import BaseModel, BaseManager


class Order(BaseModel):
    manager_class = BaseManager
    table_name = "orders"
