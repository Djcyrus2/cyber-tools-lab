import socket


def grab_banner(target, port):

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(2)


        sock.connect(
            (target, port)
        )


        banner = sock.recv(
            1024
        ).decode(
            errors="ignore"
        )


        sock.close()


        if banner:

            return banner.strip()


    except:

        pass


    return "No banner detected"