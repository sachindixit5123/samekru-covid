#extract file
import sys
# start=input().split('-')
# end=input().split('-')
month_names = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


f=open("mapper_output.txt","w")
for i in [2020,2021,2022]:
        for month in month_names:
                f_str="news/"+str(i)+"/"+str(month)+".txt"
                try: 
                        file1=open(f_str,"r+",encoding='cp1252')
                except:
                        # print("file not found")
                        continue
                for line in file1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+str(i)
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                                

