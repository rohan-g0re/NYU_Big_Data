#!/usr/bin/env python3

import sys

# Input format: StationID,CountryCode,RegionCode,Timestamp,Temperature,Humidity
for line in sys.stdin:
    try:
        fields = line.strip().split(',')
        if len(fields) == 6:
            station_id = fields[0]
            region_code = fields[2]
            temperature = float(fields[4])
            
            # Emit key-value pairs: (StationID_RegionCode, Temperature)
            key = f"{station_id}_{region_code}"
            print(f"{key}\t{temperature}")
    except Exception as e:
        # Skip malformed lines
        continue
