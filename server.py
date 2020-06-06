""" Server for multithreaded (asynchronous) chat application"""

#import the necessary modules
from socket import  AF_INET, socket, SOCK_STREAM
from threading import  Thread

#Setup

clients = {}
addressess = {}

HOST = ""
PORT = 8080
BUFF_SIZE = 1024
ADDRS = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRS)

""" Handle incoming connections """

def accept_incoming_connections():

	while True:
		client, client_address = SERVER.accept()
		print("{} has connected.".format(client_address))
		client.send(bytes("WELCOME\nNOW ENTER YOUR NAME.", "utf8"))

	addressess[client] = client_address
	Thread(target=handle_client, args=(client, )).start()


""" Handle individual clients """

def handle_client(client): #Takes a client socket as argument
	name = client.recv(BUFF_SIZE).decode("utf8")
	welcome = "Hello {}! If you want to quit type {EXIT}.".format(name)
	client.send(bytes(welcome,"utf8"))
	msg = "{} has joined the chat.".format(name)
	broadcast(bytes(msg, "utf8"))
	clients[client] = name
	while  True:
		msg = client.recv(BUFF_SIZE)
		if msg != bytes('{EXIT}', "utf8"):
			broadcast(msg, name+": ")
		else:
			client.send(bytes('{EXIT}', "utf8"))
			client.close()
			del clients[client]
			broadcast(bytes("{} has left the chat.".format(name), "utf8"))
			break

""" broadcast the message to all connected clients"""

def broadcast(msg, prefix=""):
	for client in clients:
		client.send(bytes(prefix, "utf8") + msg)


if __name__ == "__main__":
	SERVER.listen(5)
	print("Waiting for connection!")
	ACCEPT_THREAD = Thread(target=accept_incoming_connections)
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	SERVER.close()
