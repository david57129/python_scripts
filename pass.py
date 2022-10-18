import netmiko
from netmiko import ConnectHandler
from getpass import getpass
import re


cisco1 = {
    "device_type": "cisco_ios",
    "host": "R1.ratkay.com",
    "username": "Saas",
    "password": getpass(),
}

# Show command that we execute
command = "show interface summary"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned

print()
print(output)
print()
