import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if match:
        for i in range(1, 5):
            segment = match.group(i)
            if len(segment) > 1 and segment[0] == "0":  # zéro de tête interdit
                return False
            if not 0 <= int(segment) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
