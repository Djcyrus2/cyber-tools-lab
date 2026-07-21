import argparse
from .scanner import start_scan
from .database import show_history


def main():

    parser = argparse.ArgumentParser(
        description="Cyber Tools Lab Scanner v9"
    )


    parser.add_argument(
        "-t",
        "--target"
    )


    parser.add_argument(
        "-p",
        "--ports",
        default="1-100"
    )


    parser.add_argument(
        "--history",
        action="store_true",
        help="Show previous scans"
    )


    args = parser.parse_args()


    if args.history:

        show_history()
        return


    start_scan(
        args.target,
        args.ports
    )


if __name__ == "__main__":
    main()