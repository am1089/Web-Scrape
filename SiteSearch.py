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
#links = "Clinks.txt"

All_Links = find_word(links, word)

pprint.pprint(All_Links)