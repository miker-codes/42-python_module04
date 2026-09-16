#!/usr/bin/env python3


import sys


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    content = file.read()
    file.close()
    print("---")
    print()
    print(content)
    print()
    print("---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
