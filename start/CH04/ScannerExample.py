#!/usr/bin/env python3
# port scanner example
# use 'pip3 install python-nmap' to install modules
# use 'sudo apt -y install nmap' to install nmap
# by Rafaell

# import necessary python modules
import nmap

# identify target address
target_address = "192.168.1.109"

# identify start and stop port for the scan
port_start = 1
port_end = 100

# create the scanner object
scanner = nmap.PortScanner()

print("Scanning {0}".format(target_address))

# loop through each port and scan
for port in range(port_start, port_end + 1):
    result = scanner.scan(target_address, str(port))
    port_status = result['scan'][target_address]['tcp'][port]['state']
    print("\tPort: {0} is {1}".format(port, port_status))