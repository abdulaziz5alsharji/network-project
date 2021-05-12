from socket import socket, AF_INET, SOCK_STREAM
import socket as sock


def Client(host: str, port=80) -> str:
    sockObject = socket(AF_INET, SOCK_STREAM)
    sockObject.connect((host, port))
    sockObject.send(f"GET / HTTP/1.1\r\nHost:{host}\r\n\r\n".encode())
    data = sockObject.recv(1800)
    sockObject.close()
    return data.decode()


if __name__ == '__main__':
    Host = "www.google.com"
    print(Client(Host))
