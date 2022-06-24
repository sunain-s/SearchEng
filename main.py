# Search

# Performs PR algorithm and provides ranking for searched terms
# ==> PR(A) = (1 - d) + d[PR(T1)/C(T1) + ..... + PR(Tn)/C(Tn)]
# Utilises bs4's BeautifulSoup for html parsing

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Imports

import os
from bs4 import BeautifulSoup

def file_rename():
    for file in htmls:
        if int(str(file).strip('.html')) != htmls.index(file):
            os.rename(f'webpages/{file}', f'{htmls.index(file)}.html')

#-------------------------------------------------------------------------------------------------------------------------------------------------
# PageRank Functions

def page_rank_algo(file_index, inbounds):
    tn = 0
    for page in inbounds:
        tx = page_ranks[page]/outbound_counts[page]
        tn += tx
    pr = (1 - d) + (d * tn)
    page_ranks[file_index] = pr

def pr_setup():
    for i in range(len(htmls)):
        outbound = 0
        with open(f'webpages/{i}.html', 'r') as file:
            soup = BeautifulSoup(file, features="html.parser")

            for link in soup.find_all('a', href=True):
                linked_to = int(str(link['href']).strip('.html'))
                inbound_pages[linked_to].append(i)
                outbound += 1
            outbound_counts[i] = outbound
            page_titles[i] = soup.title.string

def call_pr(iterations):
    for x in range(iterations):
        for i in range(len(htmls)):
            page_rank_algo(i, inbound_pages[i])
        print(page_ranks)
      
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Search Functions

def input_search():
    search_term = input('Enter search:  ')
    search_words = search_term.split(' ')
    return search_words

def get_content(file_index):
    with open(f'webpages/{file_index}.html', 'r') as file:
        soup = BeautifulSoup(file, features="html.parser")
        tag = soup.select_one('head')
        tag.decompose()
   
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
