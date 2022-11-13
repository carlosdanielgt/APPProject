from http.server import BaseHTTPRequestHandler
import json
from customer import Customer
from product import Product
from order import Order

DEFAULT_ENCODING = 'utf-8'


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/api/customers':
            customers = Customer.objects.select(
                'id', 'first_name', 'last_name', 'email')
            json_string = json.loads(str(customers))
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                bytes(json.dumps(json_string), DEFAULT_ENCODING))
        elif self.path == '/api/products':
            products = Product.objects.select(
                'id', 'name', 'price', 'image_link')
            json_string = json.loads(str(products))
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                bytes(json.dumps(json_string), DEFAULT_ENCODING))
        elif self.path == '/api/orders':
            orders = Order.objects.select(
                'id', 'customer_id', 'product_id', 'price', 'quantity', 'tps', 'tvq', 'discount', 'total')
            json_string = json.loads(str(orders))
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                bytes(json.dumps(json_string), DEFAULT_ENCODING))
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
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", DEFAULT_ENCODING))
        self.wfile.write(bytes("<body>", DEFAULT_ENCODING))
        self.wfile.write(
            bytes("<p>POST request for {}</p>".format(self.path), DEFAULT_ENCODING))
        self.wfile.write(bytes("<p>POST body:</p>", DEFAULT_ENCODING))
        self.wfile.write(
            bytes("<p><pre>{}</pre></p>".format(post_data.decode('utf-8')), DEFAULT_ENCODING))
        self.wfile.write(bytes("</body></html>", DEFAULT_ENCODING))
