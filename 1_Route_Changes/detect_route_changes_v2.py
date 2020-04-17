#!/usr/bin/env python

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

nr = InitNornir()

result = nr.run(task=netmiko_send_command, command_string="show ip route")

watched_routes = ['192.168.0.13']

# 1. For loop for each device
"""
for device in result:
    print(device)
"""

# 2. nested loop for device result
# why do we need result[device] instead of just device?
"""
for device in result:
    print('Device: ' + device)
    for output in result[device]:
        print(output)
"""

# 3. Detect if a route disappeared from the table
# why do we need str(output) instead of just output
for device in result:
    print(device + ":")
    for output in result[device]:
        for route in watched_routes:
            if route in str(output):
                print('Nice, the route is there.')
            else:
                print('Oh no, time to troubleshoot!')

