import socket
from datetime import datetime

print("=== Cyber Tools Lab Port Scanner ===")

target = input("Enter target IP address: ")

ports = [21, 22, 23, 53, 80, 443, 8080]

print("\nScanning:", target)
print("Started:", datetime.now())

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        sock.close()

    except socket.error:
        print("Connection error")

print("\nScan complete.")

 notepad tools/port_scanner.py
