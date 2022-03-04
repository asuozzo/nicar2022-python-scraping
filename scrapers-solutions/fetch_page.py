import requests
from time import sleep

def fetch_page(url, params={}):
    sleep(1)

    r = requests.get(url, params=params)
    
    return r.text

if __name__=="__main__":
    
    text = fetch_page("https://nicar22-scraping.herokuapp.com/")
    print(text)