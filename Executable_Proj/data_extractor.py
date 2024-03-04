import sys
import os
from urllib.request import Request, urlopen

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        os.makedirs(directory_path+'/2020')
        os.makedirs(directory_path+'/2021')
        os.makedirs(directory_path+'/2022')

# Example usage:
directory_path = "news"
create_directory(directory_path)
directory_path = "response"
create_directory(directory_path)
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
years = [2020,2021,2022]

for year in years:
    for month in months:
        link= f'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{month}_{year}'
        req = Request(link,headers ={'User-Agent':'Mozilla/5.0'})
        webpage = urlopen(req).read()
        mydata = webpage.decode("utf8")
        f=open('news.html','w',encoding="utf-8")
        f.write(mydata)
        os.system(f"python3 getNews.py ./news/{year}/{month}.txt")
        # f1=open(f'./news/{year}/{month}.txt','w+',encoding="utf-8")
        # f1.write(str1)
        f.close()

for year in years:
    for month in months:
        try:
            link= f'https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_{month}_{year}'
            req = Request(link,headers ={'User-Agent':'Mozilla/5.0'})
            webpage = urlopen(req).read()
            mydata = webpage.decode("utf8")
            f=open('response.html','w',encoding="utf-8")
            f.write(mydata)
            os.system(f"python3 getresponse.py ./response/{year}/{month}.txt")
            # f1=open(f'./news/{year}/{month}.txt','w+',encoding="utf-8")
            # f1.write(str1)
            f.close()
        except:
                continue
        
