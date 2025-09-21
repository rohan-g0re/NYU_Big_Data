#!/usr/bin/env python3
import sys

# Load the total word count from total.txt
with open("total.txt", "r") as f:
    total_words = int(f.readline().strip())

for line in sys.stdin:
    word, count = line.strip().split('\t')
    probability = int(count) / total_words
    print(f"{word}\t{probability}")