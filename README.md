# http_request

This Python script connects to a web server using a socket, sends an HTTP GET request, and prints the server's response. It demonstrates low-level network programming with Python's socket library and basic HTTP communication.

Requirements:
- Python 3

Required libraries:
- socket (comes pre-installed with Python)

Functions:
1. Hostname to IP Resolution
Resolves the provided website hostname (www.example.com) into its corresponding IP address using DNS.

2. Socket Connection
Creates a socket and connects it to the web server using the resolved IP address and the standard HTTP port (80).

3. HTTP Request
Sends a basic HTTP GET request to the web server to retrieve the homepage content (/).

4. Receiving Response
Receives and prints the server's response, which includes HTTP headers and part of the HTML content.

5. Error Handling
Catches and prints any socket-related errors, ensuring the connection is closed properly.

### Example Usage:
The user inputs a website hostname (www.example.com), and the script returns the HTTP response from the server, including headers and content.
If redirected to HTTPS, no actual content will be displayed.
