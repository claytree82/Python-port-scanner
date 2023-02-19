import subprocess
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Blank screen
subprocess.call('clear', shell=True)

# Ask for ip
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a banner
print("_" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("_" * 60)

# Check date and time the scan was started
t1 = datetime.now()

# Define the scanning function
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
        print("Port {}: open".format(port))
    sock.close()

# Use a thread pool to scan multiple ports at once
with ThreadPoolExecutor(max_workers=50) as executor:
    for port in range(1, 50):
        executor.submit(scan_port, port)

# Check time again
t2 = datetime.now()

# Calculate difference in time to know how long the scan took
total_time = t2 - t1

# Print the total time
print("Scanning Completed in: ", total_time)
