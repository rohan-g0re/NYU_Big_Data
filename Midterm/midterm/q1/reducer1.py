#!/usr/bin/env python3

import sys

current_key = None
temp_sum = 0
temp_count = 0

# Input: StationID_RegionCode\tTemperature
for line in sys.stdin:
    try:
        key, temperature = line.strip().split('\t')
        temperature = float(temperature)
        
        if current_key == key:
            temp_sum += temperature
            temp_count += 1
        else:
            if current_key:
                # Output: StationID_RegionCode\tAverageTemperature
                avg_temp = temp_sum / temp_count
                print(f"{current_key}\t{avg_temp}")
            
            current_key = key
            temp_sum = temperature
            temp_count = 1
    except Exception as e:
        continue

# Output the last key
if current_key and temp_count > 0:
    avg_temp = temp_sum / temp_count
    print(f"{current_key}\t{avg_temp}")
