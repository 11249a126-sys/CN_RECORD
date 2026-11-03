Aim
To implement a TCP-based echo client and server in which the server returns the message received from the client.
Algorithm
28.	Start the server program.
29.	Create a TCP socket, bind it to the local address and port, and listen for a client.
30.	Accept the incoming client connection.
31.	Start the client program and connect it to the server.
32.	Read a message from the client and send it to the server.
33.	Receive the message at the server and send the same data back.
34.	Display the echoed message at the client.
35.	Repeat the communication until the client enters exit or closes the connection.
36.	Close the client and server sockets.
Program
exp4_eco_server.py
import socket
 
# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind server to localhost and port
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)
 
print("Echo Server is waiting for a connection...")
 
conn, addr = server_socket.accept()
print("Connected by:", addr)
 
while True:
    data = conn.recv(1024)
 
    if not data:
        break
 
    print("Client:", data.decode())
    conn.sendall(data)
 
conn.close()
server_socket.close()
print("Server closed.")
exp4_eco_client.py
import socket
 
# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Connect to the echo server
client_socket.connect(("127.0.0.1", 12345))
 
print("Connected to Echo Server.")
 
while True:
    message = input("Enter message (type 'exit' to quit): ")
 
    if message.lower() == "exit":
        break
 
    client_socket.sendall(message.encode())
 
    data = client_socket.recv(1024)
    print("Echo from Server:", data.decode())
 
client_socket.close()
print("Client closed.")
