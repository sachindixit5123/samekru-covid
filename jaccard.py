from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')


if len(sys.argv) != 4:
    print("Usage: script.py <Country_name> <Start Date(dd-mm-yyyy)> <End Date(dd-mm-yyyy)>")
    sys.exit(1)

def get_news(country,start,end):
    os.system(f"python3 backjaccard.py {country} {start} {end}")
    f = open("reducer_output.txt",'r')
    data =""
    while True:
        line = f.readline()
        if not line:
            break
        data += line.split(':')[1]
    return data

# Assuming you have a function to calculate Jaccard similarity
def calculate_jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# List of countries
countries = ["Australia","India","Malaysia","England","Singapore"]
country1 = sys.argv[1]. strip()
# start_data = input("Enter Start Date(dd-mm-yyyy) : ")
# end_data = input("Enter End Date(dd-mm-yyyy) : ")
start_data = sys.argv[2]
end_data = sys.argv[3]


# Retrieve and preprocess news for Australia
australia_news = get_news(country1,start_data,end_data)
australia_words = set(set(word_tokenize(australia_news.lower())) - set(stopwords.words('english')))

# Calculate Jaccard similarity for each country
max_similarity = 0
closest_country = ""
for country in countries:
    try:
        if country != country1:
            country_news = get_news(country,start_data,end_data)
            country_words = set(set(word_tokenize(country_news.lower())) - set(stopwords.words('english')))
            similarity = calculate_jaccard_similarity(australia_words, country_words)
            print(f'{country1} & {country} similarity : {similarity}')
            if similarity > max_similarity:
                max_similarity = similarity
                closest_country = country
    except:
        continue

with open("jaccardoutput.txt", 'w') as file:
    file.write(f"The closest country is: {closest_country} with Jaccard similarity: {max_similarity}")
