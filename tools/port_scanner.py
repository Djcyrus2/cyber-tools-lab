import socket
import argparse
from datetime import datetime


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        sock.close()

        if result == 0:
            return "OPEN"
        else:
            return "CLOSED"

    except Exception:
        return "ERROR"


def main():

    parser = argparse.ArgumentParser(
        description="Cyber Tools Lab - TCP Port Scanner"
    )

    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="Target IP address"
    )

    args = parser.parse_args()

    target = args.target

    ports = [21,22,23,53,80,443,8080]

    filename = f"tools/reports/scan_{target}.txt"

    print("\n=== Cyber Tools Lab Scanner ===")
    print("Target:", target)
    print("Started:", datetime.now())

    results = []

    for port in ports:
        status = scan_port(target, port)

        line = f"Port {port}: {status}"

        print(line)

        results.append(line)


    with open(filename, "w") as file:
        file.write("Cyber Tools Lab Scan Report\n")
        file.write(f"Target: {target}\n")
        file.write(f"Time: {datetime.now()}\n\n")

        for result in results:
            file.write(result + "\n")


    print("\nReport saved:", filename)


if __name__ == "__main__":
    main()