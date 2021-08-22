import socket
import threading
from termcolor import colored

HOST = "127.0.0.1"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []


def broadcast(message) -> None:
    for client in clients:
        client.send(message)


def handle(client) -> None:
    while True:
        message = client.recv(1027)
        broadcast(message)


def receive() -> None:
    while True:
        client, address = server.accept()
        print(colored(f"[!!]Connected With {address}", color="red"))
        client.send("NICK".encode("UTF-8"))
        nickname = client.recv(1027).decode("UTF-8")
        clients.append(client)
        nicknames.append(nickname)
        print(colored(f"[!!]Nickname Is {nickname}", color="red"))
        broadcast(f"{nickname} Joined!".encode("UTF-8"))
        client.send("Connected To Server!".encode("UTF-8"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(colored("[!!]SERVER LISTENING.....", color="red"))
receive()
