from http.server import BaseHTTPRequestHandler
import json
import random
from customer import Customer
from product import Product
from order import Order

DEFAULT_ENCODING = 'utf-8'


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/api/customers':
            Customer.getAllCustomers(self)
        elif self.path == '/api/products':
            Product.getAllProducts(self)
        elif self.path == '/api/orders':
            Order.getAllOrders(self)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes("<html><head><title>Not found</title></head>", DEFAULT_ENCODING))
            self.wfile.write(bytes("<body>", DEFAULT_ENCODING))
            self.wfile.write(bytes("<p>Not found</p>", DEFAULT_ENCODING))
            self.wfile.write(bytes("</body></html>", DEFAULT_ENCODING))

    def do_POST(self):
        if self.path == '/api/orders':
            # get request body
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            json_items = json.loads(body.decode(DEFAULT_ENCODING))
            # generate random number
            customer_id = random.randint(1, 2)
            customer = Customer.getCustomerById(customer_id)
            product = Product.getProductById(json_items['product_id'])
            orderdetails = {}
            orderdetails['customer'] = customer
            orderdetails['items'] = json_items
            orderdetails['product'] = product
            calculated_order = Order.calculateOrderTotal(self, orderdetails)
            print(calculated_order)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(
                bytes(str(calculated_order), DEFAULT_ENCODING))
