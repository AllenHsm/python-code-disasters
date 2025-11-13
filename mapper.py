#!/usr/bin/env python3
import os
import sys

EXCLUDE_PREFIXES = {'.git', '.github', '.idea', '__pycache__', '.mypy_cache'}

def should_include(path: str) -> bool:
    parts = path.split(os.sep)
    return not any(part in EXCLUDE_PREFIXES for part in parts)

def main() -> None:
    filename = os.environ.get('mapreduce_map_input_file') or os.environ.get('map_input_file') or "UNKNOWN_FILE"
    for line in sys.stdin:
        line = line.rstrip('\n')
        if should_include(filename):
            print(f"{filename}\t1")

if __name__ == '__main__':
    main()
