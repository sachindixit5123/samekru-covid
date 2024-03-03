from urllib.request import Request, urlopen
import activecases
import dailyDeaths
import newRecoveries
import newCases
from datetime import datetime

def downloadwebpage(url):
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('webpage.html','w',encoding="utf-8")
    f.write(mydata)
    f.close
    
countryURL = {}

continents=['Europe','North America','Asia','South America','Africa','Oceania']

file = open('worldometers_countrylist.txt','r')
for line in file:
    ex=False
    line = line.strip()
    if('-' in line):
        continue
    if(line==''):
        continue
    for continent in continents:
        if(continent in line):
            ex=True
            break
    if(ex):
        continue
    if(line.lower()=='usa'):
        url=f'https://www.worldometers.info/coronavirus/country/us/'
    elif(line.lower()=='vietnam'):
        url="https://www.worldometers.info/coronavirus/country/viet-nam/"
    else:
        url=f'https://www.worldometers.info/coronavirus/country/{line.replace(" ","-").lower()}/'
    countryURL[line]=url
file.close()
countries=countryURL.keys()
# for country in countries:
#     print(countryURL[country])
#     downloadwebpage(countryURL[country])
#     activeCases=activecases.getCurrentlyInfected()
#     dailyDeath=dailyDeaths.getDailyDeaths()
#     newRecovered=newRecoveries.getNewRecoveries()
#     newCase=newCases.getNewCases()
#     file.write(f'{country}\n------------------------------\nActive Cases: {activeCases}\nDaily Death: {dailyDeath}\nNew Recovered: {newRecovered}\nNew Cases: {newCase}\n\n')
countries=list(countryURL.keys())
n=len(countries)
#for i in range(0,n):
#    print(f"{i+1}. {countries[i]}")
#while(True):
#    try:
#        ch = int(input(f"Choose the Country with its keys in range (1,{n}): "))-1
#        if(ch<0 or ch>=n):
#            raise ValueError
#        break
#    except:
#        print(f"Expected value in range 1 to {n}")
#    
for ch in range(0, n):
    downloadwebpage(countryURL[countries[ch]])
    def fileWrite(filename,data,dates):
        file=open(filename,'w')
        if (data=='N/A' or dates=='N/A'):
            file.write('N/A')
        else:
            for i in range(0,len(dates)):
                try:
                    d=int(data[i])
                except:
                    d=0
                file.write(f'{dates[i]}\t{d}\n')
        file.close()
    dates1,activeCases=activecases.getCurrentlyInfected()
    
#    fileWrite('ActiveCases.txt',activeCases,dates1)
#    print(dates,activeCases)
    dates2,dailyDeath=dailyDeaths.getDailyDeaths()
#    fileWrite('DailyDeaths.txt',dailyDeath,dates2)
    dates3,newRecovered=newRecoveries.getNewRecoveries()
#    fileWrite('NewRecovered.txt',newRecovered,dates3)
    dates4,newCase=newCases.getNewCases()
#    fileWrite('NewCases.txt',newCase,dates4)
    union_set = set(dates1).intersection(set(dates2), set(dates3), set(dates4))
    # Convert the union set back to a list if needed
    converted_dates = []
    for date in dates1:
        try:
            converted_date = datetime.strptime(date, '%b %d, %Y').strftime('%d-%m-%Y')
            converted_dates.append(converted_date)
        except ValueError:
            pass
    # Sort the converted dates
    dates1 = sorted(converted_dates)

    converted_dates = []
    for date in dates2:
        try:
            converted_date = datetime.strptime(date, '%b %d, %Y').strftime('%d-%m-%Y')
            converted_dates.append(converted_date)
        except ValueError:
            pass
    # Sort the converted dates
    dates2 = sorted(converted_dates)

    converted_dates = []
    for date in dates3:
        try:
            converted_date = datetime.strptime(date, '%b %d, %Y').strftime('%d-%m-%Y')
            converted_dates.append(converted_date)
        except ValueError:
            pass
    # Sort the converted dates
    dates3 = sorted(converted_dates)
    
    
    converted_dates = []
    for date in dates4:
        try:
            converted_date = datetime.strptime(date, '%b %d, %Y').strftime('%d-%m-%Y')
            converted_dates.append(converted_date)
        except ValueError:
            pass
    # Sort the converted dates
    dates4 = sorted(converted_dates)
    
    
    
    
    dates1 = sorted(dates1, key=lambda x: datetime.strptime(x, '%d-%m-%Y'))
    dates2 = sorted(dates2, key=lambda x: datetime.strptime(x, '%d-%m-%Y'))
    dates3 = sorted(dates3, key=lambda x: datetime.strptime(x, '%d-%m-%Y'))
    dates4 = sorted(dates4, key=lambda x: datetime.strptime(x, '%d-%m-%Y'))
    
    def fileWrite(filename, country, values, dates):
        # Open the file in write mode
        with open(filename, 'w',encoding='utf-8') as file:
            # Write headers

            # Write data line by line
            for date, value in zip(dates, values):
                file.write(f"{country},{date},{value}\n")


        
    fileWrite('{}_ActiveCases.txt'.format(countries[ch]),countries[ch].replace(" ", ""), activeCases,dates1)
    fileWrite('{}_DailyDeaths.txt'.format(countries[ch]),countries[ch].replace(" ", ""), dailyDeath,dates2)
    fileWrite('{}_RecoveredCases.txt'.format(countries[ch]),countries[ch].replace(" ", ""), newRecovered,dates3)
    fileWrite('{}_NewCases.txt'.format(countries[ch]),countries[ch].replace(" ", ""), newCase,dates4)


#    print("Sorted Dates:")
#    for date in dates:
#        print(date)
#        print("Sorted Dates:")
#        for date in sorted_dates:
#            print(date)


    
#    activecases_dict = {k: v for k, v in zip(dates1, activeCases)}
#    dailyDeath_dict = {k: v for k, v in zip(dates2, dailyDeath)}
#    newRecovered_dict = {k: v for k, v in zip(dates3, newRecovered)}
#    newCase_dict = {k: v for k, v in zip(dates4, newCase)}
##    print(activecases_dict)
#    output = []
#
## Iterate over the dates list
#    for date in dates:
#        # Retrieve values from dictionaries if the date is present as a key
#        active_cases = activecases_dict.get(date, 'NA')
#        daily_death = dailyDeath_dict.get(date, 'NA')
#        new_recovered = newRecovered_dict.get(date, 'NA')
#        new_cases = newCase_dict.get(date, 'NA')
#        
#        # Append values to the output list
#        output.append([countries[ch], date, active_cases, daily_death, new_recovered, new_cases])
#
##    print("Output List:")
##    for item in output:
##        print(item)
#    
#    # Open the file in write mode
##    filename =
#    with open('{}.txt'.format(countries[ch]), "w") as file:
#        # Write data line by line
#       for i in output:
#            file.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n")
#    
