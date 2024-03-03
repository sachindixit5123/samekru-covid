#extract file
import sys

month_names = [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october", "november", "december"
]


start_data = input("Enter Start Date(dd-mm-yyyy) : ").split('-')
start_year = int(start_data[2])
start_month = int(start_data[1])-1
start_date=int(start_data[0])
end_data = input("Enter End Date(dd-mm-yyyy) : ").split('-')
end_year = int(end_data[2])
end_month = int(end_data[1])-1
end_date=int(end_data[0])
f=open("mapper_output.txt","r")
final = open("reducer_output.txt",'w')
flag=0
while True:
    line = f.readline()
    try:
        if not line :
            break
        key = line.split(":")[0].split(' ')
        # print(key)
        if(month_names.index(key[1].strip().lower())>=start_month and int(key[0].strip())>=start_date and int(key[2].strip())>=start_year):
            flag=1
        if(flag):
            final.write(line)
        if(month_names.index(key[1].strip().lower())>=end_month and int(key[0].strip())>=end_date and int(key[2].strip())>=end_year):
            break
    except:
        continue
