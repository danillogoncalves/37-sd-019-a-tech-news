from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598
    return [
        (news["title"], news["url"])
        for news in search_news({"title": {"$regex": title, "$options": "i"}})
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
