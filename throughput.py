# Task 6: reading from a file
# Write a Python program that reads throughput values from a file and identifies the minimum
# throughput.
# NOTE: Create a text file named throughput_values.txt with the following lines:
# 100 Mbps
# 2000 Kbps
# 1 Gbps
# 200 Mbps
# Hint: Consider the units conversion: 1Kbps = 1000bps, 1Mbps = 1000Kbps, 1Gbps = 1000Mbps
# Output: The minimum throughput value is: 2000 Kbps

def minimum_throughput(file):
    minthrput_kbps = float('inf')
    minthrput_str = None

    with open(file, "r") as file:
        for line in file:
            value, unit = line.strip().split()
            value = float(value)

            if unit.lower() == 'kbps':
                thrput_kbps = value
            elif unit.lower() == 'mbps':
                thrput_kbps = value * 1000
            elif unit.lower() == 'gbps':
                thrput_kbps = value * 1000 * 1000
            elif unit.lower() == 'tbps':
                thrput_kbps = value * 1000 * 1000 * 1000
            elif unit.lower == 'bps':
                thrput_kbps = value / 1000

            if thrput_kbps < minthrput_kbps:
                minthrput_kbps = thrput_kbps
                minthrput_str = line.strip()

    print(f"The minimum throughput value is:",minthrput_str)

minimum_throughput("throughput_values.txt")

