import csv
import json

import requests
from bs4 import BeautifulSoup as BS, BeautifulSoup

#url = 'https://www.scopus.com/results/results.uri?src=s&sort=plf-f&st1=university+of+luxemburg+thesis&sid=b613f7156515fed3307d8b390bedf737&sot=b&sdt=b&sl=35&s=ALL%28university+of+luxemburg+thesis%29&cl=t&offset=1&ss=plf-f&ws=r-f&ps=r-f&cs=r-f&origin=resultslist&zone=queryBar'

url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0,5&q=thesis+luxembourg+university&scisbd=1'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)
#print (BS(page.content, 'lxml'))

soup = BeautifulSoup(page.content, 'html.parser')

#get all authers
ds_allAuthor = soup.find_all("div",class_="gs_a")
allAuthor = []
for autor in ds_allAuthor:
    allAuthor.append(autor.string)
    print(autor.string)
    
    
#get all document title
ds_documents = soup.find_all("h3",class_="gs_rt")
documents = []
for title in ds_documents:
    documents.append(title.string)
    print(title.string)
    
#get all date
ds_years = soup.find_all("div",class_="gs_a")
years = []
for year in ds_years:
    years.append(year.string)
    print(year.string)
    
    
#get all document title
ds_documents_samury = soup.find_all("div",class_="gs_rs")
documents_samury = []
for su in ds_documents_samury:
    documents_samury.append(su.contents[3].string)
    print(su.contents[1].string,su.contents[2].string,su.contents[3].string,su.contents[4].string)
    

print(json.dumps(allAuthor))

  
#Create list for the headers
headers = ["Author and year","title","description"]

#Open a new file to write to called ‘data.csv’
with open('data.csv', 'w', newline='') as csvfile:
    #Create a writer object with that file
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    #Loop through each element in titles and descriptions lists
    for i in range(len(allAuthor)):
        #Create a new row with the title and description at that point in the loop
        row = [allAuthor[i], documents[i], documents_samury[i]]
        writer.writerow(row)


