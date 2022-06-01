import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

from collections import Counter
from string import punctuation
from nltk.tokenize import RegexpTokenizer

from playwright.sync_api import sync_playwright

def get_dynamic_soup(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        soup = BeautifulSoup(page.content(), "html.parser")        
        browser.close()
        print(soup)
        return soup

def list_links(base_url):
    bsObj = get_dynamic_soup(base_url)
    #bsObj = BeautifulSoup(html.read(), features="html.parser");
    link_container = bsObj.find_all('span', class_='plugin_pagetree_children_span')
    # link_container = bsObj.find_all('a')
    print(link_container)

def count_header_and_main(base_url):
    #base_url = 'https://docs.blockbit.com/display/RC/Blockbit+Client'
    html = urlopen(base_url)
    bsObj = BeautifulSoup(html.read(), features="html.parser");

    wiki_content = bsObj.find_all("div",class_='wiki-content')
    main_header = bsObj.find_all(id="title-text")
    headers = main_header[0].get_text().split('\n')
    contents = wiki_content[0].get_text().split('\n')
    contador = 0
    for c in contents:
        tokenizer = RegexpTokenizer(r'\w+')
        bla = tokenizer.tokenize(c)
        contador += len(bla)
        
    for h in headers:
        tokenizer = RegexpTokenizer(r'\w+')
        bla = tokenizer.tokenize(h)
        contador += len(bla)
    print(contador)
    return (base_url,contador)
    
    

