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
    '''
    Performs the PageRank Algorithm for a single page
    '''

    tn = 0
    for page in inbounds:
        tx = page_ranks[page]/outbound_counts[page]
        tn += tx
    pr = (1 - d) + (d * tn)
    page_ranks[file_index] = pr

def pr_setup():
    '''
    Gets all necessary information before performing the PageRank Algorithm
    - Finds which pages link to other pages
    - Number of links on a page
    - Page titles
    '''
    
    # iterates through every html file
    for i in range(len(htmls)):
        outbound = 0
        with open(f'webpages/{i}.html', 'r') as file:
            soup = BeautifulSoup(file, features="html.parser")

            # adds page to inbound list, and adds a count to outbound list
            for link in soup.find_all('a', href=True):
                linked_to = int(str(link['href']).strip('.html'))
                inbound_pages[linked_to].append(i)
                outbound += 1
            outbound_counts[i] = outbound
            page_titles[i] = soup.title.string # gets page title

def call_pr(iterations):
    '''
    Calls the PageRank Algorithm for the stated number of interations
    '''

    for x in range(iterations):
        for i in range(len(htmls)):
            page_rank_algo(i, inbound_pages[i])
        print(f'Iteration {x + 1}:  {page_ranks}')

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Search Functions

def input_search():
    '''
    Gets user search term and splits into separate words
    '''

    search_term = input('\nEnter search:  ')
    search_words = search_term.lower().split(' ')
    return search_term, search_words

def get_content(file_index):
    '''
    Reads the content of each webpage using BeautifulSoup
    Removes newlines and splits into a list of words
    '''

    with open(f'webpages/{file_index}.html', 'r') as file:
        soup = BeautifulSoup(file, features="html.parser")
        tag = soup.select_one('head')
        tag.decompose()
        file_words = soup.get_text().lower().replace('\n', ' ').split(' ')

        # deleting empty string data points in list
        del file_words[:4]
        del file_words[-2:]

        # getting a random snippet of the text
        rnd_num = random.randint(1, len(file_words) - 10)
        snippet = str(file_words[rnd_num] + ' ' +  file_words[rnd_num + 1] + ' ' + file_words[rnd_num + 2] + ' ' + file_words[rnd_num + 3] + ' ' + file_words[rnd_num + 4])
        page_snippets[file_index] = snippet
        return file_words

def get_search_score(file_index, search_term, search_words, file_words):
    '''
    Assigns a search score dependant on the number of times each part of the search term appears in a file
    - default score of 1
    - add 1 if exact search word is found
    - add 0.5 if search word is within another word
    '''

    score = 1
    if search_term.lower() == page_titles[file_index].lower():
        score += 10
    for i in file_words:
        for word in search_words:
            if word in i:
                score += 0.5
            if word == i:
                score += 1
    search_scores[file_index] = score

def call_search():
    '''
    Calls the search algorithm
    '''

    search_term, search_words = input_search()
    for i in range(len(htmls)):
        file_words = get_content(i)
        get_search_score(i, search_term, search_words, file_words)
    print(f'\nSearch Scores: {search_scores}')

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Ranking functions

def final_rank_scores():
    '''
    Calculates final rank scores for each page using following formula: Final Rank = PageRank * Search Score
    '''

    for i in range(len(htmls)):
        rank_scores[i] = page_ranks[i] * search_scores[i]
    print(f'\nFinal Combined Scores: {rank_scores}')

def create_ranked_list(rank_scores, page_titles, html_files, page_snippets):
    '''
    Creates a ranked list based on Final Rank, and makes corresponding lists for webpage titles, html files and page snippets
    '''

    # empty lists
    sorted_ranks = []
    sorted_titles = []
    sorted_files = []
    sorted_snippets = []
    i = 0

    # iterates until all pages are sorted
    while i < len(htmls):
        top = max(rank_scores) # finds top final rank

        # adds corresponding final rank, title, file and snippet to new lists
        sorted_ranks.append(top)
        sorted_titles.append(page_titles[rank_scores.index(top)])
        sorted_files.append(html_files[rank_scores.index(top)])
        sorted_snippets.append(page_snippets[rank_scores.index(top)])

        # removes the top rank for next loop
        index = rank_scores.index(top)
        del rank_scores[index]
        del page_titles[index]
        del html_files[index]
        del page_snippets[index]
        i += 1
    return sorted_ranks, sorted_titles, sorted_files, sorted_snippets

def display_results(sorted_ranks, sorted_titles, sorted_snippets, top_display_num):
    '''
    Outputs the top 5 pages, based on PageRank and the search term
    '''

    print('\n\nTop Results:\n')
    # checks if there are the required number of pages
    if len(htmls) < top_display_num:
        top_display_num = len(htmls)
    for i in range(top_display_num):
        print(f'\n{i + 1} - {sorted_titles[i]} (rank: {sorted_ranks[i]})')
        print(f'    - {sorted_snippets[i]}...')

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Select Webpage functions

def check_input_valid(inp, top_display_num):
    '''
    Check if the inputted number is valid
    '''

    if inp > 0 and inp <= top_display_num:
        return True
    return False
        
def select_page(sorted_htmls):
    '''
    Select which page the user wants to open
    '''

    selected_num = int(input("\nEnter the corresponding number of the webpage you'd like to open:  "))
    if check_input_valid(selected_num, 5):
        open_page(sorted_htmls, selected_num)

def open_page(sorted_htmls, index):
    '''
    Opens the webpage selected in the user's default browser
    '''

    file = sorted_htmls[index - 1]
    os.startfile(f'webpages\{file}')

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    '''
    Main function that calls all other functions
    '''

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
top_display_num = 5
current_path = os.getcwd()
htmls = [file for file in os.listdir(f'{current_path}/webpages/') if file.endswith('.html')]

# creating all lists required to the necessary length
page_ranks = [1 for x in range(len(htmls))]
inbound_pages = [[] for x in range(len(htmls))] 
outbound_counts = [0 for x in range(len(htmls))]
page_titles = ['' for x in range(len(htmls))]
page_snippets = ['' for x in range(len(htmls))]
search_scores = [1 for x in range(len(htmls))]
rank_scores = [0 for x in range(len(htmls))]

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Runs program

if __name__ == '__main__':
    main()
