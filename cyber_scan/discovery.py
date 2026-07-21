import socket
from concurrent.futures import ThreadPoolExecutor


def check_host(ip):

    try:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.3)

        result = sock.connect_ex(
            (ip, 80)
        )

        sock.close()

        if result == 0:

            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown"

            return {
                "ip": ip,
                "hostname": hostname
            }

    except:
        pass

    return None


def discover_hosts(network):

    base = network.rsplit(".", 1)[0]

    hosts = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        results = executor.map(
            check_host,
            [f"{base}.{i}" for i in range(1, 255)]
        )

        for result in results:

            if result:

                hosts.append(result)

    return hosts