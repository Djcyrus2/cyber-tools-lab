import socket
from datetime import datetime
from rich.console import Console
from rich.table import Table

from .database import save_scan, create_database
from .exporter import export_csv


VERSION = "12.0.0"

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
            return port

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
        title="Open Ports"
    )

    table.add_column(
        "Port",
        style="cyan"
    )

    table.add_column(
        "Status",
        style="green"
    )

    open_ports = []

    total_ports = end - start + 1

    for port in range(
        start,
        end + 1
    ):

        result = scan_port(
            target,
            port
        )

        if result:

            table.add_row(
                str(result),
                "OPEN"
            )

            open_ports.append(result)

            save_scan(
                target,
                result,
                "OPEN"
            )

    console.print(table)

    console.rule("[bold green]Summary")

    console.print(
        f"Ports Scanned : {total_ports}"
    )

    console.print(
        f"Open Ports    : {len(open_ports)}"
    )

    export_csv(open_ports)

    console.print(
        "\n[bold green]CSV report saved to reports/report.csv[/bold green]"
    )