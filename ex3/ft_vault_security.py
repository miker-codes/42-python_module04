#!/usr/bin/env python3


def secure_archive(filename: str,
                   action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "write":
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        with open(filename, "r") as f:
            return (True, f.read())
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file", "read", "")
    print(f"{result}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/shadow", "read", "")
    print(f"{result}\n")
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "read", "")
    print(f"{result}\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    result_write = secure_archive("copy.txt", "write", result[1])
    print(f"{result_write}\n")


if __name__ == "__main__":
    main()
