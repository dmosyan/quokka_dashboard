from random import choice
import string


def create_devices(num_devices=1, num_subnets=1):
    # create list of devices
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("ERROR: Too many devices or subnets provided")
        return created_devices

    for subnet_index in range(1, num_subnets+1):
        for device_index in range(1, num_devices+1):
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
               device["version"] = choice(["5.3", "7.9", "10", "12T"])
            elif device["vendor"] == "juniper":
                device["os"] = "junos"
                device["version"] = choice(["5", "4.9", "10U", "12K"])
            elif device["vendor"] == "arista":
                device["os"] = "eos"
                device["version"] = choice(["55", "56.77", "57.2", "58L"])
            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

            for key, value in device.items():
                print(f"{key:>8s} : {value}")

            # add device to the list of devices
            created_devices.append(device)
    sum_devices = num_devices * num_subnets
    return created_devices, sum_devices
