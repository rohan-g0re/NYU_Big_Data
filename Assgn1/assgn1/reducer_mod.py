#!/usr/bin/env python3
import sys
from collections import defaultdict

def main(separator='\t'):
    word_counts = defaultdict(int)
    total_words = 0

    for line in sys.stdin:
        word, count = line.strip().split(separator)
        count = int(count)
        word_counts[word] += count
        total_words += count

    # Output word counts
    for word, count in word_counts.items():
        print(f"{word}{separator}{count}")

    # Output total word count with a special key
    print(f"__TOTAL__{separator}{total_words}")

if __name__ == "__main__":
    main()