import argparse
import sys

# Task 5: Port address check using argparse
# Write a Python program that utilises argparse to take two optional arguments (-p and -s). Check if
# the server is specified with (-s) and ensure that the given port number is within the range (1025,
# 65535).
# Example:
# Run: python3 portcheck.py –s -p 1000
# → Output: Invalid port. The port must be within the range 1025 and 65536
# Run: python3 portcheck.py -p 1075
# → Output: The server is not available
# Run: python3 portcheck.py -s -p 1075
# → Output: Valid port

parser = argparse.ArgumentParser(description="Check port validity")
parser.add_argument('-s', '--server', action='store_true', help='Specify server address')
parser.add_argument('-p', '--port', help='Specify port number', type=int)
args = parser.parse_args()


def checkport(port):
    return 1025 <= port <= 65535

def main():
    if args.port:
        if args.server:
            if checkport(args.port):
                print("Valid port")
            else:
                print("Invalid port. The port must be within the range 1025 and 65536")
        else:
            if not args.server and args.port:
                print("The server is not available")
    elif args.server and not args.port:
        print("Invalid port. The port must be within the range 1025 and 65536")

if __name__ == "__main__":
  main()