import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "front end"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving files from the '{DIRECTORY}' directory at http://localhost:{PORT}")
    print("Navigate to http://localhost:8080/index.html to see your landing page.")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()