import json
from model import BaseModel, BaseManager
from decorators.responsedecorators import jsonresponse_decorator
from utils import Condition


class Customer(BaseModel):
    manager_class = BaseManager
    table_name = "customer"

    @jsonresponse_decorator
    def getAllCustomers():
        customers = Customer.objects.select(
            'id', 'first_name', 'last_name', 'email', 'customer_type')
        json_string = json.loads(str(customers))
        return json_string

    def getCustomerById(customerId):
        customer = Customer.objects.select(
            'id', 'first_name', 'last_name', 'email', 'customer_type', condition=Condition(id__eq=customerId))
        return customer
