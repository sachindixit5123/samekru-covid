#!/usr/bin/env python
"""combiner.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.replace("::", ":0:")
    line = line.replace("N/A", "0")
    print(line)