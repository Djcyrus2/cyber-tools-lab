import socket
from datetime import datetime


def scan_port(target, port):

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(1)

        result = sock.connect_ex(
            (target, port)
        )

        sock.close()


        if result == 0:
            return port


    except:
        pass


    return None



def start_scan(target, port_range):

    start, end = port_range.split("-")


    print(
        "\nCyber Tools Lab Scanner v8"
    )

    print(
        "Target:",
        target
    )

    print(
        "Started:",
        datetime.now()
    )


    for port in range(
        int(start),
        int(end)+1
    ):

        result = scan_port(
            target,
            port
        )


        if result:

            print(
                f"[OPEN] Port {result}"
            )


    print(
        "\nScan complete"
    )