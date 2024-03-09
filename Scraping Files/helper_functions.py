import requests
from bs4 import BeautifulSoup

def get_soup(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    return(soup)

def find_ucla_focus(whole_set, tag):
    if whole_set.find(tag) is None:
        return('')
    else:
        return(whole_set.find(tag).text.replace(' Field of Study: ',''))
    
def clean_nebraska_links(whole_set, tag):
    if ':' in whole_set.find(tag, href=True)['href']:
        return('')
    else:
        return(''.join(['https://history.unl.edu/',whole_set.find(tag, href=True)['href']]))
    
def find_duke_focus(whole_set, tag, class_name):
    if whole_set.find(tag,{'class':class_name}) is None:
        return('')
    else:
        return(whole_set.find(tag,{'class':class_name}).text)