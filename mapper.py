
import os
import sys

EXCLUDE_PREFIXES = {'.git', '.github', '.idea', '__pycache__', '.mypy_cache'}


def should_include(path: str) -> bool:
    parts = path.split(os.sep)
    return not any(part in EXCLUDE_PREFIXES for part in parts)


def main() -> None:
    for line in sys.stdin:
        line = line.rstrip('\n')
        if not line:
            continue
        filename = os.environ.get('mapreduce_map_input_file') or os.environ.get('map_input_file')
        if not filename:
            continue
        rel_path = filename
        for marker in ('repos/', 'workspace/'):
            if marker in rel_path:
                rel_path = rel_path.split(marker, 1)[-1]
        rel_path = rel_path.lstrip('/')
        if rel_path and should_include(rel_path):
            print(f"{rel_path}\t1")


if __name__ == '__main__':
    main()
