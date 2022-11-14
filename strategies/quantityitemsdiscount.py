from Strategy import Strategy


class Buy2Get3Discount(Strategy):
    def checkvalidity(self, orderdetails):
        item = orderdetails['items']
        product = orderdetails['product'][0]
        if item['quantity'] == 3:
            return float(product.price)

    def do_algorithm(self, orderdetails: dict):
        discount = self.checkvalidity(orderdetails)
        if discount > 0:
            item = orderdetails['items']
            product = orderdetails['product'][0]
            print(
                f'Applying Buy 2 Get 3 promotion for product: {product.name}')
            item['subtotal'] = round(
                float(item['quantity']) * float(product.price), 2)
            item['discount'] = discount
            item['total'] = round(item['subtotal'] - item['discount'], 2)
            orderdetails["items"] = item
            return orderdetails
