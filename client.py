from socket import socket, AF_INET, SOCK_STREAM


def client(host: str, port=777) -> None:
    sockObject = socket(AF_INET, SOCK_STREAM)
    sockObject.connect((host, port))
    while True:
        sockObject.send(input("Message :").encode())
        data = sockObject.recv(1800)
        print(data.decode())


if __name__ == '__main__':
    Host = "192.168.1.100"
    client(host=Host)
