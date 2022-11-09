import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news = []
    for header in selector.css(".entry-title"):
        url_news = header.css("h2 a::attr(href)").get()
        news.append(url_news)
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news = {}
    news["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    news["title"] = selector.css(".entry-title::text").get().strip()
    news["timestamp"] = selector.css("li.meta-date::text").get()
    news["writer"] = selector.css("a.url.fn.n::text").get()
    news["comments_count"] = len(selector.css(".comment-list li").getall())
    news["summary"] = "".join(
        selector.css(".entry-content p")[0].css("*::text").getall()
    ).strip()
    news["tags"] = selector.css("a[rel='tag']::text").getall()
    news["category"] = selector.css("span.label::text").get()
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://blog.betrybe.com/"
    news_list = []

    while len(news_list) < amount:
        page = fetch(url)
        news_list_url = scrape_novidades(page)
        for news_url in news_list_url:
            news = scrape_noticia(fetch(news_url))
            news_list.append(news)

        url = scrape_next_page_link(page)

    news_list = news_list[:amount]

    create_news(news_list)

    return news_list
