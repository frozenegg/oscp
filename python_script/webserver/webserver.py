import socketserver
import http.server

with socketserver.TCPServer(('192.168.2.106', 8000), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
