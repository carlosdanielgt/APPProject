import unittest
from Strategy import Context
from strategies import quantityitemsdiscount, customertypediscount


class MockProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class MockCustomer:
    def __init__(self, customer_type):
        self.customer_type = customer_type


class TestStrategies(unittest.TestCase):

    def testBuy2Get2Strategy(self):
        context = Context(quantityitemsdiscount.Buy2Get3Discount())
        orderdetails = {}
        orderdetails['customer'] = [MockCustomer('student')]
        orderdetails['items'] = {'product_id': 1, 'quantity': 3}
        mockproduct = MockProduct('Test Product', 10.00)
        orderdetails['product'] = [mockproduct]
        result = context.do_some_business_logic(orderdetails)
        total = result["items"]["total"]
        self.assertEqual(total, 20.0)

    def testStudentTypeStrategy(self):
        context = Context(customertypediscount.CustomerTypeDiscount())
        orderdetails = {}
        orderdetails['customer'] = [MockCustomer('student')]
        orderdetails['items'] = {'product_id': 1, 'quantity': 3}
        mockproduct = MockProduct('Test Product', 10.00)
        orderdetails['product'] = [mockproduct]
        result = context.do_some_business_logic(orderdetails)
        total = result["items"]["total"]
        self.assertEqual(total, 27.0)

    def testEmployeeTypeStrategy(self):
        context = Context(customertypediscount.CustomerTypeDiscount())
        orderdetails = {}
        orderdetails['customer'] = [MockCustomer('employee')]
        orderdetails['items'] = {'product_id': 1, 'quantity': 3}
        mockproduct = MockProduct('Test Product', 10.00)
        orderdetails['product'] = [mockproduct]
        result = context.do_some_business_logic(orderdetails)
        total = result["items"]["total"]
        self.assertEqual(total, 24.0)

    def testAffiliateTypeStrategy(self):
        context = Context(customertypediscount.CustomerTypeDiscount())
        orderdetails = {}
        orderdetails['customer'] = [MockCustomer('affiliate')]
        orderdetails['items'] = {'product_id': 1, 'quantity': 3}
        mockproduct = MockProduct('Test Product', 10.00)
        orderdetails['product'] = [mockproduct]
        result = context.do_some_business_logic(orderdetails)
        total = result["items"]["total"]
        self.assertEqual(total, 25.5)


if __name__ == '__main__':
    unittest.main()
