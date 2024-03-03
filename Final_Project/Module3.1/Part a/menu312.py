import os

# Print the menu
print("COVID-19 comparison Menu:")
print("a. Total cases")
print("b. Active cases")
print("c. Total deaths")
print("d. Total recovered")
print("e. Total tests")
print("f. Death/million")
print("g. Tests/million")
print("h. New cases")
print("i. New deaths")
print("j. New recovered")

while True:
    # Take user input for choice and country
    choice = input("Choose from [a-j]: ").strip()
    if choice not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
        print("Invalid choice! Please choose from [a-j].")
        continue

    country = input("Enter Country name: ").strip()
    # Run the pipeline with user's choice and country
    os.system(f"python3 mapper312.py {choice} {country} | python3 combiner312.py | python3 reducer312.py > percentagechange.txt")
    break
