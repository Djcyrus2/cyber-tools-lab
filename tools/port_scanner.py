 import socket
import argparse
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


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
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.5)

        result = sock.connect_ex(
            (target, port)
        )

        sock.close()

        if result == 0:
            return {
                "port": port,
                "service": SERVICES.get(port, "Unknown"),
                "status": "open"
            }

    except:
        pass

    return None


def main():

    parser = argparse.ArgumentParser(
        description="Cyber Tools Lab Scanner v5"
    )

    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="Target IP"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-100",
        help="Port range"
    )

    args = parser.parse_args()


    start, end = args.ports.split("-")

    ports = range(
        int(start),
        int(end)+1
    )


    print("\n=== Cyber Tools Lab Scanner v5 ===")
    print("Target:", args.target)
    print("Time:", datetime.now())


    results = []


    with ThreadPoolExecutor(
        max_workers=50
    ) as executor:

        scans = executor.map(
            lambda p: scan_port(args.target,p),
            ports
        )


        for result in scans:

            if result:
                print(
                    f"[OPEN] {result['port']} - {result['service']}"
                )

                results.append(result)


    report = {
        "target": args.target,
        "scan_time": str(datetime.now()),
        "open_ports": results
    }


    filename = (
        "tools/reports/report.json"
    )


    with open(filename,"w") as file:
        json.dump(
            report,
            file,
            indent=4
        )


    print(
        "\nReport saved:",
        filename
    )


if __name__ == "__main__":
    main()