#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
- Total file size: File size: <total size> (the sum of all previous)
- Number of lines by status code
(status codes: 200, 301, 400, 401, 403, 404, 405, 500)
"""


def print_stats(total_size, status_count):
    """
    Prints metrics including total file size and number
    of lines by status code.

    Args:
        total_size (int): Total file size.
        status_count (dict): Dictionary containing counts of
            lines by status code.
    """

    print(f"File size: {total_size}")

    for code in sorted(status_count.keys()):
        print(f"{code}: {status_count[code]}")


if __name__ == "__main__":
    import sys

    total_size = 0
    status_count = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for i, line in enumerate(sys.stdin, 1):
            data = line.split()

            if len(data) >= 2:
                try:
                    status_code = int(data[-2])
                    file_size = int(data[-1])
                    total_size += file_size

                    if str(status_code) in valid_codes:
                        status_count[status_code] = \
                            status_count.get(status_code, 0) + 1

                    if i % 10 == 0:
                        print_stats(total_size, status_count)

                except ValueError:
                    pass

    except KeyboardInterrupt:
        print_stats(total_size, status_count)
        raise
