from app import app
from .models import Articles, News
from pip._vendor import requests
# import requests

# Getting api key
api_key = app.config["NEWS_API_KEY"]

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# Getting the articles base url
article_base_url = app.config["ARTICLE_API_BASE_URL"]


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    
    get_news_url = base_url.format(api_key)
    print(get_news_url)
 
    get_news_response = requests.get(get_news_url).json()

    if get_news_response['sources']:
        news_results_list = get_news_response['sources']
        news_results = process_results(news_results_list)

        return news_results


def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:

        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            news_obj = News(id, name, description, url,
                            category, language, country)
            news_results.append(news_obj)
    return news_results

# get articles


def get_articles(id):
    get_articles_url = article_base_url.format(id, api_key)

    get_articles_response = requests.get(get_articles_url).json()
    if get_articles_response['articles']:
        articles_results_list = get_articles_response['articles']
        articles_results = process_article(articles_results_list)

        return articles_results


def process_article(article_list):
    articles_results = []
    for article in article_list:
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        if urlToImage:
            article_result = Articles(
                id, author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_result)
    return articles_results

