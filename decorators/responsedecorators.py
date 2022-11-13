import json


def jsonresponse_decorator(function):
    def wrapper(self):
        func = function()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(
            bytes(json.dumps(func), "utf-8"))
    return wrapper
