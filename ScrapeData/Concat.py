filenames = ['CLinks.txt', 'CLinks2.txt', 'CLinks3.txt', 'CLinks4.txt', 'CLinks5.txt']
with open('CLinksAll.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())