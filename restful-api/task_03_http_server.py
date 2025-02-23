#!/usr/bin/python3
import http.server
import socketserver
"""restfulAPI week! ft.http.server and socketserver"""


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    """Class - Request Handler"""
    def do_GET(self):
        """Func - Get requests"""
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b"Hello, this is a simple API!")

if __name__ == "__main__":
    handler = MyRequestHandler

    with socketserver.TCPServer(("localhost", 8000), handler) as httpd:
        print("Server started on http://localhost:8000")
        httpd.serve_forever()
