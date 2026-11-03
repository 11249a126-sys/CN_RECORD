Aim
To develop a TCP socket-based Python client that connects to a web server, sends an HTTP request, and displays the server response.
Algorithm
18.	Start the program and import the socket module.
19.	Specify the web server name and port number.
20.	Create a TCP socket.
21.	Connect the socket to the web server.
22.	Construct an HTTP GET request and encode it.
23.	Transmit the request to the server.
24.	Receive the server response until the connection is closed.
25.	Decode and display the received response.
26.	Handle socket errors, if any, and close the socket.
27.	Stop the program.
Program
Exp3_http_webclient.py
import socket
 
# Web server details
host = "example.com"
port = 80
 
# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    # Connect to the web server
    client_socket.connect((host, port))
 
    # Send HTTP GET request
    request = (
        "GET / HTTP/1.1\r\n"
        "Host: example.com\r\n"
        "Connection: close\r\n\r\n"
    )
    client_socket.sendall(request.encode())
 
    # Receive webpage response
    response = b""
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data
 
    # Display the response
    print(response.decode("utf-8", errors="replace"))
 
except socket.error as e:
    print("Error:", e)
 
finally:
    client_socket.close()
