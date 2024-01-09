import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="crt/privkey.pem", 
        certfile='crt/cert.pem', server_side=True)
httpd.serve_forever()
