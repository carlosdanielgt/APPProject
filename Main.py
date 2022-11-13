from http.server import HTTPServer
from customer import Customer
from manager import BaseManager
from server import MyServer

HOSTNAME = "localhost"
SERVERPORT = 8080


def connectdatabase():
    BaseManager.set_connection()
    print("Connection set")


if __name__ == "__main__":
    connectdatabase()
    webServer = HTTPServer((HOSTNAME, SERVERPORT), MyServer)
    print("Server started http://%s:%s" % (HOSTNAME, SERVERPORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
