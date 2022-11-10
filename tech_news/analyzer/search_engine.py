from tech_news.database import search_news
from datetime import datetime


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
    # https://stackoverflow.com/questions/502726/converting-date-between-dd-mm-yyyy-and-yyyy-mm-dd
    try:
        date_format_in_database = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        return [
            (news["title"], news["url"])
            for news in search_news({"timestamp": date_format_in_database})
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    # https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/94d0e996-1827-4fbc-bc24-c99fb592925b/section/d2b16462-a889-47fc-aa04-92517825b186/day/c436d6e0-7e4f-4d32-8e47-15c4f17e5e0f/lesson/12759a16-4246-4764-aeee-564ad0f187ec
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
        )
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"category": {"$regex": category, "$options": "i"}}
        )
    ]
