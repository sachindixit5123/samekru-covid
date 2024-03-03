#!/usr/bin/env python
"""mapper.py"""

import sys

for line in range(1,3):
    line = sys.argv[line].strip()
    print(line)

with open('countries.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.replace(',', '').replace('+', '')
        Country, Total_Cases, New_Cases, Total_Deaths, New_Deaths, Total_Recovered, New_Recovered, Active_Cases, Deaths_M, Total_Tests, Tests_M = line.split(' ')
        print(f'{Country}:{Total_Cases}:{Active_Cases}:{Total_Deaths}:{Total_Recovered}:{Total_Tests}:{Deaths_M}:{Tests_M}:{New_Cases}:{New_Deaths}:{New_Recovered}:')
