import json
from model import BaseModel, BaseManager
from decorators.responsedecorators import jsonresponse_decorator


class Customer(BaseModel):
    manager_class = BaseManager
    table_name = "customer"

    @jsonresponse_decorator
    def getAllCustomers():
        customers = Customer.objects.select(
            'id', 'first_name', 'last_name', 'email')
        json_string = json.loads(str(customers))
        return json_string
