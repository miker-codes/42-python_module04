#!/usr/bin/env python3


import sys


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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
    print(content.rstrip("\n"))
    print()
    print("---")
    print(f"File '{filename}' closed.")

    # New code ex1
    print()
    print("Transform data:")
    print("---")
    print()

    lines = content.rstrip("\n").split("\n")
    new_lines = [line + '#' for line in lines]
    new_content = '\n'.join(new_lines) + '\n'

    print(new_content.rstrip("\n"))
    print()
    print("---")
    new_file_name = input("Enter new file name (or empty): ")
    if len(new_file_name) == 0:
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file_name}'")
    try:
        new_file = open(new_file_name, "w")
    except OSError as e:
        print(f"Error opening file '{new_file_name}': {e}")
        return
    new_file.write(new_content)
    new_file.close()
    print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
