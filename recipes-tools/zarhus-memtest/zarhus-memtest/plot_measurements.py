#!/usr/bin/env python3

import csv
import sys
import matplotlib.pyplot as plt

from datetime import datetime


def date_to_relative(timestamps: list[str]) -> list[int]:
    dates = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in timestamps]
    return [int((date - dates[0]).total_seconds()) for date in dates]


def get_axes(filename: str):
    timestamps = []
    used_mem = []
    used_swap = []

    with open(f"{filename}", 'r') as csv_file:
        lines = csv.reader(csv_file)
        # Skip header
        next(lines, None)
        for row in lines:
            timestamps.append(row[0])
            used_mem.append(row[1])
            used_swap.append(row[2])
    return date_to_relative(timestamps), used_mem, used_swap


if len(sys.argv) == 1:
    print("Usage: python3 plot_measurement.py measurements_directory")
    exit(1)

timestamps, used_mem, used_swap = get_axes(sys.argv[1])
plt.figure(figsize=(8, 8))
plt.plot(timestamps, used_mem, label="Used RAM")
plt.plot(timestamps, used_swap, label="Used Swap memory")
plt.legend()
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Memory [Ki]")
plt.title("Memory usage")
plt.savefig("mem-usage.png")
plt.show()
