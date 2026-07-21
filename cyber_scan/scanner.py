import socket
from datetime import datetime

from rich.console import Console
from rich.table import Table

from .database import save_scan, create_database
from .exporter import export_csv
from .banner import grab_banner
from .services import SERVICES


VERSION = "14.0.0"

console = Console()


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

            return {
                "port": port,
                "service": SERVICES.get(
                    port,
                    "Unknown"
                ),
                "banner": grab_banner(
                    target,
                    port
                )
            }


    except Exception:

        pass


    return None



def validate_port_range(port_range):

    try:

        start, end = map(
            int,
            port_range.split("-")
        )


        if start < 1 or end > 65535 or start > end:

            raise ValueError


        return start, end


    except ValueError:

        console.print(
            "[red]Invalid port range.[/red]"
        )

        return None, None



def start_scan(target, port_range):

    create_database()


    start, end = validate_port_range(
        port_range
    )


    if start is None:

        return



    console.rule(
        f"[bold cyan]Cyber Tools Lab Scanner v{VERSION}"
    )


    console.print(
        f"[green]Target:[/green] {target}"
    )


    console.print(
        f"[green]Started:[/green] {datetime.now()}"
    )


    table = Table(
        title="Service Detection"
    )


    table.add_column(
        "Port",
        style="cyan"
    )


    table.add_column(
        "Service",
        style="yellow"
    )


    table.add_column(
        "Banner",
        style="green"
    )


    open_ports = []



    for port in range(
        start,
        end + 1
    ):


        result = scan_port(
            target,
            port
        )


        if result:


            open_ports.append(
                result["port"]
            )


            table.add_row(

                str(result["port"]),

                result["service"],

                result["banner"][:50]

            )


            save_scan(

                target,

                result["port"],

                result["service"]

            )



    console.print(table)



    console.rule(
        "[bold green]Scan Summary"
    )


    console.print(
        f"Ports Scanned: {end-start+1}"
    )


    console.print(
        f"Open Ports: {len(open_ports)}"
    )



    if open_ports:

        console.print(
            "Open Ports:",
            ", ".join(
                map(
                    str,
                    open_ports
                )
            )
        )


    else:

        console.print(
            "No open ports found."
        )



    export_csv(
        open_ports
    )


    console.print(
        "\n[bold green]Report saved to reports/report.csv[/bold green]"
    )