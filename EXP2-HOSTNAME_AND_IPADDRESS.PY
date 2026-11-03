Aim
To write a Python program that retrieves and displays the hostname and IP address of the local computer.
Algorithm
12.	Begin the program.
13.	Import the socket module.
14.	Obtain the system hostname using gethostname().
15.	Find the IP address associated with the hostname using gethostbyname().
16.	Display the hostname and IP address.
17.	Terminate the program.
Program
Exp2_Hostname_and_IPaddress.py
import socket
 
# Get the hostname
hostname = socket.gethostname()
 
# Get the IP address
ip_address = socket.gethostbyname(hostname)
 
print("Host Name:", hostname)
print("IP Address:", ip_address)
