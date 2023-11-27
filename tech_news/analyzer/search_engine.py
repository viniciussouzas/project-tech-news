from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    response = []
    news = search_news({"title": {"$regex": title, "$options": "i"}})

    for new in news:
        response.append((new["title"], new["url"]))

    return response


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
