import sys

try:
    import os
    from getmac import get_mac_address
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def getMacAddress(host: str) -> str:
    return get_mac_address(ip=host)


def default() -> None:
    ip = "192.168.1."
    print(colored("IP\t\t\t\t\t\t\t\t\tMAC", color="blue"))
    print(colored("==============================================", color="blue"))
    for number in range(100, 120):
        HOST = f"{ip}{number}"
        MAC = getMacAddress(host=HOST)
        if MAC is None:
            continue
        print(colored(f"{HOST}\t\t\t\t{MAC}", color="blue"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Mac Address"), color="blue"))
    print("\n")
    print(colored("""
[1]Default
[2]Ip
[0]Exit
    """, color="blue"))
    try:
        mode = int(input(colored("Option: ", color="blue")))
        print("\n")
        if mode == 1:
            default()
        elif mode == 2:
            IP = str(input(colored("IP: ", color="blue")))
            mac = getMacAddress(host=IP)
            if mac is None:
                print(colored("[!!]Not Found..", color="red"))
                sys.exit()
            print(colored("IP\t\t\t\t\t\t\t\t\tMAC", color="blue"))
            print(colored("==============================================", color="blue"))
            print(colored(f"{IP}\t\t\t\t{mac}", color="blue"))
        elif mode == 0:
            sys.exit()
        else:
            print(colored("[!!]Invalid Option...", color="red"))
            input(colored("[!]Press Any Key To Exit .. ", color="red"))
            sys.exit()
    except ValueError as e:
        print(colored(e, color="red"))
