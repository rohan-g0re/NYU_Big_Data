#!/usr/bin/env python3

import sys

current_region = None
anomalies = []

# Input: RegionCode\tAnomaly
for line in sys.stdin:
    try:
        region, anomaly = line.strip().split('\t')
        anomaly = float(anomaly)
        
        if current_region == region:
            anomalies.append(anomaly)
        else:
            if current_region:
                # Output all anomalies for the region
                for a in anomalies:
                    print(f"{current_region}\t{a}")
            
            current_region = region
            anomalies = [anomaly]
    except Exception as e:
        continue

# Output anomalies for the last region
if current_region:
    for a in anomalies:
        print(f"{current_region}\t{a}")
