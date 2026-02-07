#!/usr/bin/env python
import sys

if __name__ == "__main__":
    print("Script name:", sys.argv[0])
    print("Arguments:", sys.argv[1:])

    if len(sys.argv) < 2:
        print("Usage: python script.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Hello, {name}")
