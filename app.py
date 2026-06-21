from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

def fibonacci(n):
    """Calculate fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def process_numbers(count):
    """Process numbers with a for loop"""
    results = []
    for i in range(count):
        results.append(i * 2)
    return results

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hello World!</h1>')
        elif path == '/fibonacci':
            try:
                n = int(query_params.get('n', [5])[0])
                result = fibonacci(n)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({'n': n, 'result': result})
                self.wfile.write(response.encode())
            except (ValueError, IndexError):
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Invalid parameter'}).encode())
        elif path == '/process':
            try:
                count = int(query_params.get('count', [10])[0])
                results = process_numbers(count)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({'count': count, 'results': results})
                self.wfile.write(response.encode())
            except (ValueError, IndexError):
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Invalid parameter'}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 - Not Found</h1>')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print('Server running on http://localhost:8000')
    print('Available endpoints:')
    print('  GET / - Hello World')
    print('  GET /fibonacci?n=5 - Calculate fibonacci number')
    print('  GET /process?count=10 - Process numbers with for loop')
    httpd.serve_forever()
