Python Load Balancer
This project implements a basic Load Balancer in Python, designed to distribute incoming HTTP requests across a pool of backend servers. It aims to enhance the availability and reliability of web applications by efficiently managing the request load among multiple servers.

Features
Round Robin Scheduling: Distributes incoming requests equally across all servers.
Health Checks: Periodically checks the health of backend servers to ensure requests are only forwarded to operational servers.
Easy Configuration: Simple configuration file to add or remove servers from the pool.
Logging: Comprehensive logging of requests and server status for easy debugging and monitoring.
Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.6 or later
pip (Python package installer)
Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/python-load-balancer.git
Navigate to the project directory:
bash
Copy code
cd python-load-balancer
Install the required dependencies:
Copy code
pip install -r requirements.txt
Configuration
To configure the load balancer, edit the config.json file in the root directory. Add your backend servers and their respective addresses as follows:

json
Copy code
{
  "servers": [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002",
    // Add more servers as needed
  ]
}
Running the Load Balancer
To start the load balancer, run:

Copy code
python load_balancer.py
By default, the load balancer will listen on port 8080. You can change this and other settings in the config.json file.

Usage
With the load balancer running, direct your HTTP requests to the load balancer's IP and port. The load balancer will then forward your requests to one of the backend servers in the pool, according to the configured scheduling algorithm.

Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.
