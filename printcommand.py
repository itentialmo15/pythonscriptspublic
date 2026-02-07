#!/usr/bin/env python
import sys
import argparse
def main():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument('--command', required=True, help="Command to run")
    args = parser.parse_args()
    output =args.command
    print(output)

if __name__ == "__main__":
    main()
