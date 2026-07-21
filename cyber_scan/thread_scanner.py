from concurrent.futures import ThreadPoolExecutor

from .port_checker import scan_port


def threaded_scan(target, start, end, workers=50):

    open_ports = []


    with ThreadPoolExecutor(
        max_workers=workers
    ) as executor:


        results = executor.map(
            lambda port: scan_port(
                target,
                port
            ),

            range(
                start,
                end + 1
            )
        )


        for result in results:

            if result:

                open_ports.append(
                    result
                )


    return open_ports