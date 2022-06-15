# Search

# Performs PR algorithm and provides ranking for searched terms
# ==> PR(A) = (1 - d) + d[PR(T1)/C(T1) + ..... + PR(Tn)/C(Tn)]
# Utilises bs4's BeautifulSoup for html parsing

def file_rename():
  pass

def page_rank_algo():
  pass

def pr_setup():
  pass

def main():
  pass

d = 0.85
htmls = [file for file in os.listdir() if file.endswith('.html')]
page_ranks = [1 for i in range(len(htmls))]
inbound_pages = [[] for i in range(len(htmls))] 
outbound_counts = []

if __name__ == '__main__':
    main()
