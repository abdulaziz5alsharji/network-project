from socket import socket, AF_INET, SOCK_STREAM


def server(host: str, port=777) -> None:
    sockObject = socket(AF_INET, SOCK_STREAM)
    sockObject.bind((host, port))
    sockObject.listen(1)
    client, address = sockObject.accept()
    while True:
        data = client.recv(1800)
        print(data.decode())
        client.send(input("Message :").encode())


if __name__ == '__main__':
    Host = "0.0.0.0"
    server(host=Host)
