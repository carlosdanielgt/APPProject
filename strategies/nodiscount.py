from Strategy import Strategy


class NoDiscount(Strategy):
    def checkvalidity(self):
        return 0

    def do_algorithm(self, orderdetails: dict):
        discount = self.checkvalidity()
        if discount == 0:
            item = orderdetails['items']
            product = orderdetails['product'][0]
            print('No discount applied')
            item['subtotal'] = round(
                float(item['quantity']) * float(product.price), 2)
            item['discount'] = discount
            item['total'] = round(item['subtotal'] - item['discount'], 2)
            orderdetails["items"] = item
            return orderdetails
