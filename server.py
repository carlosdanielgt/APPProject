from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/customers':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                bytes("""{
	"id": 1,
	"first_name": "John",
	"last_name": "Doe",
	"email": "johndoe@mail.com"
}""", "utf-8"))
        if self.path == '/api/products':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                bytes("""[
    {
	"id": 100,
	"name": "salad",
	"price": 5.99,
    "image_link": "https://www.google.com"
    },
    {
        "id": 101,
        "name": "shawarma",
        "price": 5.99,
        "image_link": "https://www.google.com"
    },
    {
        "id": 102,
        "name": "pizza",
        "price": 5.99,
        "image_link": "https://www.google.com"
    }
]""", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(
            bytes("<p>POST request for {}</p>".format(self.path), "utf-8"))
        self.wfile.write(bytes("<p>POST body:</p>", "utf-8"))
        self.wfile.write(
            bytes("<p><pre>{}</pre></p>".format(post_data.decode('utf-8')), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
