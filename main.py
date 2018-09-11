# Network port scanner
# Focus first will be on making the functionality of the software.
# Second focus will be on lowering the runtime of the software.


import socket
import logging
from time import perf_counter


class SConnect:
    def __init__(self, ip, port=None):
        self.address = (ip, port)
        self.s_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_connection.settimeout(0.3)

    def port_is_open(self):
        connection = self.s_connection.connect_ex(self.address)
        if connection == 0:
            return True
        else:
            return False


def main():
    print("\nHello user and welcome to Network Port Scanner!\n \
           Please insert a IP address that you want to scan for open and closed ports.\n \
           The range of ports scanned is 1-65535.\n")

    target_ip = input("Target IP: ")
    if target_ip is None:
        raise EOFError("You must provide a target IP")

    open_pcounter = 0
    closed_pcounter = 0

    for p in range(1, 65536):
        start = perf_counter()
        c = SConnect(u_ip, p)
        if c.port_is_open():
            print("Port {} is open".format(p))
            open_pcounter += 1
        else:
            print("Port {} is closed".format(p))
            closed_pcounter += 1
        duration = perf_counter() - start
        print("--- {:.3} seconds ---".format(duration))

    print("Total open ports: {}".format(open_pcounter))
    print("Total closed ports: {}".format(closed_pcounter))


if __name__ == '__main__':
    main()
