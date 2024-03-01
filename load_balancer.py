from flask import Flask, request
from werkzeug.serving import run_simple
import requests

app = Flask(__name__)

# List of backend servers
servers = ['http://localhost:5000', 'http://localhost:5001']
current_server = 0

@app.route('/')
def load_balancer():
    global current_server
    # Distribute requests among servers in a round-robin fashion
    server_url = servers[current_server]
    current_server = (current_server + 1) % len(servers)

    # Forward the request to the selected backend server
    response = requests.get(server_url + request.full_path)
    return response.text

if __name__ == '__main__':
    run_simple('localhost', 8000, app)