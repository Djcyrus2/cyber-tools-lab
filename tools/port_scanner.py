 import socket
import argparse
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from logger import write_log


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


def load_config():

    with open("tools/config.json", "r") as file:
        return json.load(file)



def scan_port(target, port, timeout):

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(timeout)

        result = sock.connect_ex(
            (target, port)
        )

        sock.close()


        if result == 0:

            return {
                "port": port,
                "service": SERVICES.get(
                    port,
                    "Unknown"
                ),
                "status": "OPEN"
            }


    except:

        pass


    return None



def main():

    config = load_config()


    parser = argparse.ArgumentParser(
        description="Cyber Tools Lab Scanner v7"
    )


    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="Target IP address"
    )


    parser.add_argument(
        "-p",
        "--ports",
        default=config["default_ports"],
        help="Port range example 1-1000"
    )


    args = parser.parse_args()


    start, end = args.ports.split("-")


    print("\n=== Cyber Tools Lab Scanner v7 ===")
    print("Target:", args.target)
    print("Started:", datetime.now())


    write_log(
        f"Scan started: {args.target}"
    )


    results = []


    with ThreadPoolExecutor(
        max_workers=config["threads"]
    ) as executor:


        scans = executor.map(
            lambda port:
            scan_port(
                args.target,
                port,
                config["timeout"]
            ),

            range(
                int(start),
                int(end)+1
            )
        )


        for result in scans:

            if result:

                print(
                    f"[{result['status']}] "
                    f"{result['port']} "
                    f"- {result['service']}"
                )

                results.append(result)



    report = {

        "target": args.target,

        "time": str(datetime.now()),

        "results": results

    }


    with open(
        "tools/reports/report.json",
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    write_log(
        "Scan completed"
    )


    print(
        "\nReport saved!"
    )



if __name__ == "__main__":
    main()