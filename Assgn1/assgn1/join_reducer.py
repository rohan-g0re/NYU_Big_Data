#!/usr/bin/env python3
import sys
import itertools

def read_mapper_output(file):
    for line in file:
        yield line.strip()

# Initialize counters outside the function
line_count = 0
group_count = 0
output_count = 0

# Input comes from STDIN
data = read_mapper_output(sys.stdin)
# Convert data to a list and sort it to ensure proper grouping
data_list = sorted(data, key=lambda x: x.split('\t')[0])

for word, group in itertools.groupby(data_list, lambda x: x.split('\t')[0]):
    group_count += 1
    print(f"DEBUG: Processing group for word: {word}", file=sys.stderr)
    
    id_val = None
    prob_val = None
    
    for item in group:
        line_count += 1  # Move this inside the loop where we process each line
        parts = item.split('\t')
        if len(parts) != 3:
            print(f"DEBUG: Skipping malformed line: {item}", file=sys.stderr)
            continue
            
        if parts[1] == "ID":
            id_val = parts[2]
            print(f"DEBUG: Found ID {id_val} for {word}", file=sys.stderr)
        elif parts[1] == "PROB":
            prob_val = parts[2]
            print(f"DEBUG: Found PROB {prob_val} for {word}", file=sys.stderr)
    
    if id_val is not None and prob_val is not None:
        print(f"{id_val}\t{word}\t{prob_val}")
        output_count += 1
        print(f"DEBUG: Emitted output for {word}: {id_val}\t{word}\t{prob_val}", file=sys.stderr)
    else:
        print(f"DEBUG: Missing data for {word}. ID: {id_val}, PROB: {prob_val}", file=sys.stderr)

print(f"DEBUG: Processed {line_count} lines in {group_count} groups. Emitted {output_count} joined records", file=sys.stderr)
