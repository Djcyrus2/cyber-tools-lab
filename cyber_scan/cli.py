import argparse

from .scanner import start_scan
from .database import show_history
from .discovery import discover_hosts


VERSION = "13.0.0"


def main():

    parser = argparse.ArgumentParser(
        description="Cyber Tools Lab Scanner"
    )


    parser.add_argument(
        "-t",
        "--target",
        help="Target IP address"
    )


    parser.add_argument(
        "-p",
        "--ports",
        default="1-100",
        help="Port range example: 1-1000"
    )


    parser.add_argument(
        "--history",
        action="store_true",
        help="Show scan history"
    )


    parser.add_argument(
        "--discover",
        help="Discover live hosts example: 192.168.1.0"
    )


    parser.add_argument(
        "--version",
        action="version",
        version=f"Cyber Tools Lab Scanner v{VERSION}"
    )


    args = parser.parse_args()


    # Show previous scans
    if args.history:

        show_history()

        return



    # Discover hosts on network
    if args.discover:

        print("\n=== Host Discovery ===")

        print(
            "Network:",
            args.discover
        )


        hosts = discover_hosts(
            args.discover
        )


        if not hosts:

            print(
                "No live hosts found."
            )

        else:

            print(
                "\nLive Hosts:\n"
            )


            for host in hosts:

                print(
                    f"{host['ip']} - {host['hostname']}"
                )


            with open(
                "reports/hosts.txt",
                "w"
            ) as file:


                for host in hosts:

                    file.write(
                        f"{host['ip']} - {host['hostname']}\n"
                    )


            print(
                "\nSaved to reports/hosts.txt"
            )


        return



    # Normal port scan

    if args.target:

        start_scan(
            args.target,
            args.ports
        )

    else:

        parser.print_help()



if __name__ == "__main__":

    main()