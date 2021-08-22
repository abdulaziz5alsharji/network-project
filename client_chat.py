import socket
import threading
from termcolor import colored

nickname = input(colored("[+]Choose Your Nickname: ", color="red"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 4444))


def receive() -> None:
    while True:
        message = client.recv(1027).decode("UTF-8")
        if message == "NICK":
            client.send(nickname.encode("UTF-8"))
        else:
            print("\n")
            print(colored(f"[!!]{message}", color="green"))


def send() -> None:
    while True:
        message = '{}: {}'.format(nickname, input(""))
        client.send(message.encode("UTF-8"))


receiveThread = threading.Thread(target=receive)
receiveThread.start()

sendThread = threading.Thread(target=send)
sendThread.start()
