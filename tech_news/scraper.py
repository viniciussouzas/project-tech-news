import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(
            url, headers={"user-agent": "Fake user-agent"},
            timeout=3)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    url_list = []
    selector = Selector(html_content)

    url = selector.css(".cs-overlay-link ::attr(href)").getall()
    url_list.extend(url)

    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    try:
        next = selector.css(".next ::attr(href)").get()

        return next
    except IndexError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
