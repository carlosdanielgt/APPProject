from Strategy import Context
from orderprocessing import all_strategies
from strategies import *


class Calculator:

    def calculate(self, orderdetails):
        print("Dinamically loaded all strategies: ", all_strategies)
        # context = Context(customertypediscount.CustomerTypeDiscount())
        context = Context(quantityitemsdiscount.Buy2Get3Discount())
        return context.do_some_business_logic(orderdetails)
