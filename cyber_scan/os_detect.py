import subprocess
import re


def detect_os(target):

    try:

        result = subprocess.check_output(
            [
                "ping",
                "-n",
                "1",
                target
            ],
            text=True
        )


        ttl = re.search(
            r"TTL=(\d+)",
            result,
            re.IGNORECASE
        )


        if ttl:

            ttl_value = int(
                ttl.group(1)
            )


            if ttl_value <= 64:

                return "Linux / Unix"


            elif ttl_value <= 128:

                return "Windows"


            elif ttl_value <= 255:

                return "Network Device"


        return "Unknown"


    except:

        return "Unknown"