#!/usr/bin/python3
import http.server
import socketserver
import json
"""restfulAPI week! ft.http.server, socketserver and json"""


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    """Class - Request Handler"""
    def do_GET(self):
        """Func - Get requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=http.server.HTTPServer, handler_class=MyRequestHandler):
    with socketserver.TCPServer(("localhost", 8000), handler_class) as httpd:
        print("Server started on http://localhost:8000")
        httpd.serve_forever()


if __name__ == "__main__":
    run()
