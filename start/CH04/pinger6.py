#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By Rafaell

# import necessary Python modules
import platform
import os
from datetime import datetime

def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    f = open("pinger.log", "a")
    f.write(message)
    f.close()

def ping_host(ip):
    # determine the current os
    current_os = platform.system().lower()

    if current_os == "windows":
        # build our ping command for windows
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        # build our ping command for other oss
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    # execute command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code

def import_addresses():
    # create empty list object
    lines = []

    # open file and read line-by-line
    f = open("ips.txt", "r")
    for line in f:
        # use strip() to remove spaces and carriage returns
        line = line.strip()
        # add the line to the lines list object
        lines.append(line)

    # return the list object to the main body
    return lines

# read IPs from file
write_log("Reading IPs from ips.txt")
ip_addresses = import_addresses()
write_log("Imported {0} IPs".format(len(ip_addresses)))

for ip in ip_addresses:
    # call ping_host function and capture the return value
    exit_code = ping_host(ip)

    # print results to console only if successful
    if exit_code == 0:
        write_log("{0} is online".format(ip))
        print("{0} is online".format(ip))
    else:
        write_log("{0} is offline".format(ip))