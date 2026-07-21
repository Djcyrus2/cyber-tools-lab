from .discovery import discover_hosts
parser.add_argument(
    "--discover",
    help="Discover live hosts (example: 192.168.1.0)"
)
if args.discover:

    hosts = discover_hosts(args.discover)

    print("\nLive Hosts Found:\n")

    for host in hosts:

        print(
            host["ip"],
            "-",
            host["hostname"]
        )

    with open(
        "reports/hosts.txt",
        "w"
    ) as file:

        for host in hosts:

            file.write(
                f"{host['ip']} - {host['hostname']}\n"
            )

    return