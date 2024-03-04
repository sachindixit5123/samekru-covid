#!/usr/bin/env python
"""reducer.py"""

import sys

# Define initial variables
Total_Cases = Active_Cases = Total_Deaths = Total_Recovered = Total_Tests = Deaths_M = Tests_M = New_Cases = New_Deaths = New_Recovered = 0

# input comes from STDIN (standard input)
flag = 0
for line in sys.stdin:
    line = line.strip()
    if flag == 0:
        choice = line
        flag += 1
        continue
    if flag == 1:
        country = line
        flag += 1
        continue
    if 'World' in line:
        parts = line.split(':')[:-1]
        # Assign values to variables
        Total_Cases, Active_Cases, Total_Deaths, Total_Recovered, Total_Tests, Death_Per_Million, Tests_Per_Million, New_Cases, New_Deaths, New_Recovered = map(float, parts[1:])
        # print(Total_Cases)
        continue
    if country in line:
        parts = line.split(':')[:-1]
        # Assign values to variables
        Total_Cases2, Active_Cases2, Total_Deaths2, Total_Recovered2, Total_Tests2, Death_Per_Million2, Tests_Per_Million2, New_Cases2, New_Deaths2, New_Recovered2 = map(float, parts[1:])
        # print(Total_Cases2)
        continue
if choice == 'a':
    if Total_Cases != 0:
        print(((Total_Cases2 / Total_Cases) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'b':
    if Active_Cases != 0:
        print(((Active_Cases2 / Active_Cases) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'c':
    if Total_Deaths != 0:
        print(((Total_Deaths2 / Total_Deaths) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'd':
    if Total_Recovered != 0:
        print(((Total_Recovered2 / Total_Recovered) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'e':
    if Total_Tests != 0:
        print(((Total_Tests2 / Total_Tests) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'f':
    if Death_Per_Million != 0:
        print(((Death_Per_Million2 / Death_Per_Million) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'g':
    if Tests_Per_Million != 0:
        print(((Tests_Per_Million2 / Tests_Per_Million) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'h':
    if New_Cases != 0:
        print(((New_Cases2 / New_Cases) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'i':
    if New_Deaths != 0:
        print(((New_Deaths2 / New_Deaths) * 100), '%')
    else:
        print("Cannot divide by zero")
elif choice == 'j':
    if New_Recovered != 0:
        print(((New_Recovered2 / New_Recovered) * 100), '%')
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
