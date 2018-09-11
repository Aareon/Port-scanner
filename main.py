# Network port scanner
# Focus first will be on making the functionality of the software.
# Second focus will be on lowering the runtime of the software.


import socket
import logging


class SConnect:

    def __init__(self, ip, port=None):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.s_connection = socket.socket()

    def portscan(self):
        try:
            self.s_connection.connect(self.address)

        except ConnectionRefusedError as err:
            logging.warning(err)


def main():

    logging.basicConfig(filename="errlog.log", format="%(asctime)s : %(message)s")
    logging.info("Start")
    print("Hello user and welcome to Network Port Scanner!\n")
    print("Please insert a IP address that you want to scan for open and closed ports\n")
    u_ip = input("Target IP: ")

    if u_ip is not None:
        for p in range(1, 10000):
            c = SConnect(u_ip, p)
            c.portscan()
    else:
        print("You failed, terminating.\n")

    logging.info("Finished")


if __name__ == '__main__':
    main()
