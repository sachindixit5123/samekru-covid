import sys
from datetime import datetime

def calculate_change(start_value, end_value):
    if start_value == 0:
        return 0
#    print(end_value, start_value,((end_value - start_value) / start_value) * 100)
    return ((end_value - start_value) / start_value) * 100

def find_closest_country(given_country, given_value, query, country_data):
    closest_country = None
    min_difference = float('inf')
    

    for country in country_data:
#        print(country, country_data[country])
        if(country!=given_country):
            maxdate=None
            maxval=None
            mindate=None
            minval=None
            for i in country_data[country]:
                if(maxdate is None or maxdate<i[0]):
                    maxdate=i[0]
                    maxval=i[1]
                if(mindate is None or mindate>i[0]):
                    mindate=i[0]
                    minval=i[1]
            date = mindate
            start_active = minval
            end_date = maxdate
            end_active = maxval
#            print(date, start_active, end_date, end_active)
#            print(start_values)
#            print(end_values)
            
            value = calculate_change(start_active, end_active)
#            print(value, given_value)
            difference = abs(value - given_value)
#            print(difference)
            if difference < min_difference:
                min_difference = difference
                closest_country = country
#                print(closest_country, min_difference)
    
    return closest_country, min_difference

def main():
    country_data = {}
    start_date=None
    end_date=None
    for line in sys.stdin:
#        print(line)
        if line.startswith("-1"):
#            print("TRUE")
            parts = line.strip().split(',')
            country_name = parts[1]
            start_date = datetime.strptime(parts[2], '%d-%m-%Y')
            end_date = datetime.strptime(parts[3], '%d-%m-%Y')
            query = parts[4]

            if country_name not in country_data:
                country_data[country_name] = []

        else:
            data = line.strip().split()
            country_n=data[0]
            date = datetime.strptime(data[1], '%d-%m-%Y')
            value = int(data[2])
            
            if country_n not in country_data:
                country_data[country_n] = []
            if start_date<=date and date <= end_date:
                country_data[country_n].append((date, value))
#    print(country_data)
#    print(country_data)
    for country in country_data:
        
#        print(country, country_data[country])
        if(country.replace(" ", "")==country_name.replace(" ", "")):
            start_values = country_data[country][0]
            end_values = country_data[country][-1]
            maxdate=None
            maxval=None
            mindate=None
            minval=None
            for i in country_data[country]:
                if(maxdate is None or maxdate<i[0]):
                    maxdate=i[0]
                    maxval=i[1]
                if(mindate is None or mindate>i[0]):
                    mindate=i[0]
                    minval=i[1]
            
            date = mindate
            start_active = minval
            end_date = maxdate
            end_active = maxval
#            print(date, start_active, end_date, end_active)
#            print(date, start_active, start_death, start_recovered, start_cases)
#            print(end_date, end_active, end_death, end_recovered, end_cases)
            active_change = calculate_change(start_active, end_active)
            

            print(f"For the given country {country}:")
            print(f"Query {query} Change is in %: {active_change:.2f}%")
           

            closest_country, min_difference = find_closest_country(country_name, active_change, query, country_data)
            print(f"Closest country similar to query {query}: {closest_country} with difference as {min_difference}")

if __name__ == "__main__":
    main()
