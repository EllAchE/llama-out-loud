from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Assuming the incoming data is JSON
        try:
            data = json.loads(post_data.decode('utf-8'))
            print("Received POST request with data:", data)
        except json.JSONDecodeError:
            print("Received non-JSON data:", post_data.decode('utf-8'))

        # Send a response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'status': 'received'}
        self.wfile.write(json.dumps(response).encode('utf-8'))


if __name__ == '__main__':
    server_address = ('127.0.0.1', 8040)  # Listen on localhost at port 4040
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on http://127.0.0.1:4040...")
    httpd.serve_forever()
