import socket
import argparse
from datetime import datetime


SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}


def scan_port(target, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        sock.close()

        if result == 0:
            service = SERVICES.get(port, "Unknown")
            return f"[OPEN] {port} ({service})"

        return None

    except:
        return None


def main():

    parser = argparse.ArgumentParser(
        description="Cyber Tools Lab Port Scanner v4"
    )

    parser.add_argument(
        "-t",
        "--target",
        required=True
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-100"
    )

    args = parser.parse_args()

    start, end = args.ports.split("-")

    start = int(start)
    end = int(end)

    print("\nCyber Tools Lab Scanner v4")
    print("Target:", args.target)
    print("Started:", datetime.now())

    results = []

    for port in range(start, end + 1):

        result = scan_port(args.target, port)

        if result:
            print(result)
            results.append(result)


    filename = f"tools/reports/report_{args.target}.txt"

    with open(filename, "w") as file:

        file.write(
            "Cyber Tools Lab Scan Report\n"
        )

        for item in results:
            file.write(item + "\n")


    print("\nSaved:", filename)


if __name__ == "__main__":
    main()