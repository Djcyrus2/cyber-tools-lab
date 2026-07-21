from rich.console import Console


console = Console()



def show_web_report(result):

    console.rule(
        "[bold cyan]Web Scan Report"
    )


    console.print(
        "URL:",
        result["url"]
    )


    console.print(
        "Status:",
        result["status"]
    )


    console.print(
        "Server:",
        result["server"]
    )


    if result["headers"]:

        console.print(
            "Security Headers:"
        )

        for header in result["headers"]:

            console.print(
                "✓",
                header
            )

    else:

        console.print(
            "No security headers detected"
        )