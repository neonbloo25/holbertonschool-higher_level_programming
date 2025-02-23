#!/usr/bin/python3
import http.server
import socketserver
"""restfulAPI week! ft.http.server and socketserver"""


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

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    handler = MyRequestHandler

    with socketserver.TCPServer(("localhost", 8000), handler) as httpd:
        print("Server started on http://localhost:8000")
        httpd.serve_forever()
