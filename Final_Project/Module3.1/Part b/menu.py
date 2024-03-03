import sys
import os
from datetime import datetime

def main():
    
    country_name = input("Enter country name: ")
    start_date = input("Enter start date (dd-mm-yyyy): ")
    end_date = input("Enter end date (dd-mm-yyyy): ")

    # Convert date strings to datetime objects
    try:
        start_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
    
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        sys.exit(1)
    
    # Display menu for query selection
    print("\nSelect Query:")
    print("a. Change in active cases in %")
    print("b. Change in daily death in %")
    print("c. Change in new recovered in %")
    print("d. Change in new cases in %")
    print("-1 for exit")
    query = input("Enter query option (a, b, c, d): ")
    
    if(query not in ['a','b', 'c', 'd', -1]):
        print("Invalid query input format.")
        sys.exit(1)
    
    # os.system("python3 DataConvertor.py")
    
    os.system("clear")
    # Construct the shell command to run the query
    
    command = "python3 mapper.py {} {} {} {} | sort -n | python3 combiner.py | sort -n | python3 reducer.py > result.txt".format(country_name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'), query)
    
    # Execute the command
    os.system(command)

if __name__ == "__main__":
    main()

