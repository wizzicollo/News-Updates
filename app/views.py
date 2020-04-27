from flask import render_template
from app import app
from .requests import get_articles,get_sources

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news_source = get_sources()
    title = 'Home - Welcome to The best News  Highlight Website Online'
    return render_template('index.html', title = title,news_source = news_source )



@app.route('/articles/<id>')
def news(id):
    article = get_articles(id)
    print(article)
    return render_template('articles.html',article = article)
