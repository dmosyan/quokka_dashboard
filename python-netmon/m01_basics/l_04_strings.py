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

