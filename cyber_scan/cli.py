import argparse

from .scanner import start_scan



VERSION = "20.0.0"



def main():

    parser = argparse.ArgumentParser(

        description="Cyber Tools Lab Network Scanner"

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
        required=True,
        help="Port range example: 1-1000"

    )


    parser.add_argument(

        "--threads",
        type=int,
        default=100,
        help="Number of scanning threads"

    )


    parser.add_argument(

        "--version",
        action="store_true",
        help="Show scanner version"

    )



    args = parser.parse_args()



    if args.version:

        print(
            f"Cyber Tools Lab Scanner v{VERSION}"
        )

        return



    start_scan(

        args.target,

        args.ports

    )




if __name__ == "__main__":

    main()