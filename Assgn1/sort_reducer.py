#!/usr/bin/env python3
import sys

"""
Reducer reads sorted input from the Mapper (sorted by count in descending order)
and prints words with an index.
"""

word_list = []
for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 2:
        count, word = int(parts[0]), parts[1]
        word_list.append((count, word))

# Sort by count in descending order
word_list.sort(reverse=True, key=lambda x: x[0])

# Print indexed output
for i, (_, word) in enumerate(word_list, start=1):
    print(f"{i}\t{word}")
