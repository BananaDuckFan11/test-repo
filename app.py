from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hello World!</h1>')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 - Not Found</h1>')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever()
