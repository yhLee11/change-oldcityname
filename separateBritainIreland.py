import requests
from bs4 import BeautifulSoup
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
COUNTRY_LIST_FOLDER = THIS_FOLDER + "/BritainIreland/"
entries = os.listdir(THIS_FOLDER)  # for files on the current directory
country_list_entries = os.listdir(COUNTRY_LIST_FOLDER)  # for files on the current directory


routeList = []


def make_wikivoyage_html_soup(crawled_filename):

    openfile_crawled = open(COUNTRY_LIST_FOLDER+crawled_filename, "r")
    soup = BeautifulSoup(openfile_crawled.read(), 'html.parser')

    return soup


def makeList(soup):

    routeList = []

    #ex) London
    destination = soup.find('h1',  class_='wpb-name').get_text().encode('utf-8')

    #ex) Europe > Britain and Ireland > United Kingdomt > England
    rawData = soup.select('div.ext-wpb-pagebanner-subtitle > a')

    for info in rawData:
        title = info['title'].encode('utf-8')
        routeList.append(title)

    #ex) Europe > Britain and Ireland > United Kingdom > England > London
    routeList.append(destination)

    length=len(routeList)
    if length>2:
        dest = routeList[-1]
        country = routeList[2]
        f.write(country + ":" + dest + '\n')

    print(routeList)


#main
f = open("countryInfoOne.txt","w")

for entry in country_list_entries:
    if entry.endswith(".txt"):
        soup = make_wikivoyage_html_soup(entry)
        makeList(soup)

f.close()
