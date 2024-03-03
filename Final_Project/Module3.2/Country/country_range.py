#extract file
import sys
# start=input().split('-')
# end=input().split('-')
month_names = [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october", "november", "december"
]


country = input("Enter Country Name : ").strip()
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
# Specify the path to your text file
map_data=open("mapper_output.txt",'r', encoding='utf-8')
first_line=map_data.readline()
last_line=None
while(True):
        line = map_data.readline()
        if not line:
                break
        if(line.strip()!=''):
                last_line=line
# print(map_data)
# # Print the results
print(f"From Date: {first_line.split(':')[0]}")
print(f"To Date: {last_line.split(":")[0]}")



