from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

# create empty list for holding devices
# devices = [] another way of creating list
devices = list()

# for loop to create large number of devices
for index in range(1, 10):
    # create device dictionary
    device = dict()

    # random device name
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )
    # random vendor name
    device["vendor"] = (choice(["cisco", "juniper", "arista"]))
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "nexus"])
        device["version"] = choice(["5.3","7.9","10","12T"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["5", "4.9", "10U", "12K"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["55", "56.77", "57.2", "58L"])
    device["ip"] = "10.0.0." + str(index)

    print(device)
    for key, value in device.items():
        print(f"{key:>8s} : {value}")

    # add device to the list of devices
    devices.append(device)

print("\n____ DEVICES AS LIST OF DICTS ____")
pprint(devices)

# use 'tabulate' to print table of devices
print("\n ____ SORTED DEVICES IN TABULAR FORMAT ____")
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
print(tabulate(sorted_devices, headers="keys"))
#print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))