from bs4 import BeautifulSoup
import requests
import wikipediaapi as wa

# check if link is valid

# graph search problem

en_wiki = wa.Wikipedia("en")


def is_valid_request(res):
    print(res.status_code)
    if res.status_code == 200:
        return True
    else:
        return False


starting_page_title = input("Enter start page: ")
wiki_url = "https://en.wikipedia.org/wiki/" + starting_page_title
visited_links = []
res = requests.get(wiki_url)



#
# while is_valid_wiki_link(wiki_url):
#     req = urllib.request.Request(wiki_url)
