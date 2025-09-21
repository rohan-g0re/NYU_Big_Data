#!/usr/bin/env python3
import sys

"""
Mapper reads input line by line, splits word and count,
and outputs it in key-value format with count as key 
for sorting later.
"""

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 2:
        word, count = parts[0], int(parts[1])
        print(f"{count}\t{word}")  # Swap word and count for sorting by count
