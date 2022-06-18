# Search

# Performs PR algorithm and provides ranking for searched terms
# ==> PR(A) = (1 - d) + d[PR(T1)/C(T1) + ..... + PR(Tn)/C(Tn)]
# Utilises bs4's BeautifulSoup for html parsing

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Imports

import os
from bs4 import BeautifulSoup

def file_rename():
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------------
# PageRank Functions

def page_rank_algo():
    pass

def pr_setup():
    pass

def call_pr(iterations):
    for x in range(iterations):
        for i in range(len(htmls)):
            page_rank_algo(i, inbound_pages[i])
        print(page_ranks)
      
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Globals

d = 0.85
htmls = [file for file in os.listdir() if file.endswith('.html')]
page_ranks = [1 for i in range(len(htmls))]
inbound_pages = [[] for i in range(len(htmls))] 
outbound_counts = []

if __name__ == '__main__':
    main()
