# 42 - Python Module04

Project done for the 42 Malaga curriculum by **mruiz-ra**.

## About

This is **Data Archivist**, the fifth Python project of the 42 core curriculum. It covers file operations, from a plain read of a file named on the command line up to a reusable safe access function built on a context manager. Each exercise extends the previous one, so the same script grows step by step until exercise 3 starts fresh with the `with` statement.

## Structure

```
.
├── ex0/
│   └── ft_ancient_text.py
├── ex1/
│   └── ft_archive_creation.py
├── ex2/
│   └── ft_stream_management.py
└── ex3/
    └── ft_vault_security.py
```

## Exercises

| # | File | Concept | Description |
|---|------|---------|-------------|
| 00 | `ft_ancient_text.py` | `open()`, `read()`, `close()` | Takes a file name from the command line and prints its contents the way `cat` would, with a header and a footer. The file is opened inside a `try`, and a single `except OSError` covers both `FileNotFoundError` and `PermissionError` since they share that base class, so a missing or unreadable file is reported instead of crashing the program. The header and the `Accessing file` line are printed before the open attempt so they appear on the failure paths too, and an early `return` stops execution before any line that assumes the open succeeded. The handle is closed explicitly with `close()`. |
| 01 | `ft_archive_creation.py` | Writing files | Extends ex0. After displaying the file, the content is split into lines with `str.split()`, a `#` is appended to each one with a list comprehension, and the result is rebuilt with `str.join()`. Calling `str.rstrip()` before the split drops the trailing newline so the last element is a real line and not an empty string, which would otherwise produce a stray `#` on its own line, and the newline is added back before writing so the saved file keeps its final line ending. The user is then asked for a destination name, an empty answer skips saving, and a name opens the file in `"w"` mode, which creates it or replaces it if it already exists. The write is guarded by its own `try/except`. |
| 02 | `ft_stream_management.py` | Standard streams | Extends ex1. Every error message coming from an exception is redirected to the error stream with `print(..., file=sys.stderr)` and a `[STDERR]` prefix, which lets the caller separate the two channels (`2>/dev/null` hides the errors, `1>/dev/null` keeps only them). The `input()` built-in is replaced by `sys.stdin.readline()`, which means the prompt has to be printed manually with `end=""`, followed by `sys.stdout.flush()` because stdout is buffered and the prompt would otherwise appear after the user has already typed, and the trailing newline kept by `readline()` has to be stripped so the empty answer check still works. |
| 03 | `ft_vault_security.py` | `with` statement | A fresh script built around `secure_archive()`, a single safe entry point for reading and writing. It takes a mandatory file name plus two optional parameters with default values, the action to perform and the content to write, and always returns a `tuple[bool, str]`: the file contents or a confirmation message on success, the text of the caught `OSError` on failure. The file work happens inside a `with` block, so the handle is closed automatically even when the function returns from inside the block or an exception propagates, which is what the explicit `close()` calls of the previous exercises were doing by hand. `main()` exercises the four cases: a nonexistent file, an inaccessible one, a regular read, and writing the content just read into a new file. |

## Testing

Exercises 0 to 2 take the file to process as a command line argument:

```bash
python3 ex0/ft_ancient_text.py ancient_fragment.txt
python3 ex1/ft_archive_creation.py ancient_fragment.txt
python3 ex2/ft_stream_management.py ancient_fragment.txt
```

Exercise 3 runs on its own:

```bash
python3 ex3/ft_vault_security.py
```

The stream separation of ex2 can be checked with a redirection:

```bash
python3 ex2/ft_stream_management.py nonexistent 2>/dev/null
python3 ex2/ft_stream_management.py nonexistent 1>/dev/null
```

## Style

Every file respects **flake8** (PEP8) and **mypy** for type hints:

```bash
flake8 exX/file.py
mypy exX/file.py
```

> Note: "La Norme" from the C projects does not apply here, this is a pure Python project with its own rules defined in the subject.

As required by the subject, the `with` statement is not used before exercise 3: exercises 0 to 2 open and close their files manually.

## Key concepts covered

- `open()` in read and write mode, `read()`, `write()`, `close()`
- The file object returned by `open()` and its `typing.IO` type
- `OSError` as the shared base class of `FileNotFoundError` and `PermissionError`
- Early `return` inside an `except` block to skip code that assumes success
- Standard streams: `sys.stdin`, `sys.stdout`, `sys.stderr`, and why only the first two are buffered
- Reading input without `input()`, with `readline()` and a manual prompt plus `flush()`
- Trailing newline handling when splitting and rejoining text
- Optional parameters with default values, and returning a status tuple instead of raising
- The `with` statement as a context manager that guarantees the file is closed