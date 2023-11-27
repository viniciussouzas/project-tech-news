import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    info_new = {}
    selector = Selector(html_content)

    info_new["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    info_new["title"] = selector.css("h1::text").get().strip()
    info_new["timestamp"] = selector.css(".meta-date ::text").get()
    info_new["writer"] = selector.css(
        ".title-author a::text").re_first(r'\b(\w+\s\w+)\b')
    info_new["reading_time"] = int(
        selector.css(".meta-reading-time ::text").re_first(r'\d+'))
    info_new["summary"] = ''.join(selector.css(
        ".entry-content > p:first-of-type *::text").getall()).strip()
    info_new["category"] = selector.css(".label ::text").get()

    return info_new


# Requisito 5
def get_tech_news(amount):
    first_page = "https://blog.betrybe.com"
    html_content = fetch(first_page)
    url_list = scrape_updates(html_content)
    counter = len(url_list)

    while True:
        next_page = scrape_next_page_link(html_content)

        if next_page is None:
            break

        html_content = fetch(next_page)
        new_url = scrape_updates(html_content)
        url_list.extend(new_url)
        counter += len(new_url)
        if counter >= amount:
            break

    news_list = []

    for index in range(amount):
        html_content = fetch(url_list[index])
        news_list.append(scrape_news(html_content))
    create_news(news_list)

    return news_list
