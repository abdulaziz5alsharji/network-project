import sys

try:
    import socket
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .."))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def portScanner(host: str, start: int, end: int) -> None:
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(start, end + 1):
        try:
            socketObject.connect((host, port))
            print(f"Port {port} Is Open")
        except OSError:
            print(f"Port {port} Is Close")


def portScannerTwo(host: str, port: int) -> str:
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socketObject.connect((host, port))
        return f"Port {port} Is Open"
    except OSError:
        return f"Port {port} Is Close"


def main():
    try:
        clear()
        print()
        print(colored(figlet_format("Port Scanner"), color="blue"))
        print("\n")
        HOST = input(colored("[+] Host :", color="blue"))
        startPort = int(input(colored("[+] Start Port :", color="blue")))
        endPort = int(input(colored("[+] End Port :", color="blue")))
        for port in range(startPort, endPort+1):
            print()
            print(f"[+]{colored(portScannerTwo(host=HOST, port=port), color='blue')}")
    except ValueError as er:
        print(colored(er, color="red"))


if __name__ == '__main__':
    main()
