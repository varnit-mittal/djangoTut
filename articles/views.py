from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# Create your views here.

@csrf_protect
@login_required
def article_create_view(request):
    form=ArticleForm(request.POST or None)
    context={
        'form':form
    }
    if form.is_valid():
        article_obj=form.save()
        context['form']=ArticleForm()
        # title=request.POST.get('title')
        # content=request.POST.get('content')
        # article_obj=Article.objects.create(title=title,content=content)
        context["obj"] = article_obj
        context["created"]=True
    return render(request,"articles/create.html",context=context)

def article_search_view(request):
    article_obj=None
    query_dict=dict(request.GET)
    query=query_dict.get('q')
    try:
        query=int(query[0])
    except:
        query=None
    if query:
        article_obj=Article.objects.get(id=query)
    context={
        "object": article_obj,
    }
    return render(request,"articles/search.html",context=context)

def article_detail_view(request,id=None):
    article_obj=None
    if id is not None:
        article_obj=Article.objects.get(id=id)
    context={
        "object":article_obj,

    }
    return render(request,"articles/detail.html",context=context)

