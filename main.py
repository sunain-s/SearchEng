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
    file_rename()
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Globals

d = 0.85
current_path = os.getcwd()
htmls = [file for file in os.listdir(f'{current_path}/webpages/') if file.endswith('.html')]
page_ranks = [1 for x in range(len(htmls))]
inbound_pages = [[] for x in range(len(htmls))] 
outbound_counts = [0 for x in range(len(htmls))]
page_titles = ['' for x in range(len(htmls))]
search_scores = [1 for x in range(len(htmls))]
rank_scores = [0 for x in range(len(htmls))]

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Runs program

if __name__ == '__main__':
    main()
