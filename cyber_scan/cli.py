import argparse
from .scanner import start_scan


def main():

    parser = argparse.ArgumentParser(
        description="Cyber Tools Lab Scanner v8"
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
        default="1-100",
        help="Port range"
    )


    parser.add_argument(
        "--version",
        action="version",
        version="Cyber Scanner v8.0.0"
    )


    args = parser.parse_args()


    start_scan(
        args.target,
        args.ports
    )


if __name__ == "__main__":
    main()