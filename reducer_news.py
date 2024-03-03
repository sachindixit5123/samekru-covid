import sys

# Check if the correct number of arguments are passed (script name, start date, end date)
if len(sys.argv) != 3:
    print("Usage: script.py <Start Date(dd-mm-yyyy)> <End Date(dd-mm-yyyy)>")
    sys.exit(1)

month_names = [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october", "november", "december"
]

# Use command-line arguments for start and end dates
start_data = sys.argv[1].split('-')
end_data = sys.argv[2].split('-')

start_year = int(start_data[2])
start_month = int(start_data[1])-1
start_date = int(start_data[0])

end_year = int(end_data[2])
end_month = int(end_data[1])-1
end_date = int(end_data[0])

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
