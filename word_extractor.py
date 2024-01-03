import requests
from bs4 import BeautifulSoup

from urllib.parse import urljoin

def Extract_From_This_Website(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    list_elements = soup.find_all('li', class_="word both-dicts")
    words = []
    for item in list_elements:
        span = item.find('a').find('span')
        if span: words.append(span.text.strip().lower())
        
    return words

if __name__ == "__main__":
    url = "https://www.thewordfinder.com/wordlist/all/?dir=ascending&field=word&pg=1&size=7"
    r = requests.get(url)
    domain_name = 'https://www.thewordfinder.com'
    soup = BeautifulSoup(r.content, 'html.parser')
    h3 = soup.find('h3', string ='Pagination')
    links = h3.find_next_sibling('nav', class_ = 'links').find_all('a')
    urls = []
    for link in links:
        href = link['href']
        href  = urljoin(domain_name, href)
        urls.append(href)
    with open('words.txt', 'a') as f:
        for url in urls:
            words = Extract_From_This_Website(url)
            # print(url)
            f.write('\n'.join(words))
            f.write('\n')