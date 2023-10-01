import socket

# Function to check if a port is open
def is_port_open(ip, port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout to avoid hanging on closed ports
            s.settimeout(1)
            # Attempt to connect to the IP and port
            s.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

# Define the range of ports to scan
start_port = 1
end_port = 1024  # You can adjust this range as needed

# Define the target IP address or hostname
target = "127.0.0.1"  # Replace with the target IP or hostname

# Perform the port scan and print results
print(f"Scanning ports {start_port} to {end_port} on {target}...\n")
for port in range(start_port, end_port + 1):
    if is_port_open(target, port):
        print(f"Port {port} is open.")
