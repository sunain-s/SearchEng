# Search

# Performs PR algorithm and provides ranking for searched terms
# ==> PR(A) = (1 - d) + d[PR(T1)/C(T1) + ..... + PR(Tn)/C(Tn)]
# Utilises bs4's BeautifulSoup for html parsing

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Imports

import os
import random
from bs4 import BeautifulSoup

def file_rename():
    '''
    Renames new files to the standardised file names: 0.html, 1.html etc
    Allows for simpler use within the program => file name is the index of the file in a list
    '''

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
        file_words = soup.get_text().replace('\n', ' ').split(' ')
        del file_words[:4]
        del file_words[-2:]
        return file_words
    
def get_search_score(file_index, search_words, file_words):
    score = 1
    for i in file_words:
        for word in search_words:
            if word in i:
                score += 0.5
            if word == i:
                score += 1
    search_scores[file_index] = score

def call_search():
    search_words = input_search()
    for i in range(len(htmls)):
        file_words = get_content(i)
        get_search_score(i, search_words, file_words)
    print(f'\nSearch Scores: {search_scores}')
    
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Ranking functions

def final_rank_scores():
    for i in range(len(htmls)):
        rank_scores[i] = page_ranks[i] * search_scores[i]
    print(f'\nFinal Combined Scores: {rank_scores}')

def create_ranked_list(rank_scores, page_titles, html_files):
    sorted_ranks = []
    sorted_titles = []
    sorted_files = []
    i = 0
    
    while i < len(htmls):
        top = max(rank_scores)
        sorted_ranks.append(top)
        sorted_titles.append(page_titles[rank_scores.index(top)])
        sorted_files.append(html_files[rank_scores.index(top)])
        index = rank_scores.index(top)
        del rank_scores[index]
        del page_titles[index]
        del html_files[index]
        i += 1
    return sorted_ranks, sorted_titles, sorted_files

def display_results(sorted_ranks, sorted_titles):
    print('\n\nTop Results:\n')
    top_display_num = 5
    if len(htmls) < top_display_num:
        top_display_num = len(htmls)
    for i in range(top_display_num):
        print(f'{i + 1} - {sorted_titles[i]} (rank: {sorted_ranks[i]})')
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Select Webpage functions

def check_input_valid(inp):
    if inp > 0 and inp <= len(htmls):
        return True
    return False

def select_page(sorted_htmls):
    selected_num = int(input("\nEnter the corresponding number of the webpage you'd like to open:  "))
    if check_input_valid(selected_num):
        open_page(sorted_htmls, selected_num)

def open_page(sorted_htmls, index):
    file = sorted_htmls[index - 1]
    os.startfile(f'webpages\{file}')
    
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    file_rename()
    pr_setup()
    call_pr(100)
    call_search()
    final_rank_scores()
    sorted_ranks, sorted_titles, sorted_files, sorted_snippets = create_ranked_list(rank_scores[:], page_titles[:], htmls[:], page_snippets[:]) # passing in copies of the original lists
    display_results(sorted_ranks, sorted_titles, sorted_snippets, top_display_num)
    select_page(sorted_files)

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
