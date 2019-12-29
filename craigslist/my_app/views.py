from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus# Automatically inserts & signs in the web url....eg:ad asd as = ad+20as+20as
import requests # For requesting data from the website
from . import models
# Create your views here.

BASE_CRAIGSLIST_URL='https://pune.craigslist.org/search/?query={}'
BASE_IMAGE_URL='https://images.craigslist.org/{}_300*300.jpg'
def home(request):
    return render(request,'base.html')

def new_search(request):
    save=request.POST.get('search')
    models.Search.objects.create(search=save)
    final_url=BASE_CRAIGSLIST_URL.format(quote_plus(save))
    response=requests.get(final_url)
    data=response.text
    soup=BeautifulSoup(data,features='html.parser')
    post_listings=soup.find_all('li',{'class':'result-row'})
    final_postings=[]

    for post in post_listings:
        post_title=post.find(class_ = 'result-title').text
        post_url=post.find('a').get('href')
        if post.find(class_ = 'result-price'):
            post_price=post.find(class_ = 'result-price').text
        else:
            post_price='N/A'

    if post.find(class_='result-image').get('data-imgid'):
        post_image_id=post.find(class_='result-image').get('data-ids').split(',')[0].split(':')
        post_image_url=BASE_IMAGE_URL.format(post_image_id)
        print(post_image_url)
    else:
        post_image_url='https://craigslist.org/images/peace.jpg'

    final_postings.append((post_title,post_url,post_price,post_image_url))

    stuff_for_frontend={
        'search':save,
        'final_postings':final_postings,
    }
    return render(request,'my_app/new_search.html',stuff_for_frontend)
