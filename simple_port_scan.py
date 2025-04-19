import socket

# Ask user for the target
target = input("Enter the target IP or hostname: ")

# Ask user for custom ports
ports_input = input("Enter the ports you want to scan (separated by commas, or press Enter to use default ports): ")

# If user enters something, split it into a list
if ports_input:
    ports = [int(port.strip()) for port in ports_input.split(',')]
else:
    # Default ports if nothing entered
    ports = [21, 22, 23, 25, 53, 80, 443, 3389]

print(f"\nScanning {target}...\n")

# Loop through ports
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # 1 second timeout
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")
    sock.close()