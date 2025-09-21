#!/usr/bin/env python3

import sys
import os

# Load station-region average temperatures from the distributed cache
station_region_avgs = {}
with open(os.environ['STATION_REGION_AVGS']) as f:
    for line in f:
        key, avg_temp = line.strip().split('\t')
        station_region_avgs[key] = float(avg_temp)

# Process input data and calculate anomalies
for line in sys.stdin:
    try:
        fields = line.strip().split(',')
        if len(fields) == 6:
            station_id = fields[0]
            region_code = fields[2]
            temperature = float(fields[4])
            
            key = f"{station_id}_{region_code}"
            if key in station_region_avgs:
                avg_temp = station_region_avgs[key]
                anomaly = temperature - avg_temp
                
                # Emit: RegionCode\tAnomaly
                print(f"{region_code}\t{anomaly}")
    except Exception as e:
        continue
