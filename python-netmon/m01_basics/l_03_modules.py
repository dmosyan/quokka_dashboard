from tabulate import tabulate
from util.create_util import create_devices

# MAIN PROGRAM
if __name__ == '__main__':

    devices, count = create_devices(num_subnets=5, num_devices=5)
    print("\n", tabulate(devices, headers="keys"))
    print(f"\n{count} devices are generated")
