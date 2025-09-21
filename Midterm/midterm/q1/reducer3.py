#!/usr/bin/env python3

import sys
import math

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
            if current_region and anomalies:
                # Calculate standard deviation for the region
                mean = sum(anomalies) / len(anomalies)
                variance = sum((x - mean) ** 2 for x in anomalies) / len(anomalies)
                std_dev = math.sqrt(variance)
                
                # Output: RegionCode\tVolatility(StdDev)
                print(f"{current_region}\t{std_dev}")
            
            current_region = region
            anomalies = [anomaly]
    except Exception as e:
        continue

# Calculate volatility for the last region
if current_region and anomalies:
    mean = sum(anomalies) / len(anomalies)
    variance = sum((x - mean) ** 2 for x in anomalies) / len(anomalies)
    std_dev = math.sqrt(variance)
    print(f"{current_region}\t{std_dev}")
