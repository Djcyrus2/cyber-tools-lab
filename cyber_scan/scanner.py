import socket
from datetime import datetime
from .database import save_scan, create_database


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

    create_database()

    start, end = port_range.split("-")

    print("\n=== Cyber Tools Lab Scanner v9 ===")

    print(
        "Target:",
        target
    )

    print(
        "Started:",
        datetime.now()
    )


    open_ports = []


    for port in range(
        int(start),
        int(end) + 1
    ):

        result = scan_port(
            target,
            port
        )


        if result:

            print(
                f"[OPEN] Port {result}"
            )


            open_ports.append(result)


            save_scan(
                target,
                result,
                "OPEN"
            )


    print("\nScan complete")

    print(
        "Open ports found:",
        len(open_ports)
    )