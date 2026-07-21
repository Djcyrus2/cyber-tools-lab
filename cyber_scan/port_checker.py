import socket

from .banner import grab_banner
from .services import SERVICES


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