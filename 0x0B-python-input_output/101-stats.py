#!/usr/bin/python3
import sys


def print_data():
    print(f"File size: {total_size}")
    for code in codes:
        if codes_counts[code]:
            print(f"{code}: {codes_counts[code]}")


total_size = 0
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
codes_counts = dict()
for code in codes:
    codes_counts[code] = 0

try:
    line_num = 1
    for line in sys.stdin:
        try:
            if line_num == 11:
                line_num = 1
                print_data()
            info = line.split()
            total_size += int(info[-1])
            codes_counts[info[-2]] += 1
            line_num += 1
        except Exception:
            pass
    else:
        print_data()
except KeyboardInterrupt as e:
    print_data()
    raise e
