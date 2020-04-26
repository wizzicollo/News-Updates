from app import app
import urllib.request,json
from .models import News , Articles

News = news.News
Articles = article.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the News base url
base_url = app.config["NEWS_API_BASE_URL"]
