from Strategy import Context
from orderprocessing import all_strategies
from strategies import *


class Calculator:

    _instance = None

    def __init__(self):
        raise ValueError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
        return cls._instance

    def calculate(self, orderdetails):
        print("Dinamically loaded all strategies: ", all_strategies)
        # context = Context(customertypediscount.CustomerTypeDiscount())
        context = Context(quantityitemsdiscount.Buy2Get3Discount())
        return context.do_some_business_logic(orderdetails)
