import sys
from datetime import datetime

def main():
    country_data = {}
    start_date=None
    end_date=None
    for line in sys.stdin:
        if line.startswith("-1"):
            parts = line.strip().split(',')
            country_name = parts[1]
            start_date = datetime.strptime(parts[2], '%d-%m-%Y')
            end_date = datetime.strptime(parts[3], '%d-%m-%Y')
            query = parts[4]
            print("-1,{},{},{},{}".format(country_name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'), query), end='\n')

        else:
            data = line.strip().split()
            country_n=data[0]
#            print(data[1])
            date = datetime.strptime(data[1], '%d-%m-%Y')
            if(data[2]!='NA'):
                value = int(data[2])
            if country_n not in country_data:
                country_data[country_n] = []
            if start_date<=date and date <= end_date:
                print("{} {} {}".format(country_n, date.strftime('%d-%m-%Y'), value))

if __name__ == "__main__":
    main()
