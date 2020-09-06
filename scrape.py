import requests
from bs4 import BeautifulSoup
import pprint
import re
import hashlib
import html2text

url = 'https://www.sacred-texts.com/hin/'
res = requests.get(url)
content = BeautifulSoup(res.text, 'html.parser')
links = content.select('.c_t')

def get_href(links):
    CHILDREN = []
    HREFS = []
    hr = re.compile(".*href=.*")
    for item in links:
        children = list(item.children)
        CHILDREN.append(children[0])
    for idx, child in enumerate(CHILDREN):
        if (hr.match(str(child)) != None):
            href = CHILDREN[idx].get('href', None)
            HREFS.append(href)
    return HREFS

def make_links(href):
    URLS = []
    for h in href:
        new_url = url + h
        URLS.append(new_url)
    return URLS

def follow_links(url):
    IndexSet = []
    hr = re.compile(".*.htm.*")
    idx = re.compile('.*index.*')
    for u in url:
        URL = u
        res = requests.get(URL)
        content = BeautifulSoup(res.text, 'html.parser')
        for i in content.find_all('a'):
            index = i.get('href')
            if (hr.match(str(index)) != None):
                if (idx.match(str(index)) == None):
                    group = [URL, index]
                    IndexSet.append(group)
    return IndexSet

def final_links(links):
    EndLinks = []
    for i in range(len(links)):
        string = links[i][0]
        cut = re.sub('index.htm$', '', string)
        end = cut + links[i][1]
        EndLinks.append(end)
    return EndLinks

def get_content(links):
    LinkGroups = {}
    for l in range(len(links)):
        html = requests.get(links[l])
        htmltext = html2text.html2text(html.text)
        utf8 = htmltext.encode('utf-8')
        result = hashlib.md5(htmltext.encode())
        LinkHash = result.hexdigest()
        f = open("ScrapeData/" + LinkHash, "w+")
        f.write(str(utf8))
        LinkGroups[LinkHash] = links[l]
    return LinkGroups

HR = get_href(links)
L = make_links(HR)  
IS = follow_links(L)
AllLinks = final_links(IS)
ContentGroup = get_content(AllLinks)
pprint.pprint(ContentGroup)