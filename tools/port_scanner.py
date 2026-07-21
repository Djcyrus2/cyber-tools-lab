 import socket
import argparse
import json
import html
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from logger import write_log


SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}


def get_banner(target, port):

    try:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(2)

        sock.connect((target, port))

        banner = sock.recv(1024).decode(
            errors="ignore"
        )

        sock.close()

        return banner.strip()

    except:
        return "No banner"


def scan_port(target, port):

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.5)

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
                "banner": get_banner(
                    target,
                    port
                )
            }


    except:
        pass


    return None



def create_html(data):

    page = """
    <html>
    <head>
    <title>Cyber Tools Lab Report</title>
    </head>
    <body>
    <h1>Scan Report</h1>
    """

    page += f"<h3>Target: {data['target']}</h3>"


    for item in data["ports"]:

        page += f"""
        <p>
        Port: {item['port']}<br>
        Service: {html.escape(item['service'])}<br>
        Banner: {html.escape(item['banner'])}
        </p>
        """


    page += "</body></html>"


    with open(
        "tools/reports/report.html",
        "w"
    ) as file:

        file.write(page)



def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--target",
        required=True
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-100"
    )


    args = parser.parse_args()


    start,end = args.ports.split("-")


    results=[]


    write_log(
        f"Started scan {args.target}"
    )


    with ThreadPoolExecutor(
        max_workers=50
    ) as executor:


        scans = executor.map(
            lambda p: scan_port(
                args.target,
                p
            ),
            range(
                int(start),
                int(end)+1
            )
        )


        for result in scans:

            if result:

                print(
                    "[OPEN]",
                    result["port"]
                )

                results.append(result)



    data={

        "target":args.target,

        "time":str(datetime.now()),

        "ports":results

    }


    with open(
        "tools/reports/report.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


    create_html(data)


    write_log(
        "Scan completed"
    )


    print(
        "Reports created"
    )



if __name__=="__main__":

    main()