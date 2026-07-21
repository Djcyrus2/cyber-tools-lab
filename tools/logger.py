from datetime import datetime


def write_log(message):

    with open("tools/scanner.log", "a") as file:
        file.write(
            f"[{datetime.now()}] {message}\n"
        )