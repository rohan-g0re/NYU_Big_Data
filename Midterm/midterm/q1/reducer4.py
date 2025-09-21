#!/usr/bin/env python3

import sys

# Store all region volatilities
region_volatilities = []

# Input: RegionCode\tVolatility
for line in sys.stdin:
    try:
        region, volatility = line.strip().split('\t')
        volatility = float(volatility)
        region_volatilities.append((region, volatility))
    except Exception as e:
        continue

# Sort by volatility in descending order and take top 3
top_regions = sorted(region_volatilities, key=lambda x: x[1], reverse=True)[:3]

# Output the top 3 regions with highest volatility
for i, (region, volatility) in enumerate(top_regions, 1):
    print(f"Rank {i}: Region {region} - Volatility: {volatility}")
