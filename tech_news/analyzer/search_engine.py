from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    response = []
    news = search_news({"title": {"$regex": title, "$options": "i"}})

    for new in news:
        response.append((new["title"], new["url"]))

    return response


# Requisito 8
def search_by_date(date):
    try:
        converted_date = datetime.strptime(
            date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    response = []

    news = search_news({"timestamp": converted_date})

    for new in news:
        response.append((new["title"], new["url"]))

    return response


# Requisito 9
def search_by_category(category):
    response = []

    news = search_news({"category": {"$regex": category, "$options": "i"}})

    for new in news:
        response.append((new["title"], new["url"]))

    return response
