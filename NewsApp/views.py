from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.
def index(request):
    news_api = NewsApiClient(api_key="46fdf3d518e44c769d3c6c5055e49c4f")
    topheadlines = news_api.get_top_headlines(language="en")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'Index.html', context={"mylist": mylist})


def sports(request):
    news_api = NewsApiClient(api_key="852068c180154060820c5bb0aa46dc8e")
    topheadlines = news_api.get_top_headlines(language="en", category="sports")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'sports.html', context={"mylist": mylist})


def politics(request):
    news_api = NewsApiClient(api_key="852068c180154060820c5bb0aa46dc8e")
    topheadlines = news_api.get_top_headlines(language="en",
                                              category="business")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'politics.html', context={"mylist": mylist})


def movies(request):
    news_api = NewsApiClient(api_key="852068c180154060820c5bb0aa46dc8e")
    topheadlines = news_api.get_top_headlines(language="en",
                                              category="entertainment")
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'movies.html', context={"mylist": mylist})
