from pprint import pprint

# Dictionary
device = {
    "name": "sbx-n9kv",
    "vendor": "cisco",
    "model": "Nexus9000",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.0.0.1"
}

# simple print
print("\n___ SIMPLE PRINT ___")
print("device:", device)
print("device name:", device["name"])

# pretty print
print("\n___ PRETTY PRINT ___")
pprint(device)

# for loop, nice formatted print
print("\n___ FOR LOOP, USING F-STRING")
# make dictionary iterable by items function
for key, value in device.items():
    print(f"{key:>8s} : {value}")

