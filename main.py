from bs4 import BeautifulSoup
import urllib.request
import wikipediaapi as wa

# graph search problem
# using depth first search

en_wiki = wa.Wikipedia("en")


def is_valid_request(res):
    print(res.status_code)
    if res.status_code == 200:
        return True
    else:
        return False


# expects url in form /wiki/someTextHere
def is_valid_url(url):
    # print("url: " + url + "\nurl[:6]: " + url[:6])
    return (url is not None) and (len(url) > 6) and (url[0] != '#') and (url[:6] == "/wiki/")


def print_url(url):
    print("Current page: " + url + "\n")


next_link = input("Enter wiki url in form \"/wiki/PageTitle\" without surrounding quotes: ")
visited_links = []
# if title is not form /wiki/validTitle break
if not is_valid_url(next_link):
    print("Invalid title: " + next_link)
    exit()

while True:
    next_link = "https://en.wikipedia.org" + next_link
    # make http request with full link
    req = urllib.request.Request(next_link)
    content = urllib.request.urlopen(req).read()
    # if response status code is not 200 break
    # if not is_valid_request(response):
    #     print("Invalid response, status code: " + str(response.status_code))
    #     break
    # get content of http response
    # get beautiful soup html
    soup = BeautifulSoup(content, 'html.parser')
    # get the title from current header
    title = soup.findAll('h1', {'class': 'firstHeading'})[0].contents[0]
    if title == "Philosophy":
        print("We win! Current title is: " + title)
        exit()
    else:
        print("Current title issss: " + title)

    content = soup.findAll("div", {"class": "mw-parser-output"})[0]
    paragraphs = content.findAll('p')

    found_next_url = False
    for p in paragraphs:
        if not found_next_url:
            parenthesis = False
            for text in p.contents:
                if not found_next_url:
                    # print("Text line 62: " + str(text))
                    if "(" in text:
                        parenthesis = True
                    if ")" in text and parenthesis:
                        parenthesis = False

                    if not parenthesis:
                        if not isinstance(text, str):
                            try:
                                x = text['href']
                                if not x in visited_links:
                                    found_next_url = True
                                    next_link = x
                                    visited_links.append(next_link)
                            except:
                                pass


    # next_url_found = False
    # for paragraph in paragraphs:
    #     if not next_url_found:
    #         parenthesis_in_progress = False
    #         for thing in paragraph.contents:
    #             if not next_url_found:
    #                 # print(thing)
    #                 if "(" in thing:
    #                     parenthesis_in_progess = True
    #                 if ")" in thing and parenthesis_in_progress:
    #                     parenthesis_in_progress = False
    #
    #                 if not parenthesis_in_progress:
    #                     if not isinstance(thing, str):
    #                         try:
    #                             n = thing['href']
    #                             if not n in visited:
    #                                 next_url_found = True
    #                                 nexturl = n
    #                                 visited.append(nexturl)
    #                         except:
    #                             pass
    #
    # nexturl = "http://en.wikipedia.org" + nexturl
    # # get list of all unvisited possible urls
    # out_urls = [url.get('href') for url in soup.findAll('a') if
    #             (is_valid_url(url.get('href')) and
    #              url.get('href') not in visited_links)]
    # # if we have no possible urls to visit, break
    # # else add
    # if len(out_urls) == 0:
    #     print("Could not find Philosophy, out urls was empty! Breaking")
    #     break
    # else:
    #     # print(out_urls[0])
    #     title = out_urls[0]
    #     visited_links[title] = True
