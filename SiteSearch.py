import requests
from bs4 import BeautifulSoup
import pprint
import re
import html2text

def find_word(filename, word):
    LINKS = {}
    UseableLinks = []
    with open(filename) as fh:
        for line in fh:
            h, l = line.strip().split('=')
            LINKS[h] = l.strip()
    FILE = list(LINKS.keys())
    URL = list(LINKS.values())
    for i in range(len(FILE)):
        f = open(FILE[i])
        content = str(f.read())
        if content.find(word) > 0:
            use_link = URL[i]
            lines = [sentence + '.' for sentence in content.split('.') if word in sentence]
            use_line = lines[0]
            group = (use_line, use_link)
            UseableLinks.append(group)
    return UseableLinks

word = input('Enter a word:')
while word == '':
    word = input('Enter a word:')

links = "CLinksAll.txt"
#links = 'CLinks.txt'
#links2 = 'CLinks2.txt'
#links3 = 'CLinks3.txt'
#links4 = 'CLinks4.txt'
#links5 = 'CLinks5.txt'

All_Links = find_word(links, word)
#All_Links2 = find_word(links2, word)
#All_Links3 = find_word(links3, word)
#All_Links4 = find_word(links4, word)
#All_Links5 = find_word(links5, word)

#Use_Links = All_Links + All_Links2 + All_Links3 + All_Links4 + All_Links5
#pprint.pprint(Use_Links)
pprint.pprint(All_Links)