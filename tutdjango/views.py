"""
To render html webpages
"""
from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string

def article_home_view(request):
    return HttpResponse

def home_view(request,*args,**kwargs):
    '''
    Take in a request(django sends a request)
    Return HTML as a response (We pick to return the 
    response)
    '''

    number=random.randint(1,4)
    name="Varnit"

    article_obj=Article.objects.get(id=number)
    article_list=Article.objects.all() #this is a query set
    context={
        "my_list":article_list,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id
    }

    HTML_STRING=render_to_string("home-view.html",context=context)
    # HTML_STRING='''
    # <h1>{title} (id: {id})!</h1>
    # <p>{content}!</p>
    # '''.format(**context)
    return HttpResponse(HTML_STRING)