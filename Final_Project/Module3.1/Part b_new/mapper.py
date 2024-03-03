import sys
from datetime import datetime

def calculate_change(start_value, end_value):
    if start_value == 0:
        return 0
    return ((end_value - start_value) / start_value) * 100

def find_closest_country(query, country_data):
    closest_country = None
    min_difference = float('inf')

    for country, data in country_data.items():
        if query == 'a':
            value = data[0]
        elif query == 'b':
            value = data[1]
        elif query == 'c':
            value = data[2]
        elif query == 'd':
            value = data[3]
        else:
            return None

        difference = abs(value - country_data[query][0])

        if difference < min_difference and difference != 0:
            min_difference = difference
            closest_country = country

    return closest_country

def main():
    if len(sys.argv) != 5:
        print("Usage: python mapper.py <country_name> <start_date> <end_date> <query>")
        sys.exit(1)

    country_name = sys.argv[1]
    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]
    query = sys.argv[4]
#    print(country_name, start_date_str, end_date_str, query)

    try:
        start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y')
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        sys.exit(1)

    country_data = []
    flag=0
    with open('worldometers_countrylist.txt', 'r') as file:
        for line in file:
            data = line.strip().replace(':', "").replace("-", "")
#            print(country_name.strip(), data)
            country_data.append(data)
            if(country_name.strip()==data):
                flag=1
#                print("country found")
    
#    print(country_data)
    if flag==0:
        print("Country not found.")
        sys.exit(1)
#    string =
    print("-1,{},{},{},{}".format(country_name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'), query), end='\n')
#    print(country_data)
    for i in country_data:
#        print(i)
        if(i.strip()!=''):
            if(query=='a'):
                try:
                    abc = open('{}_ActiveCases.txt'.format(i), 'r+',encoding='utf-8')
#                    print(a.readlines())
                    for l in abc :
#                        print(l)
                        try:
                            data = l.strip().split(',')
                            country = data[0]
                            date = datetime.strptime(data[1].strip(), '%d-%m-%Y')
                            active_cases = int(data[2].strip())
    #                        daily_death = int(data[3])
    #                        new_recovered = int(data[4])
    #                        new_cases = int(data[5])
                            print("{} {} {}".format(country, date.strftime('%d-%m-%Y'), active_cases))
                        except:
                            continue
                except:
                    pass
            elif(query=='b'):
                try:
                    abc = open('{}_ActiveCases.txt'.format(i), 'r+',encoding='utf-8')
#                    print(a.readlines())
                    for l in abc :
#                        print(l)
                        try:
                            data = l.strip().split(',')
                            country = data[0]
                            date = datetime.strptime(data[1].strip(), '%d-%m-%Y')
                            active_cases = int(data[2].strip())
    #                        daily_death = int(data[3])
    #                        new_recovered = int(data[4])
    #                        new_cases = int(data[5])
                            print("{} {} {}".format(country, date.strftime('%d-%m-%Y'), active_cases))
                        except:
                            continue
                except:
                    pass
            elif(query=='c'):
                try:
                    abc = open('{}_ActiveCases.txt'.format(i), 'r+',encoding='utf-8')
#                    print(a.readlines())
                    for l in abc :
#                        print(l)
                        try:
                            data = l.strip().split(',')
                            country = data[0]
                            date = datetime.strptime(data[1].strip(), '%d-%m-%Y')
                            active_cases = int(data[2].strip())
    #                        daily_death = int(data[3])
    #                        new_recovered = int(data[4])
    #                        new_cases = int(data[5])
                            print("{} {} {}".format(country, date.strftime('%d-%m-%Y'), active_cases))
                        except:
                            continue
                except:
                    pass
                    
            elif(query=='d'):
                try:
                    abc = open('{}_ActiveCases.txt'.format(i), 'r+',encoding='utf-8')
#                    print(a.readlines())
                    for l in abc :
#                        print(l)
                        try:
                            data = l.strip().split(',')
                            country = data[0]
                            date = datetime.strptime(data[1].strip(), '%d-%m-%Y')
                            active_cases = int(data[2].strip())
    #                        daily_death = int(data[3])
    #                        new_recovered = int(data[4])
    #                        new_cases = int(data[5])
                            print("{} {} {}".format(country, date.strftime('%d-%m-%Y'), active_cases))
                        except:
                            continue
                except:
                    pass
            
    
#
#    country_values = country_data[country_name]
#    start_active, start_death, start_recovered, start_cases = country_values
#
#    end_values = (0, 0, 0, 0)
#
#    for country, data in country_data.items():
#        if start_date <= end_date:
#            end_values = data
#            break
#
#    end_active, end_death, end_recovered, end_cases = end_values
#
#    active_change = calculate_change(start_active, end_active)
#    death_change = calculate_change(start_death, end_death)
#    recovered_change = calculate_change(start_recovered, end_recovered)
#    cases_change = calculate_change(start_cases, end_cases)
#
#    if query == 'a':
#        print(f"a. Change in active cases in %: {active_change:.2f}%")
#    elif query == 'b':
#        print(f"b. Change in daily death in %: {death_change:.2f}%")
#    elif query == 'c':
#        print(f"c. Change in new recovered in %: {recovered_change:.2f}%")
#    elif query == 'd':
#        print(f"d. Change in new cases in %: {cases_change:.2f}%")
#    else:
#        print("Invalid query. Please provide a valid query: a, b, c, or d.")
#
#    closest_country = find_closest_country(query, country_data)
#    print(f"Closest country similar to query {query}: {closest_country}")

if __name__ == "__main__":
    main()
