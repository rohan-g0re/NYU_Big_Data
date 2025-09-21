#!/usr/bin/env python3

import sys

# Pass through the data: RegionCode\tVolatility
for line in sys.stdin:
    print(line.strip())
