#!/usr/bin/python3

import socket

# Function to resolve the website's IP address
def get_ip_from_hostname(hostname):
    return socket.gethostbyname(hostname)

# Website to check
hostname = input("Please enter the website (e.g., www.example.com): ")
port = 80  # Standard HTTP port

# Resolve the hostname to an IP address
ip = get_ip_from_hostname(hostname)

# Connect to the website
s = socket.socket()
try:
    s.connect((ip, port))
    print(f"Connected to {hostname} ({ip}) on port {port}")
    
    # Send a basic HTTP GET request
    request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
    s.send(request.encode())

    # Receive and print the response
    response = s.recv(4096)  # Increased buffer size
    print(response.decode())

except socket.error as err:
    print(f"Socket error: {err}")

finally:
    s.close()
