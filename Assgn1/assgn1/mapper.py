#!/usr/bin/env python3
import re
import sys

# def normalize(word):
#     return re.sub(r'[^a-z0-9]', ' ', word.lower()).split()

def normalize(text):
    """Normalizes text: lowercase, removes non-alphanumeric, splits into words."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)  # Keep spaces
    return text.split()

for line in sys.stdin:
    words = normalize(line)
    for word in words:
        print(f"{word}\t1")
