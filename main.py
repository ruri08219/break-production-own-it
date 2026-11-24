#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes the entry line to /output/entry.txt (UTF-8) and verifies the
round-trip: the file content must match the entry exactly.
Standard library only.
"""

import os

ENTRY_LINE = "I ran the cleanup script on prod, wiped the orders table, and now checkout shows a blank page with my name on it."


def validate_entry(text):
    """Check the entry line before anything is written to disk."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be blank"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    return text


def main():
    entry = validate_entry(ENTRY_LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == entry, "round-trip mismatch: file content differs from entry"
    print("entry written: %d characters" % len(written))


if __name__ == "__main__":
    main()
