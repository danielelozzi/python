import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

file_name = str(input("insert file name if this script is in the same directory of csv file or the complete path of file"))

pubmed = pd.read_csv(file_name)
main_link = str('https://pubmed.ncbi.nlm.nih.gov/')
for i,j in zip(range(pubmed.shape[0]), pubmed['PMID']):
    try:
        link = str(main_link + str(j))
        req = requests.get(link)
        text = str(BeautifulSoup(req.text, "html.parser"))
        citation = re.search('<em class="amount">(.*)</em>', text)
        if citation is None:
            pubmed.at[i,'citation_number'] = 0
        else:
            pubmed.at[i,'citation_number'] = citation.group(1)
    except:
        print(i, j)
pubmed.to_excel('all_articles.xlsx')
