from http.server import BaseHTTPRequestHandler
import json
from customer import Customer
from product import Product
from order import Order
from orderprocessing.calculator import Calculator

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
            print(json_items)
            # create order
            # order = Order()
            calculator = Calculator()
            calculator.calculate(json_items)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                bytes(json.dumps({'response': 'ok'}), DEFAULT_ENCODING))
