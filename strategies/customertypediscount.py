import json
from Strategy import Strategy

STUDENT_DISCOUNT = 0.1
EMPLOYEE_DISCOUNT = 0.2
AFFILIATE_DISCOUNT = 0.15


class CustomerTypeDiscount(Strategy):
    def checkvalidity(self, orderdetails):
        if orderdetails['customer'][0].customer_type == "student":
            return STUDENT_DISCOUNT
        elif orderdetails['customer'][0].customer_type == "employee":
            return EMPLOYEE_DISCOUNT
        elif orderdetails['customer'][0].customer_type == "affiliate":
            return AFFILIATE_DISCOUNT
        else:
            return 0

    def do_algorithm(self, orderdetails: dict):
        discount = self.checkvalidity(orderdetails)
        if discount > 0:
            customertype = orderdetails['customer'][0].customer_type
            print(f'Applying {discount * 100}% {customertype} discount')
            item = orderdetails['items']
            product = orderdetails['product'][0]
            item['subtotal'] = round(
                float(item['quantity']) * float(product.price), 2)
            item['discount'] = round(
                (item['subtotal'] * (discount)), 2)
            item['total'] = round(item['subtotal'] - item['discount'], 2)
            orderdetails["items"] = item
            return orderdetails
