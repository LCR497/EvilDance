import requests
from bs4 import BeautifulSoup

list_evil = []
def get_data():
    for i in range(1,20):
        url = f'https://evilinsult.com/generate_insult.php?type=plain&lang=en&_=166070397380{i}'
        r = requests.get(url, verify=False)
        print(r)
        soup = BeautifulSoup(r.content, 'html.parser')
        list_evil.append(soup)
    return list_evil

print(get_data())