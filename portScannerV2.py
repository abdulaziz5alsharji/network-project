import sys

try:
    import os
    import socket
    import threading
    import queue
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")

qu = queue.Queue()


def portScanner(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    connection = sock.connect_ex((host, port))
    if connection == 0:
        return True
    else:
        return False


def Scanning(host: str, port: int) -> None:
    try:
        result = portScanner(host, port)
        if result:
            print(colored(f"[+]Port {port} Is Open", color="blue"))
        else:
            print(colored(f"[+]Port {port} Is Close", color="red"))
    except KeyboardInterrupt:
        print(colored("[!!]Exit Program !!!!", color="red"))
        sys.exit()
    except socket.gaierror:
        print(colored("[!!]Hostname Could Not Be Resolved !!!!", color="red"))
        sys.exit()
    except socket.error:
        print(colored("[!!]Server not responding !!!!", color="red"))
        sys.exit()


def working(host: str) -> None:
    threads = []
    for port in range(qu.qsize()):
        thread = threading.Thread(target=Scanning, args=(host, qu.get()))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def option(mode: int) -> None:
    try:
        if mode == 1:
            for port in range(1, 1025):
                qu.put(port)
        elif mode == 2:
            for port in range(1, 49153):
                qu.put(port)
        elif mode == 3:
            ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
            for port in ports:
                qu.put(port)
        elif mode == 4:
            print("\n")
            start = int(input(colored("[++]START: ", color="blue")))
            end = int(input(colored("[++]END: ", color="blue")))
            for port in range(start, end + 1):
                qu.put(port)
        elif mode == 5:
            print("\n")
            ports = list(map(int, input(colored("[++]PORTS: ", color="blue")).split()))
            for port in ports:
                qu.put(port)
        elif mode == 99:
            sys.exit()
    except ValueError as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("PORT SCANNER V3"), color="blue"))
    print("\n")
    print(colored("""
[1]Scan From 1 To 1024
[2]Scan From 1 To 49152 
[3]Scan 20, 21, 22, 23, 25, 53, 80, 110, 443
[4]Choose Range
[5]Choose Ports Example (80 69 29 27 ....)
[99]Exit
    """, color="blue"))
    print("\n")
    MODE = int(input(colored("[++]MODE: ", color="blue")))
    HOST = str(input(colored("[++]TARGET: ", color="blue")))
    option(mode=MODE)
    working(host=HOST)
