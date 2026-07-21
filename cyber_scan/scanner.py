from datetime import datetime

from rich.console import Console
from rich.table import Table

from .database import save_scan, create_database
from .exporter import export_csv
from .thread_scanner import threaded_scan
from .os_detect import detect_os
from .vulnerability import check_vulnerability


VERSION = "17.0.0"

console = Console()



def validate_port_range(port_range):

    try:

        start, end = map(
            int,
            port_range.split("-")
        )


        if (
            start < 1
            or end > 65535
            or start > end
        ):

            raise ValueError


        return start, end


    except ValueError:

        console.print(
            "[red]Invalid port range. Example: 1-1000[/red]"
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


    # OS Detection

    os_info = detect_os(
        target
    )


    console.print(
        f"[green]OS Guess:[/green] {os_info}"
    )


    console.print(
        "[yellow]Scanning with 100 threads...[/yellow]"
    )



    table = Table(
        title="Security Scan Results"
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


    table.add_column(
        "Risk",
        style="red"
    )



    results = threaded_scan(
        target,
        start,
        end,
        workers=100
    )



    open_ports = []



    for result in results:


        open_ports.append(
            result["port"]
        )


        vulnerability = check_vulnerability(
            result["service"]
        )


        table.add_row(

            str(result["port"]),

            result["service"],

            result["banner"][:40],

            vulnerability["risk"]

        )


        save_scan(

            target,

            result["port"],

            result["service"]

        )



    console.print(
        table
    )



    console.rule(
        "[bold green]Scan Summary"
    )


    console.print(
        f"Ports Scanned: {end - start + 1}"
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