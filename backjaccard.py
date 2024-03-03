#extract file
import sys
import os
# start=input().split('-')
# end=input().split('-')
month_names = [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october", "november", "december"
]

country = sys.argv[1]
f=open("mapper_output.txt","w+", encoding='utf-8')
if(country=='Singapore'):
        f1=open('Singapore (2020).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2020"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Singapore (2021).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2021"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Singapore (2022).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2022"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
elif(country=='Malaysia'):
        f1=open('Malaysia (2020).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2020"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Malaysia (2021).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2021"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Malaysia (2022).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2022"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Malaysia (2023).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2023"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Malaysia (2024).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2024"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
elif(country=='England'):
        f1=open('England (January–June 2020).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2020"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('England (July–December 2020).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2020"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('England (2021).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2021"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('England (2022).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2022"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
elif(country=='India'):
        f1=open('India (January–May 2020).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2020"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('India (June–December 2020).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2020"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('India (2021).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2021"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
elif(country=='Australia'):
        f1=open('Australia_2020.txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2020"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Australia_(Jan-Jun 21).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2021"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Australia(Jul-Dec 21).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2021"
                        f.write(':'.join(data) + '\n')
                except:
                        continue
        f1=open('Australia_(2022).txt','r')
        for line in f1.readlines():
                line=line.strip()
                try:
                        if(line==''):
                                continue
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0]+' '+"2022"
                        f.write(':'.join(data) + '\n')
                except:
                        continue     
else:
        print("invalid country")
        exit()
        
f.close()

start_data = sys.argv[2].split('-')
start_year = int(start_data[2])
start_month = int(start_data[1])-1
start_date=int(start_data[0])
end_data = sys.argv[3].split('-')
end_year = int(end_data[2])
end_month = int(end_data[1])-1
end_date=int(end_data[0])
f=open("mapper_output.txt","r+", encoding='utf-8')
final = open("reducer_output.txt",'w+', encoding='utf-8')
flag=0
while True:
    line = f.readline()
    # print(line)
    try:
        if not line :
            break
        key = line.split(":")[0].split(' ')
        # print(key)
        if((month_names.index(key[1].strip().lower())>=start_month and int(key[2].strip())>=start_year) and int(key[0].strip())>=start_date ):
            flag=1
        if(int(key[2].strip())>end_year):
            break
        if(int(key[2].strip())==end_year and month_names.index(key[1].strip().lower())>end_month):
            break
        if(int(key[2].strip())==end_year and month_names.index(key[1].strip().lower())==end_month and int(key[0].strip())>=end_date):
            break
        if(flag):
            final.write(line)
        if(month_names.index(key[1].strip().lower())>=end_month and int(key[0].strip())>=end_date and int(key[2].strip())>=end_year):
            break
    except:
        continue
f.close()
final.close()