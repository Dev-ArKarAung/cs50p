import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # 1. Check format: must be exactly 4 groups of digits separated by dots
    # Using fullmatch ensures no extra characters or missing groups
    if not re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip):
        return False

    # 2. Extract the groups and convert to integers
    octets = re.findall(r"\d+", ip)

    # 3. Validate each octet is between 0 and 255
    for octet in octets:
        if not (0 <= int(octet) <= 255):
            return False
        if octet.startswith('0') and len(octet) > 1:
            return False
        
    return True


if __name__ == "__main__":
    main()