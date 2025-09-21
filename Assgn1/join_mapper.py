#!/usr/bin/env python3
import sys

# Debug counter
line_count = 0
id_count = 0
prob_count = 0

for line in sys.stdin:
    line_count += 1
    line = line.strip()
    if not line:
        continue
    
    parts = line.split('\t')
    
    # Debug
    print(f"DEBUG: Processing line {line_count}: {line}", file=sys.stderr)
    print(f"DEBUG: Split into {len(parts)} parts: {parts}", file=sys.stderr)
    
    if len(parts) != 2:
        print(f"DEBUG: Skipping line with {len(parts)} parts", file=sys.stderr)
        continue
    
    try:
        # Try to parse second part as float (probability)
        prob = float(parts[1])
        word = parts[0]
        print(f"{word}\tPROB\t{prob}")
        prob_count += 1
        print(f"DEBUG: Emitted PROB for {word}: {prob}", file=sys.stderr)
    except ValueError:
        try:
            # Try to parse first part as int (ID)
            id_num = int(parts[0])
            word = parts[1]
            print(f"{word}\tID\t{id_num}")
            id_count += 1
            print(f"DEBUG: Emitted ID for {word}: {id_num}", file=sys.stderr)
        except ValueError:
            print(f"DEBUG: Could not parse either part as expected type: {parts}", file=sys.stderr)
            continue

print(f"DEBUG: Processed {line_count} lines total. Emitted {id_count} ID records and {prob_count} PROB records", file=sys.stderr)
