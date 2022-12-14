import json
from model import BaseModel, BaseManager
from decorators.responsedecorators import jsonresponse_decorator
from orderprocessing.calculator import Calculator


class Order(BaseModel):
    manager_class = BaseManager
    table_name = "orders"

    @jsonresponse_decorator
    def getAllOrders():
        orders = Order.objects.select(
            'id', 'customer_id', 'product_id', 'quantity', 'price')
        json_string = json.loads(str(orders))
        return json_string

    def calculateOrderTotal(self, orderdetails):
        calculator = Calculator.instance()
        return calculator.calculate(orderdetails)
