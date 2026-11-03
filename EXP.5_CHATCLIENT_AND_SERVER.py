Aim
To establish a two-way communication system between a client and a server using TCP socket programming.
Algorithm
37.	Start the chat server and create a TCP socket.
38.	Bind the socket to the specified local address and port, then listen for a connection.
39.	Accept the client connection.
40.	Run the client and connect it to the server.
41.	Allow the client to enter and send a message.
42.	Receive and display the message at the server.
43.	Allow the server to enter a reply and send it to the client.
44.	Receive and display the reply at the client.
45.	Continue the exchange until either side enters exit.
46.	Close the connection and terminate both programs.
Program
exp5_chat_server.py
import socket
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12346))
server.listen(1)
 
print("Chat Server is waiting for a client...")
 
conn, addr = server.accept()
print("Client connected:", addr)
print("Type 'exit' to close the chat.")
 
while True:
    message = conn.recv(1024).decode()
 
    if not message or message.lower() == "exit":
        print("Client disconnected.")
        break
 
    print("Client:", message)
 
    reply = input("You: ")
    conn.sendall(reply.encode())
 
    if reply.lower() == "exit":
        break
 
conn.close()
server.close()
print("Chat Server closed.")
exp5_chat_client.py
import socket
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12346))
 
print("Connected to Chat Server!")
print("Type 'exit' to close the chat.")
 
while True:
    message = input("You: ")
    client.sendall(message.encode())
 
    if message.lower() == "exit":
        break
 
    reply = client.recv(1024).decode()
 
    if not reply or reply.lower() == "exit":
        print("Server disconnected.")
        break
 
    print("Server:", reply)
 
client.close()
print("Chat Client closed.")
