import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
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
        return soup

def save_to_file(sopa):
    with open('pagina1.html', 'wb+') as f:
        f.write(sopa.content)

def get_from_file(arquivo):
    with open(arquivo) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        return soup

def get_link_list(base_url,arquivo):
    #bs_obj = get_dynamic_soup(base_url)
    bs_obj = get_from_file(arquivo)
    # save_to_file(bs_obj)
    #bsObj = BeautifulSoup(html.read(), features="html.parser");
    link_container = bs_obj.find_all('span', class_='plugin_pagetree_children_span')
    
    lista_links = []
    count = 0
    for l in link_container:
        item = dict()
        link = l.find_all('a',href=True)
        url = link[0]['href']
        title = link[0].text
        item['id'] = count
        item['url'] = url
        item['title'] = title
        lista_links.append(item)
        count = count + 1
    return lista_links

def count_header_and_main(base_url):
    #base_url = 'https://docs.blockbit.com/display/RC/Blockbit+Client'
    html = urlopen(base_url)

    bsObj = BeautifulSoup(html.read(), features="html.parser");

    wiki_content = bsObj.find_all("div",class_='wiki-content')
    main_header = bsObj.find_all(id="title-text")
    headers = main_header[0].get_text().split('\n')
    contents = wiki_content[0].get_text().split('\n')
    contador = 0
    texto = []
    for h in headers:
        tokenizer = RegexpTokenizer(r'\w+')
        bla = tokenizer.tokenize(h)
        contador += len(bla)
        texto.append(bla)
    for c in contents:
        tokenizer = RegexpTokenizer(r'\w+')
        bla = tokenizer.tokenize(c)
        contador += len(bla)
        texto.append(bla)
    return (base_url,contador,headers,contents)

    
    

