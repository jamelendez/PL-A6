# PL-A6 - PONEL
Asignación 6 del curso ICOM-4036. 

Jose A. Melendez Morales & Jose A. Santiago 
PONEL is a language that simplifies the communication from client-to-server from your own device. This language provides a series of commands that are simple to follow to create servers and clients, send messages and receive an update of new activities in the server. We used PLY libraries for the parsing (YACC) and lexing (LEX) operations in the language reader.

Usage:

Run PONEL.py in terminal (python3 PONEL.py) or in your preferred IDE (IntelliJ, Eclipse, PyCharm,etc)
Run the listed commands below
The commands are:

create_server  Create a server
create_client  Create a client
bind  Creates port, type port address from 1024 forward
listen  Enables connection from clients to servers
connect  Set connection to desired device, device name and parameters needed.
accept  Accepts the connection with client and sever
send  Create and send messages to the other end of the client, string line needed.
receive  Receive feedback from server.
close_client  Closes the connection with client.
close_server  Closes the server
Contributors:

Support:

Python 3.
