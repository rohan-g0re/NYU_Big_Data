#!/usr/bin/env python3
import sys
from collections import defaultdict

word_counts = defaultdict(int)

# Read input from mapper
for line in sys.stdin:
    word, count = line.strip().split("\t")
    word_counts[word] += int(count)

# Output word counts
for word, count in word_counts.items():
    print(f"{word}\t{count}")
