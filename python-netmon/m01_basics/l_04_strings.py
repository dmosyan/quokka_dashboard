from pprint import pprint

device1_str = " r3-L-n7, cisco, catalyst 2960, ios "

#split
print("STRING SPLIT, SPLIT, REPLACE")
device1 = device1_str.split(",")
print(device1)

#strip
device1 = device1_str.strip().split(",")
print(device1)

#remove blanks
device1 = device1_str.replace(" ", "").split(",")
print(device1_str)

#remove blanks, change comma to colon
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print(device1_str_colon)

#loop with strip and split
device1_list = list()
for device in device1_str.split(","):
    device1_list.append(device.strip())
print(device1_list)

#single line strip and split (LIST COMPREHENSION)
device1_line = [item.strip() for item in device1_str.split(",")]
print(device1_line)

#ignoring case
print("\n\nIGNORING CASE")
model = "CSR100V"
if model == "csr100v":
    print("STRING MATCH")
else:
    print("DIDN'T MATCH")

if model.lower() == "csr100V".lower():
    print("STRING MATCH")
else:
    print("DIDN'T MATCH")

#finding substring
version = "Virtual XE Software 1085 (x86 arch), Version 1.3.5, Operating System Windows Server 2019"
expected_version = "Version 1.3.5"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} at location {index}")
else:
    print(f"not found {expected_version}")

#separating string components
version_info = [part.strip() for part in version.split(",")]
for vi_parts in version_info:
    print(vi_parts)

#enumerate function will return 2 values. Index and Item from the list
version_info2 = version.split(",")
for part_no, vi_parts in enumerate(version_info2):
    print(f"Index num is: {part_no} | {vi_parts.strip()}")