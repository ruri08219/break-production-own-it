#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes the entry line to /output/entry.txt (UTF-8) and verifies the
round-trip: the file content must match the entry exactly.
Standard library only.
"""

import os

ENTRY = "I ran the cleanup script on prod, wiped the orders table, and now checkout shows a blank page with my name on it."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch: file content differs from entry"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert "\n" not in written, "entry must be a single line"
    print("entry written: %d characters" % len(written))


if __name__ == "__main__":
    main()
