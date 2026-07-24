from datetime import datetime

from rich.console import Console
from rich.table import Table

from .database import save_scan, create_database
from .exporter import export_csv
from .thread_scanner import threaded_scan
from .os_detect import detect_os
from .vulnerability import check_vulnerability
from .report_generator import generate_html_report


VERSION = "20.0.0"

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




def start_scan(target, port_range, workers=100):

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


    console.print(
        f"[yellow]Threads:[/yellow] {workers}"
    )



    os_info = detect_os(
        target
    )


    console.print(
        f"[green]OS Guess:[/green] {os_info}"
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
        "Risk",
        style="red"
    )


    table.add_column(
        "Banner",
        style="green"
    )



    results = threaded_scan(

        target,

        start,

        end,

        workers=workers

    )



    open_ports = []

    scan_results = []



    for result in results:


        open_ports.append(
            result["port"]
        )


        vulnerability = check_vulnerability(
            result["service"]
        )



        scan_results.append({

            "port": result["port"],

            "service": result["service"],

            "risk": vulnerability["risk"],

            "banner": result["banner"]

        })



        table.add_row(

            str(result["port"]),

            result["service"],

            vulnerability["risk"],

            result["banner"][:50]

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



    html_report = generate_html_report(

        target,

        scan_results

    )


    console.print(

        f"[green]HTML Report:[/green] {html_report}"

    )



    console.print(

        "\n[bold green]Scan Complete[/bold green]"

    )