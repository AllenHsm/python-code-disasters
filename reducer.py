
import sys


def main() -> None:
    current_file = None
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            file_name, count = line.split('\t', 1)
            count = int(count)
        except ValueError:
            continue

        if file_name != current_file:
            if current_file is not None:
                print(f'"{current_file}": {total}')
            current_file = file_name
            total = 0
        total += count

    if current_file is not None:
        print(f'"{current_file}": {total}')


if __name__ == '__main__':
    main()
